from customtkinter import *


class TelaBase:
    def __init__(self, title):
        self.janela = CTk()
        self.tema()
        self.tela(title)

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self, title):
        self.janela.title(title)
        self.janela.geometry('600x500')
        self.janela.resizable(False, False)
        self.frame = CTkFrame(self.janela, width=550, height=500)
        self.frame.pack()
        self.fonte = ('Nunito', 22)


