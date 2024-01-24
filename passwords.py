import random
from customtkinter import *
from PIL import Image

def senhas():

#Parametrôs para senha a ser gerada:
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@#$%^&*.!"
# Obtendo o tamanho da senha a partir do widget CTkEntry
    tamanho = int(tamanho_senha.get())

# Junção de todos os parâmetros para ser gerada a senha
    password_chars = list(lower_letters + upper_letters + numbers + symbols)

    if 8 <= tamanho <= 15:
        # Sorteio entre as strings com os parâmetros, tamanho que o usuário escolher
        password = random.choices(password_chars, k=tamanho)
        senha_gerada.set(''.join(password))
        condicao.set("")  # Limpando a mensagem de condição
    else:
        # Exibindo mensagem quando o tamanho não está na faixa desejada
        condicao.set("A senha deve ter no mínimo 8 caracteres e \n no máximo 15.")
        senha_gerada.set("")  # Limpando a senha gerada

def copiar_texto():
    texto = senha_gerada.get()
    interface.clipboard_clear()
    interface.clipboard_append(texto)
    interface.update()

#Começo da interface no CustomTkinter
interface = CTk()
interface.title("Gerador de senhas")
interface.geometry("300x250")
interface.iconbitmap("images/icon_progam.ico")
interface.resizable(False, False)

set_appearance_mode('system')

interface.grid_rowconfigure(0, weight=1)
interface.grid_columnconfigure(0, weight=1)
interface.grid_rowconfigure(3, weight=1)

#Tamanho para o usuario escolher:
tamanho_senha = CTkEntry(master=interface, placeholder_text='Digite o tamanho da senha',
                          width=200, text_color="white")
tamanho_senha.place(x=53, y=48)

#Botão
imagem = Image.open("images/password.image.png") #Importando imagem do botão
botao = CTkButton(master=interface, width=100, height=30, text='Gerar senha', command=senhas, corner_radius=32, fg_color="#0000FF",
                  hover_color="#6A0888", border_width=2, image=CTkImage(dark_image=imagem, light_image=imagem))
botao.place(x=86, y=90)

# Variável para armazenar a senha gerada
senha_gerada = StringVar()
condicao = StringVar()

# Label para exibir a senha gerada
label_senha = CTkLabel(master=interface, textvariable=senha_gerada, width=100)
label_senha.place(x=100, y=130)

# Label para exibir a mensagem de condição
label_condicao = CTkLabel(master=interface, textvariable=condicao, width=50, text_color='red')
label_condicao.place(x=28, y=5)

#Botão para copiar texto:
imagem_copiar = Image.open("images/icon_copiar.png")
botao_copiar = CTkButton(master=interface, command=copiar_texto, text='', width=10, border_width=2, fg_color="#0000FF", hover_color="#6A0888", image=CTkImage(dark_image=imagem_copiar, light_image=imagem_copiar))
botao_copiar.place(x=130, y=160)

interface.mainloop()

#ARRUMAR A FONTE!!!!