import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("400x400")

        self.canvas = tk.Canvas(root, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(200, 200)]
        self.apple = self.create_apple()
        self.direction = "Right"
        self.score = 0

        self.draw_snake()
        self.draw_apple()

        self.root.bind("<KeyPress>", self.change_direction)

        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tag="snake")

    def draw_apple(self):
        x, y = self.apple
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", tag="apple")

    def create_apple(self):
        x = random.randrange(0, 400, 10)
        y = random.randrange(0, 400, 10)
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= 10
        elif self.direction == "Down":
            head_y += 10
        elif self.direction == "Left":
            head_x -= 10
        elif self.direction == "Right":
            head_x += 10

        if (head_x, head_y) in self.snake or not (0 <= head_x < 400 and 0 <= head_y < 400):
            self.game_over()
            return

        self.snake.insert(0, (head_x, head_y))

        if (head_x, head_y) == self.apple:
            self.score += 1
            self.canvas.delete("apple")
            self.apple = self.create_apple()
            self.draw_apple()
        else:
            self.snake.pop()

        self.draw_snake()

        self.root.after(100, self.move_snake)

    def game_over(self):
        self.canvas.create_text(200, 200, text=f"Game Over! Score: {self.score}", fill="white", font=("Arial", 20))

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
