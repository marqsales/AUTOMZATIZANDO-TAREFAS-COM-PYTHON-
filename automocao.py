import pyautogui as pa  # Importa a biblioteca pyautogui, usada para automação de interface gráfica
import time  # Importa a biblioteca time para controlar o tempo de espera entre as ações

pa.pause = 1  # Define o tempo de pausa padrão entre as ações do pyautogui como 1 segundo

# Abre o terminal (Ctrl + Alt + T no Ubuntu, por exemplo)
pa.hotkey('ctrl', 'alt', 't')  # Envia a combinação de teclas Ctrl + Alt + T para abrir o terminal
time.sleep(1)  # Espera 1 segundo para garantir que o terminal tenha tempo de abrir

# Escreve o comando para abrir o Firefox
pa.write('firefox')  # Digita 'firefox' no terminal
pa.press('ENTER')  # Pressiona Enter para executar o comando e abrir o Firefox
pa.click(x=2489, y=105)  # Clica em uma posição específica na tela (aqui, possivelmente para focar no Firefox)

# Acessa a URL do GLPI
pa.write('https://glpi.pc.pa.gov.br/index.php?redirect=%2Ffront%2Fcentral.php&error=3')  # Digita a URL do GLPI
pa.press('ENTER')  # Pressiona Enter para ir até a página
time.sleep(1)  # Espera 1 segundo para a página carregar

# Clica no campo de login (posicionando o cursor nas coordenadas indicadas)
pa.click(x=2943, y=742)  # Clica em uma posição específica na tela para ativar o campo de login
pa.write("marcos.sales")  # Digita o nome de usuário "marcos.sales"

time.sleep(1)  # Espera 1 segundo para garantir que o campo de senha seja acessado corretamente
pa.click(x=2868, y=805)  # Clica em uma posição específica para selecionar o campo da senha
pa.write("--------")  # Digita a senha (substitua os traços por uma senha real, se necessário)

time.sleep(1)  # Espera 1 segundo para garantir que o próximo clique seja executado corretamente
pa.click(x=2947, y=903)  # Clica em uma posição específica (provavelmente para enviar o formulário de login)
