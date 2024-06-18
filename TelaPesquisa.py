from BaseInterface import TelaBase
from customtkinter import *
from tkinter import messagebox
from datetime import datetime
import TelaPrevisao


class TelaPesquisa(TelaBase):
    def __init__(self):
        super().__init__('Tela de Pesquisa')
        self.label()
        self.entradas()
        self.botoes()

        self.janela.mainloop()

    def label(self):
        self.cidade = CTkLabel(self.frame, text='Cidade:', font=self.fonte)
        self.cidade.place(x=100, y=50)

        self.data_inicio = CTkLabel(self.frame, text='Data de início:', font=self.fonte)
        self.data_inicio.place(x=100, y=150)

        self.data_fim = CTkLabel(self.frame, text='Data do fim:', font=self.fonte)
        self.data_fim.place(x=100, y=250)

    def entradas(self):
        self.entrada_cidade = CTkEntry(self.frame, font=self.fonte, width=350, placeholder_text='Digite uma cidade...')
        self.entrada_cidade.place(x=100, y=85)

        self.entrada_data_inicio = CTkEntry(self.frame, font=self.fonte, width=250, placeholder_text='DD/MM/YYYY')
        self.entrada_data_inicio.place(x=100, y=185)

        self.entrada_data_fim = CTkEntry(self.frame, font=self.fonte, width=250, placeholder_text='DD/MM/YYYY')
        self.entrada_data_fim.place(x=100, y=285)

    def botoes(self):
        self.continuar = CTkButton(self.frame, width=200, text='Continuar', font=self.fonte, command=self.continuar)
        self.continuar.place(relx=0.5, rely=0.8, anchor=CENTER)

    def validar_data(self, data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def continuar(self):
        cidade = self.entrada_cidade.get()
        data_inicio = self.entrada_data_inicio.get()
        data_fim = self.entrada_data_fim.get()

        if not cidade:
            messagebox.showerror("Campo não preenchido", "Preencha o campo da cidade.")
            return

        if not self.validar_data(data_inicio):
            messagebox.showerror("Data de início inválida",
                                 "Digite uma data de início válida no formato DD/MM/YYYY.")
            return

        if not self.validar_data(data_fim):
            messagebox.showerror("Data do fim inválida",
                                 "Digite uma data do fim válida no formato DD/MM/YYYY.")
            return

        self.janela.destroy()
        TelaPrevisao.TelaPrevisao(cidade, data_inicio, data_fim)


if __name__ == "__main__":
    tela_pesquisa = TelaPesquisa()
