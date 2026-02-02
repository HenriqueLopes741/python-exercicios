import subprocess
import sys

def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ Erro ao executar:", cmd)
        print(e.stderr)
        sys.exit(1)

print("🚀 Git Bot iniciado...\n")

run_cmd("git status")

run_cmd("git add .")

msg = input("📝 Mensagem do commit: ")
run_cmd(f'git commit -m "{msg}"')

run_cmd("git push")

print("\n✅ Código enviado para o Git com sucesso!")
