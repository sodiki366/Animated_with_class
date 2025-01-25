import tkinter as tk


class AnimatedCircle(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Создаем круг
        self.circle = self.create_oval(10, 10, 50, 50, fill="blue")

        # Переменная для хранения текущего положения круга
        self.x = 0
        self.y = 25

        # Запускаем анимацию
        self.animate()

    def animate(self):
        # Двигаем круг вправо
        self.move(self.circle, 1, 0)

        # Обновляем положение круга
        self.x += 1

        # Если круг достиг края экрана, возвращаемся к началу
        if self.x > self.winfo_width():
            self.x = 0

        # Повторяем анимацию через каждые 20 миллисекунд
        self.after(20, self.animate)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Устанавливаем размер окна
        self.geometry("400x200")

        # Создаем объект класса AnimatedCircle
        self.animated_circle = AnimatedCircle(self, width=400, height=200)
        self.animated_circle.pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()