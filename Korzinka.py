import random
import time
import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        #Настройки окна
        self.master.title('Catch the Falling Objects')
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(self, width=self.width,
        height=self.height, background='lightblue')
        self.canvas.pack()

        #Создание корзины
        self.backet_x = self.width / 2
        self.backet_y = self.height - 40
        self.backet_width = 100
        self.backet_height = 30
        self.backet = Backet(self.canvas, self.backet_x,
        self.backet_y, self.backet_width, self.backet_height)

        #Список предметов
        self.items = []

        #Счетчик пойманных предметов
        self.score = 0