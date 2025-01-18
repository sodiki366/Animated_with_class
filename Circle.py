import tkinter as tk

class AnimatedCircle(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #Создаем круг
        self.circle = self.create_oval(0, 0, 100, 100,fill= 'blue')

        #Переменная для хранения текущего положения круга
        self.x = 50
        self.y = 50

    def move(self):
        self.move(self.circle, 10, 0)
        self.after(100, self.move)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Настраиваем окно приложения
        self.title("Animated Circle")
        self.geometry("800x600")

        #Создаем экземпляр класса AnimatedCircle
        self.animated_circle = AnimatedCircle(self,width=800,height=600)
        self.animated_circle.pack()

        #Запускаем анимацию
        self.animated_circle.pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()