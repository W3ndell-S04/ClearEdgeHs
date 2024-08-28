import psutil
import subprocess

def kill_edge_process():
    # Verifica se o processo do Microsoft Edge está em execução e o encerra
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'msedge.exe':
            proc.kill()

def clear_edge_data():
    # Corrige o caminho com espaços colocando-o entre aspas
    command = r'"C:\\Program Files (x86)\\Microsoft\\Edge\\Application.exe" --clear-browsing-data"'
    try:
        subprocess.run(command, shell=True, check=True)
        print("Dados de navegação limpos com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao limpar dados de navegação: {e}")

if __name__ == "__main__":
    # Mata o processo do Edge se estiver em execução
    kill_edge_process()

    # Limpa os dados de navegação
    clear_edge_data()
if __name__ == "__main__":
    kill_edge_process()
    clear_edge_data()
    print("Script concluído e encerrado.")
