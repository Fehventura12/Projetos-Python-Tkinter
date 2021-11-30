from tkinter import *
import tkinter 

# cores
cor1 = '#0000FF' # Azul
cor2 = '#000000' # Preto
cor3 = '#FFFAFA' # Gelo

#janela
janela = Tk()
janela.title('Cronômetro')
janela.geometry('300x200')
janela.configure(bg=cor2)
janela.resizable(width=FALSE, height=FALSE)

# Definição de variaveis
global tempo
global rodar
global contador
global limite

limite = 59
tempo = '00:00:00'
rodar = False
contador = -5

#função para iniciar
def iniciar():
    global contador
    global tempo
    global limite

    if rodar:
        if contador <= -1:
            inicio = 'Começando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

#Rodando o cronometro
        else:
            label_tempo['font'] = 'Times 50 bold'
            temporario = str(tempo)
            h,m,s = map(int,temporario.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s >= limite):
                contador = 0
                m += 1

            s = str(0) + str(s)
            m = str(0) + str(m)
            h = str(0) + str(h)

# Atualizando valores
            temporario = str(h[-2:]) + ':' + str(m[-2:])+ ':' + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario


        label_tempo.after(1000,iniciar)
        contador +=1

#função para iniciar
def start():
    global rodar 
    rodar = True
    iniciar()

#Função pausar
def pausar():
    global rodar
    rodar = False

# Função reiniciar
def reiniciar():
    global contador
    global tempo 
    contador = 0
    tempo = '00:00:00'
    label_tempo['text'] = tempo


# Criando labels
label_app = Label(janela, text='Cronômetro', fon=('Arial 10'), bg=cor2, fg=cor3)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, fon=('Times 50 bold'), bg=cor2, fg=cor1)
label_tempo.place(x=20, y=30)

# Criando os Botões
Bot_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor3, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Bot_iniciar.place(x=20, y=130)

Bot_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor3, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Bot_pausar.place(x=110, y=130)

Bot_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor3, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
Bot_reiniciar.place(x=200, y=130)

start()



janela.mainloop()
