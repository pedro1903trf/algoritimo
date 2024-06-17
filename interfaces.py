# o gerador de senha ele e composto por o tkinter que foi importantissimo para que o gerador de senha com interface funcionasse perfeitamente
# pra comecar vou mostrar um pouco dos codigos que estou utilizando e como que cada um deles fazem esse sistsema funcionar
# a exemplo desses codigos temos o 'import' 'string' e 'random' o random e um codigo muito importante poruqe foi
#a prtir dele
# que o meu gerador de senha e capaz de gerar senha aleatoria de quantas caracteristicas forem necessarias
# usei o self para que eu possa ter acesso a variaveis de varias classes
# utilizei o def para definir uma funçao, utilizei o init tbm para iniciar uma clase
#usei tambem o tkinter para gerar a interface grafica

import tkinter as tk
import string
import random

import tkinter as tk

class Window:
    MAX_CHARS = 22
    MIN_CHARS = 8
    CHARS_OPTIONS = ["Alphanumeric", "Numeric", "Alpha"]
    GRID_PADY = (18, 18)

    def __init__(self):
        self.initUI()

    def initUI(self):
        self.master = tk.Tk()
        self.master.title("Password Generator")
        self.master.geometry("580x250")

        self.ptype = tk.StringVar(self.master, value=self.CHARS_OPTIONS[0])
        self.n_chars = tk.IntVar(self.master, value=self.MIN_CHARS)

        self.label_chars = tk.Label(self.master, text='Chars that will compose the Password: ')
        self.option_menu_chars = tk.OptionMenu(self.master, self.ptype, *self.CHARS_OPTIONS)

        self.frame_n_chars = tk.Frame(self.master)
        self.label_num_chars = tk.Label(self.master, text='Password Length:')
        self.option_menu_n_chars = tk.OptionMenu(self.master, self.n_chars, *range(self.MIN_CHARS, self.MAX_CHARS + 1))

        self.text_password_out = tk.Text(self.master, border=2, height=2, width=30)

        self.frame_buttons = tk.Frame()
        self.button_generate = tk.Button(self.frame_buttons, text='Generate', width=8, command=self.set_password)
        self.button_close = tk.Button(self.frame_buttons, text='Close', command=self.master.quit, width=8)

        self.label_chars.grid(row=0, column=0, pady=self.GRID_PADY)
        self.option_menu_chars.grid(row=0, column=1)

        self.label_num_chars.grid(row=1, column=0, pady=self.GRID_PADY)
        self.option_menu_n_chars.grid(row=1, column=1)

        self.text_password_out.grid(row=2, column=0, columnspan=2, pady=self.GRID_PADY)

        self.button_generate.pack(side=tk.LEFT)
        self.button_close.pack(side=tk.LEFT, pady=self.GRID_PADY)

        self.frame_buttons.grid(row=3, column=1, columnspan=2)

        self.master.mainloop()

    def set_password(self):
        chars = ''
        ptype = self.ptype.get().lower()
        if ptype == 'numeric':
            chars = string.digits
        elif ptype == 'alpha':
            chars = string.ascii_letters
        else:
            chars = string.digits + string.ascii_letters
        password = ''.join(random.choices(chars, k=self.n_chars.get()))
        self.text_password_out.delete('1.0', tk.END)
        self.text_password_out.insert('1.0', password)

if __name__ == "__main__":
    window = Window()