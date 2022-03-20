from tkinter import *
from tkinter.ttk import Combobox


class FrameMain:
    def __init__(self):
        self.__logar = None
        self.__password = None
        self.__occupation = None
        self.__titulo = None
        self.__frame_login = None
        self.__frame_background_color = None
        self.__root = Tk()
        self.__root.title('Login de Sesão')
        self.__root.geometry("1000x800")
        self.frame_background()
        self.frame_login()
        self.__root.mainloop()

    def frame_background(self):
        self.__frame_background_color = Frame(self.__root, bg='#0081CF')
        self.__frame_background_color.place(relheight=1, relwidth=1, rely=0, relx=0)

    def frame_login(self):
        self.__frame_login = Frame(self.__root, bg='#008F7A', height=400, width=500)
        self.__frame_login.place(relheight=0.7, relwidth=0.5, rely=0.10, relx=0.25)
        self.__titulo = Label(self.__frame_login, text='Lojas Vendas ABC')
        self.__titulo.place(relheight=0.1, relwidth=0.5, rely=0.01, relx=0.25)
        self.__occupation = Combobox(self.__frame_login, values=["Vendendor",
                                                                 "Gerente De Vendas",
                                                                 "Financeiro",
                                                                 "Administrador"])
        self.__occupation.place(relheight=0.1, relwidth=0.5, rely=0.20, relx=0.25)
        self.__password = Entry(self.__frame_login)
        self.__password.place(relheight=0.1, relwidth=0.5, rely=0.40, relx=0.25)
        self.__logar = Button(self.__frame_login, text='Logar agora')
        self.__logar.place(relheight=0.1, relwidth=0.5, rely=0.60, relx=0.25)


if __name__ == '__main__':
    FrameMain()
