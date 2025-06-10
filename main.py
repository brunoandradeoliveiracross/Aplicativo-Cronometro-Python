# Importar Bibliotecas
from tkinter import *
import tkinter

# Tabela de cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

#Definindo variaveis globais
global tempo
global rodar
global contador
global limitador

limitador = 59


#Criação de funções
tempo = "00:00:00"
rodar = False
contador = 0 # variavel que controla a contagem regressiva

#Função Iniciar
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        # antes do cronometro começar
        if contador <= -1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

        #Rodando o cronometro
        else:
            label_tempo['font'] = ('Times', 50, 'bold')

            temporario = str(tempo)
            h,m,s = map(int,temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s>=limitador):
                contador = 0
                m+=1
            
            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #Atualizando os valores atuais
            temporario = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_tempo['text'] = temporario
            tempo = temporario
        
        #1000 = 1 segundo
        label_tempo.after(1000,iniciar)
        contador +=1    

#Função para dar inicio
def start():
  global rodar
  rodar = True
  iniciar()

#Função para dar pause
def pausar():
  global rodar
  rodar = False
  
#Função para dar reinicio
def reiniciar():
  global contador
  global tempo

  # reiniciando o tempo e o contador
  contador = 0
  tempo = "00:00:00"
  label_tempo['text'] = tempo


#Front End
#Criação da janela
janela = Tk()
janela.title("")
janela.geometry("300x180")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE) # Bloqueia a altura e largura da janela fixa em geometry

#Criando Labels
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=50)

#Criando Botões
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela,command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief='raised', overrelief='ridge' )
botao_pausar.place(x=105, y=130)

botao_reiniciar = Button(janela,command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=("Ivy 8 bold"), relief='raised', overrelief='ridge' )
botao_reiniciar.place(x=190, y=130)




janela.mainloop()