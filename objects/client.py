
class Clien:
    def __init__(self, name, age, phone, cpf, whatsapp=False):
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__cpf = cpf
        self.__whatsapp = whatsapp

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return

    @property
    def phone(self):
        return self.__phone

    @property
    def cpf(self):
        return self.__cpf

    @property
    def whatsapp(self):
        return self.__whatsapp

