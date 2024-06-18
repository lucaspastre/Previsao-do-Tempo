from BaseInterface import TelaBase
from customtkinter import *
from tkinter import messagebox
import TelaPesquisa


class TelaInicial(TelaBase):
    def __init__(self):
        super().__init__('Tela Inicial')
        self.label()
        self.entradas()
        self.botoes()

        self.janela.mainloop()

    def label(self):
        self.titulo = CTkLabel(self.frame, text='APLICATIVO DE PREVISÃO DO TEMPO', font=self.fonte)
        self.titulo.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.username_label = CTkLabel(self.frame, text="Username:", font=self.fonte)
        self.username_label.place(x=130, y=145)

        self.senha_label = CTkLabel(self.frame, text="Senha:", font=self.fonte, anchor=W)
        self.senha_label.place(x=165, y=255, anchor=CENTER)

    def entradas(self):
        self.entrada_username = CTkEntry(self.frame, font=self.fonte, width=300, placeholder_text='Digite seu usuário...')
        self.entrada_username.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.entrada_senha = CTkEntry(self.frame, font=self.fonte, show='*', width=300, placeholder_text='Digite sua senha...')
        self.entrada_senha.place(relx=0.5, rely=0.6, anchor=CENTER)

    def botoes(self):
        self.login = CTkButton(self.frame, width=200, text='Login', font=self.fonte, command=self.continuar_tela_pesquisa)
        self.login.place(relx=0.5, rely=0.8, anchor=CENTER)

    def continuar_tela_pesquisa(self):
        self.username_digitado = self.entrada_username.get()
        self.senha_digitada = self.entrada_senha.get()
        if self.username_digitado == 'lucasps' and self.senha_digitada == '12345':
            self.janela.destroy()
            TelaPesquisa.TelaPesquisa()
            return True
        else:
            messagebox.showerror(title="Dados inválidos", message="Preencha corretamente para prosseguir")


if __name__ == "__main__":
    app = TelaInicial()
