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
