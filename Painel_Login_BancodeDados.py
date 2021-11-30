from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

# criando janela --------------------------
janela = Tk()
janela.title('Painel de acesso')
janela.geometry('600x300')
janela.configure(bg='white')
janela.resizable(width=False, height=False)
janela.iconbitmap(default='icons/Logoicon.ico')

# Carregando imagens ------------------------
logo = PhotoImage(file='icons/logo.png')

# Widgets ------------------------------------
leftFrame = Frame(janela, width=200, height=300, bg='#0000FF', relief='raise')
leftFrame.pack(side=LEFT)

rightFrame = Frame(janela, width=395, height=300, bg='#0000FF', relief='raise')
rightFrame.pack(side=RIGHT)

logo_label = Label(leftFrame, image=logo, bg='#0000FF')
logo_label.place(x=50, y=100)

# Criando Entry ---------------------
user_label = Label(rightFrame, text='Username: ', font=('Century Gothic', 20), bg='#0000FF', fg='white')
user_label.place(x=5, y=100)

user_entry = ttk.Entry(rightFrame, width=30)
user_entry.place(x=150, y=112)

pass_label = Label(rightFrame, text='Password: ', font= ('Century Gothic', 20), bg= '#0000FF', fg='White')
pass_label.place(x=5, y=150)

pass_entry = ttk.Entry(rightFrame, width=30, show='*')
pass_entry.place(x=150, y= 162)

def Login():
    user = user_entry.get()
    senha = pass_entry.get()
    database.cursor.execute("SELECT * FROM users WHERE (user =%s and password =%s )", (user, senha))
    print('Selecionou')
    verifylogin = database.cursor.fetchone()
    try:
        if (user in verifylogin and senha in verifylogin):
            messagebox.showinfo(title='Login Info', message='Acesso Confirmado. Bem Vindo!')
    except:
        messagebox.showinfo(title='Login Info', message='Acesso Negado. Faça Seu Cadastro!')

# criando botões --------------------
botao_login = ttk.Button(rightFrame, text='Login', width=20, command=Login)
botao_login.place(x=170, y= 210)

# Função Cadastro
def register():
    # removendo widgts de login
    botao_login.place(x=5000)
    botao_register.place(x=5000)
    # inserindo widgets de cadastro
    nome_label = Label(rightFrame, text='Name: ', font=('Century Gothic', 20), bg='#0000FF', fg='white')
    nome_label.place(x=5, y=5)

    nome_entry = ttk.Entry(rightFrame, width=30)
    nome_entry.place(x=150, y=18)

    email_label = Label(rightFrame, text='Email: ', font=('Century Gothic', 20), bg='#0000FF', fg='white')
    email_label.place(x=5, y= 50 )

    email_entry = ttk.Entry(rightFrame, width=30)
    email_entry.place(x=150, y=62)

    def RegisterToDataBase():
        name = nome_entry.get()
        email = email_entry.get()
        user = user_entry.get()
        senha = pass_entry.get()

        if (name == '' and email == '' and user == '' and senha ==''):
            messagebox.showerror(title='Register Error', message='Preencha todos os campos.')

        else:
            database.cursor.execute("INSERT INTO Users(name, email, user, password) VALUES (%s, %s, %s, %s)", (name, email, user, senha))
            database.banco.commit()
            messagebox.showinfo(title='Register info', message='Conta Criada Com Sucesso')

    register = ttk.Button(rightFrame, text='Register', width=10, command=RegisterToDataBase)
    register.place(x=150, y=225)

# Função voltar ao Login
    def BackToLogin():
        # Removendo widgets de cadastro
        nome_label.place(x=5000)
        nome_entry.place(x=5000)
        email_label.place(x=5000)
        email_entry.place(x=5000)
        register.place(x=5000)
        back.place(x=5000)
        # Trazendo de volta os widgets de Login
        botao_login.place(x=150)
        botao_register.place(x=150)

    back = ttk.Button(rightFrame, text='Back', width=10, command=BackToLogin)
    back.place(x=240, y=225)

botao_register = ttk.Button(rightFrame, text='Register', width=20, command=register)
botao_register.place(x=170, y=240)

janela.mainloop()