from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Importando Pillow
from PIL import ImageTk, Image

#Importando strings
import string
import random


# cores -------------------------
cor1 = '#444466' # Preta
cor2 = '#feffff' # Branca
cor3 = '#f05a43' # Red

janela = Tk()
janela.title('')
janela.geometry('295x360')
janela.configure(bg=cor2)

# Repartindo a tela ----------------------------------
frame_cima = Frame(janela, width=295, height=50, bg=cor2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor2, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Trabalhando no Frame de cima
img = Image.open('cade.png')
img = img.resize((50,30), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor2)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text='GERADOR DE SENHA', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=cor2, fg=cor1)
app_nome.place(x=40, y=5)

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor3, fg=cor1)
app_linha.place(x=0, y=42)

# -------------- FUNÇÃO 
def criar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()/@!#*_'

    global combinar
    # ---- condição para maiuscula
    if estado1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass

    # ------- condição minuscula
    if estado2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

    # ------------ condição numeros
    if estado3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # ------------ condição simbolos
    if estado4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass
    
    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo('sucesso', 'A senha foi criada com sucesso')
    botao_copiar = Button(frame_baixo,command=copiar_senha, text='Copiar',width=6, height=2, padx=0, relief='raised', overrelief='solid', anchor='center',font='Ivy 10 bold', bg=cor2, fg=cor1)
    botao_copiar.grid(row=0, column=1, sticky=NSEW, padx=5, pady=10, columnspan=5)

# Trabalhando no Frame baixo
app_senha = Label(frame_baixo, text='- - -', width=16, height=2, padx=0, relief='solid', anchor='center',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='Numero Total de Caracteres na Senha', height=1, padx=0, relief='flat', anchor='nw',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

# Criando SpinBox - contando a partir de 8 caracteres
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()/@!#*_'

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor2, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

# Criando CheckButton

# Letras Maiúscula
estado1 = StringVar()
estado1.set(False)
check_1 = Checkbutton(frame_caracteres,width=1, var=estado1, onvalue=alfa_maior, offvalue='off', relief='flat', bg=cor2)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='ABC LETRAS MAIUSCULAS', height=1, padx=0, relief='flat', anchor='nw',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

# Letras minúscula
estado2 = StringVar()
estado2.set(False)
check_2 = Checkbutton(frame_caracteres,width=1, var=estado2, onvalue=alfa_menor, offvalue='off', relief='flat', bg=cor2)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='abc letras minusculas', height=1, padx=0, relief='flat', anchor='nw',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

# Numeros
estado3 = StringVar()
estado3.set(False)
check_3 = Checkbutton(frame_caracteres,width=1, var=estado3, onvalue=numeros, offvalue='off', relief='flat', bg=cor2)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='123 Numeros', height=1, padx=0, relief='flat', anchor='nw',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)

# Simbolos
estado4 = StringVar()
estado4.set(False)
check_4 = Checkbutton(frame_caracteres,width=1, var=estado4, onvalue=simbolos, offvalue='off', relief='flat', bg=cor2)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='Simbolos', height=1, padx=0, relief='flat', anchor='nw',font='Ivy 10 bold', bg=cor2, fg=cor1)
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

# ------------------------ BOTÃO -------

botao_senha = Button(frame_caracteres, command=criar_senha, text='Gerar Senha',width=26, height=1, padx=0, relief='flat', overrelief='solid', anchor='center',font='Ivy 10 bold', bg=cor3, fg=cor2)
botao_senha.grid(row=5, column=1, sticky=NSEW, padx=0, pady=10, columnspan=5)


janela.mainloop()