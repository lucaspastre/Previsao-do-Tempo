from customtkinter import *
import requests
from datetime import datetime
import TelaPesquisa


class TelaPrevisao:
    def __init__(self, cidade, data_inicio, data_fim):
        self.cidade = cidade
        self.data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        self.data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()

        self.api()
        self.arquivo()

        self.janela = CTk()
        self.tema()
        self.tela()

        self.mostrar_previsao()
        self.scrollbar()

        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title(f"Previsão do Tempo em {self.nome}")
        self.janela.geometry("630x500")
        self.janela.resizable(False, False)

    def api(self):
        self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.FORECAST_BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
        self.API_KEY = "202923fa741eb6ffa5d48b6ba65d37d3"

        self.url = self.BASE_URL + "q=" + self.cidade + "&appid=" + self.API_KEY + "&lang=pt_br"
        self.response = requests.get(self.url).json()

        self.nome = self.response['name']
        self.condicao_tempo = self.response['weather'][0]['main']

        self.url2 = self.FORECAST_BASE_URL + "q=" + self.cidade + "&appid=" + self.API_KEY + "&lang=pt_br"
        self.response2 = requests.get(self.url2).json()

        self.previsoes = self.response2['list']
        self.condicoes = []

        self.dicionario = {
            'Thunderstorm': 'Trovoada',
            'Drizzle': 'Chuvisco',
            'Snow': 'Neve',
            'Mist': 'Nevoeiro',
            'Fog': 'Nevoeiro',
            'Haze': 'Neblina',
            'Rain': 'Chuva',
            'Clear': 'Céu limpo',
            'Clouds': 'Nublado',
        }

    def arquivo(self):
        arq = open('Lista_Previsoes.txt', 'a', encoding='utf-8')
        for previsao in self.previsoes:
            date_time = datetime.strptime(previsao['dt_txt'], '%Y-%m-%d %H:%M:%S')
            data_previsao = date_time.date()
            hora_previsao = date_time.hour

            if self.data_inicio <= data_previsao <= self.data_fim and hora_previsao in [9, 15, 21]:
                periodo = self.periodo_do_dia(hora_previsao)

                tempo = previsao['weather'][0]['main']
                condicao_tempo = self.dicionario.get(tempo, tempo)

                temperatura = previsao['main']['temp']
                umidade = previsao['main']['humidity']
                sensacao_termica = previsao['main']['feels_like']
                velocidade_vento = previsao['wind']['speed']

                arq.write(f'Cidade: {self.nome}\n')
                arq.write(f'Data: {data_previsao.strftime("%d/%m/%Y")}\n')
                arq.write(f'Período: {periodo}\n')
                arq.write(f'Condição do Tempo: {condicao_tempo}\n')
                arq.write(f'Temperatura: {temperatura - 273.15:.2f}°C\n')
                arq.write(f'Umidade: {umidade}%\n')
                arq.write(f'Sensação Térmica: {sensacao_termica - 273.15:.2f}°C\n')
                arq.write(f'Velocidade do Vento: {velocidade_vento} m/s\n')
                arq.write("\n")

        arq.close()

    def periodo_do_dia(self, hora):
        if 6 <= hora < 12:
            return "Manhã"
        elif 12 <= hora < 18:
            return "Tarde"
        else:
            return "Noite"

    def mostrar_previsao(self):
        self.canvas = CTkCanvas(self.janela, width=500)
        self.canvas.pack(side='left', fill='both', expand=True)

        self.frame_content = CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_content, anchor='nw')

        self.frame_content.grid_columnconfigure(0, weight=1)
        row_index = 0

        self.botao_voltar()

        for previsao in self.previsoes:
            date_time = datetime.strptime(previsao['dt_txt'], '%Y-%m-%d %H:%M:%S')
            data_previsao = date_time.date()
            hora_previsao = date_time.hour

            if self.data_inicio <= data_previsao <= self.data_fim and hora_previsao in [9, 15, 21]:
                periodo = self.periodo_do_dia(hora_previsao)

                tempo = previsao['weather'][0]['main']
                condicao_tempo = self.dicionario.get(tempo, tempo)

                temperatura = previsao['main']['temp']
                umidade = previsao['main']['humidity']
                sensacao_termica = previsao['main']['feels_like']
                velocidade_vento = previsao['wind']['speed']

                frame = CTkFrame(self.frame_content, width=600)
                frame.grid(row=row_index // 3, column=row_index % 3, padx=10, pady=10, sticky='nsew')

                label_data = CTkLabel(frame, text=f"Data: {data_previsao.strftime('%d/%m/%Y')}", font=('Nunito', 14))
                label_data.pack(anchor='w')

                label_periodo = CTkLabel(frame, text=f"Período: {periodo}", font=('Nunito', 14))
                label_periodo.pack(anchor='w')

                label_tempo = CTkLabel(frame, text=f"Condição do Tempo: {condicao_tempo}", font=('Nunito', 12))
                label_tempo.pack(anchor='w')

                label_temperatura = CTkLabel(frame, text=f"Temperatura: {temperatura - 273.15:.1f}°C",
                                             font=('Nunito', 12))
                label_temperatura.pack(anchor='w')

                label_umidade = CTkLabel(frame, text=f"Umidade: {umidade}%", font=('Nunito', 12))
                label_umidade.pack(anchor='w')

                label_sensacao = CTkLabel(frame, text=f"Sensação Térmica: {sensacao_termica - 273.15:.1f}°C",
                                          font=('Nunito', 12))
                label_sensacao.pack(anchor='w')

                label_vento = CTkLabel(frame, text=f"Velocidade do Vento: {velocidade_vento} m/s", font=('Nunito', 12))
                label_vento.pack(anchor='w')

                row_index += 1

        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def scrollbar(self):
        scrollbar = CTkScrollbar(self.janela, command=self.canvas.yview)
        scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=scrollbar.set)

    def botao_voltar(self):
        frame = CTkFrame(self.frame_content, width=600)
        frame.grid(row=(len(self.previsoes) // 3) + 1, column=1, padx=10, pady=10, sticky='nsew')
        botao = CTkButton(frame, text="Voltar", command=self.voltar)
        botao.pack(anchor='center')

    def voltar(self):
        self.janela.destroy()
        TelaPesquisa.TelaPesquisa()
