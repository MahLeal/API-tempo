import requests
from tkinter import *

API_KEY = "eeb7e4db2db49b9e831d2aa28caf1135"
cidade = "rio verde"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f"{temperatura}ºC")

# definicoes de tela

tela = Tk()
tela.geometry("500x500")
tela.config(background='#363636', )
tela.title('API Tempo')

texto_tempo = Label(text="Clima Rio Verde", fg='#FFFFFF', bg='#363636', font='arial')
texto_tempo.place(x=100, y=100)
texto_tempo = Label(tela, text=f"{descricao, temperatura} °C", fg='#FFFFFF', bg='#363636', font='arial')
texto_tempo.place(x=100, y=200)

tela.mainloop()

import requests
from tkinter import *

def exibir():
    cidade = entrada.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(descricao, f"{temperatura}ºC")

    texto_tempo = Label(tela, text=f"{descricao, temperatura} °C", fg='#FFFFFF', bg='#363636', font='arial')
    texto_tempo.place(x=100, y=100)


API_KEY = "eeb7e4db2db49b9e831d2aa28caf1135"

link = f"http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API_KEY}"

# definicoes de tela

tela = Tk()
tela.geometry("500x500")
tela.config(background='#363636', )
tela.title('API Tempo')

texto_tempo = Label(text="Escreva o nome da cidade:", fg='#FFFFFF', bg='#363636', font='arial')
texto_tempo.place(x=100, y=100)
entrada = Entry(bg='#FFFF00', border=0, fg='white', font='arial')
entrada.place(x=100, y=300)
botao = Button(text='Procurar', bg='#363636', border=2, fg='#FFFF00', activebackground='#363636', width=20, height=3, command= exibir)
botao.place(x=100, y=400)

tela.mainloop()
