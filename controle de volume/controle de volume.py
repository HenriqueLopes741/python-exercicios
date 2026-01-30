import cv2
import mediapipe as mp
import math
import time
import numpy as np
import pyautogui


CAMERA_ID = 0

SMOOTHING_ALPHA = 0.25     # Suavização (0.1 mais suave | 0.4 mais rápido)
VOLUME_UP_THRESHOLD = 1.35
VOLUME_DOWN_THRESHOLD = 0.75
DEADZONE_LOW = 0.85
DEADZONE_HIGH = 1.15
COOLDOWN_TIME = 0.18       # segundos entre comandos


cap = cv2.VideoCapture(CAMERA_ID)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)
mp_draw = mp.solutions.drawing_utils

prev_ratio = 1.0
last_action_time = 0

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    status_text = "Aguardando gesto..."

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        lm = hand.landmark

        # Pontos principais
        thumb = (int(lm[4].x * w), int(lm[4].y * h))
        index = (int(lm[8].x * w), int(lm[8].y * h))
        wrist = (int(lm[0].x * w), int(lm[0].y * h))
        middle = (int(lm[9].x * w), int(lm[9].y * h))

        # Distâncias
        pinch_dist = distance(thumb, index)
        hand_base = distance(wrist, middle)

        if hand_base > 0:
            ratio = pinch_dist / hand_base

            # Suavização exponencial
            ratio = (SMOOTHING_ALPHA * ratio) + ((1 - SMOOTHING_ALPHA) * prev_ratio)
            prev_ratio = ratio

            now = time.time()

            if now - last_action_time > COOLDOWN_TIME:
                if ratio > VOLUME_UP_THRESHOLD:
                    pyautogui.press("volumeup")
                    last_action_time = now
                    status_text = "🔊 Aumentando volume"

                elif ratio < VOLUME_DOWN_THRESHOLD:
                    pyautogui.press("volumedown")
                    last_action_time = now
                    status_text = "🔉 Diminuindo volume"

                elif DEADZONE_LOW <= ratio <= DEADZONE_HIGH:
                    status_text = "✋ Zona neutra"

        # Desenho
        cv2.circle(frame, thumb, 8, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, index, 8, (255, 0, 0), cv2.FILLED)
        cv2.line(frame, thumb, index, (255, 0, 0), 3)

        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

        # Barra visual
        bar_y = int(np.interp(ratio, [0.5, 1.6], [400, 150]))
        cv2.rectangle(frame, (30, 150), (60, 400), (0, 255, 0), 2)
        cv2.rectangle(frame, (30, bar_y), (60, 400), (0, 255, 0), cv2.FILLED)

        cv2.putText(frame, f"Ratio: {ratio:.2f}", (80, 170),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.putText(frame, status_text, (80, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Controle de Volume por Gestos (Avancado)", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
