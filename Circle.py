import tkinter as tk

class AnimatedCircle(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        #Создаем круг
        self.circle = self.create_oval(0, 0, 100, 100,
                                       fill='blue')

        #Переменная для зранения текущего положения круга
        self.x = 50
        self.y = 50

    def move(self):
        self.move(self.circle, 10, 0)
        self.after(100, self.move)
        #Изменяем положение круга

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Настраиваем окно приложения
        self.title("Animated Circle")
        self.geometry("800x600")

        #Создаем экземпляр класс AnimatedCircle
        self.animated_circle = AnimatedCircle(self,
        width=800, height=600)
        self.animated_circle.pack()

        #Запускаем анимацию
        self.animated_circle.move()

if __name__ == "__main__":
    app = App()
    app.mainloop()