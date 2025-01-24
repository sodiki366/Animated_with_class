import random
import time
import tkinter as tk


class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Настройки окна
        self.master.title('Catch the Falling Objects')
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, background='lightblue')
        self.canvas.pack()

        # Создание корзины
        self.basket_x = self.width / 2
        self.basket_y = self.height - 40
        self.basket_width = 100
        self.basket_height = 30
        self.basket = Basket(self.canvas, self.basket_x, self.basket_y, self.basket_width, self.basket_height)

        # Список предметов
        self.items = []

        # Счетчик пойманных предметов
        self.score = 0
        self.score_label = tk.Label(self, text=f'Score: {self.score}', font=('Arial', 16))
        self.score_label.place(x=10, y=10)

        # Начало игры
        self.start_game()

    def start_game(self):
        """Запуск игры."""
        self.spawn_item()
        self.update_basket_position()
        self.master.after(3000, self.check_collision)

    def spawn_item(self):
        """Создание нового предмета."""
        x = random.randint(0, self.width - 50)
        item = Item(self.canvas, x, 0, 'red')
        self.items.append(item)
        self.master.after(1500, self.spawn_item)

    def update_basket_position(self):
        """Обновление позиции корзины."""
        self.basket_x = self.canvas.winfo_pointerx() - self.basket_width // 2
        if self.basket_x < 0:
            self.basket_x = 0
        elif self.basket_x > self.width - self.basket_width:
            self.basket_x = self.width - self.basket_width
        self.basket.move_to(self.basket_x, self.basket_y)
        self.master.after(15, self.update_basket_position)

    def check_collision(self):
        """Проверка столкновений предметов с корзиной."""
        for item in self.items[:]:
            if self.basket.collides_with(item):
                self.score += 1
                self.score_label.config(text=f'Score: {self.score}')
                self.items.remove(item)
                item.delete()
        self.master.after(100, self.check_collision)


class Basket:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x, y, x + width, y + height, fill='green')

    def move_to(self, new_x, new_y):
        self.canvas.coords(self.id, new_x, new_y, new_x + self.basket_width, new_y + self.basket_height)

    def collides_with(self, item):
        item_coords = item.get_coords()
        basket_coords = self.canvas.coords(self.id)
        return (
            item_coords[0] >= basket_coords[0]
            and item_coords[0] <= basket_coords[2]
            and item_coords[1] >= basket_coords[1]
            and item_coords[1] <= basket_coords[3]
        )


class Item:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x, y, x + 25, y + 25, fill=color)
        self.x_speed = 0
        self.y_speed = 2
        self.active = True
        self.move()

    def get_coords(self):
        return self.canvas.coords(self.id)

    def delete(self):
        self.canvas.delete(self.id)
        self.active = False

    def move(self):
        coords = self.canvas.coords(self.id)
        if coords[1] >= self.canvas.winfo_reqheight():
            self.delete()
        else:
            self.canvas.move(self.id, self.x_speed, self.y_speed)
            self.master.after(10, self.move)


if __name__ == '__main__':
    root = tk.Tk()
    game = Game(master=root)
    root.mainloop()