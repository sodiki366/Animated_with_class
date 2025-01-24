import tkinter as tk


class AnimatedCanvas(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Создаем круг
        self.circle = self.create_oval(10, 10, 50, 50, fill="blue")

        # Запускаем анимацию
        self.animate()

    def animate(self):
        # Перемещаем круг на 1 пиксель вправо и вниз
        self.move(self.circle, 1, 1)

        # Повторяем анимацию через 20 миллисекунд
        self.after(20, self.animate)


# Создаем главное окно приложения
root = tk.Tk()
root.title("Animation Example")

# Создаем экземпляр нашего класса AnimatedCanvas
canvas = AnimatedCanvas(root, width=500, height=300, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Запускаем главный цикл приложения
root.mainloop()