import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Snake Game by Hasnain Ali")
root.resizable(False, False)

# Define constants
WIDTH = 600
HEIGHT = 400
SEG_SIZE = 20
IN_GAME = True

# Create Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.grid(row=0, column=0)

# Define the snake class
class Snake:
    def __init__(self):
        self.segments = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "Right"
        self.create_snake()
        self.bind_keys()
        
    def create_snake(self):
        for x, y in self.segments:
            canvas.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="white", tag="snake")
            
    def move(self):
        global IN_GAME, food
        x, y = self.segments[0]
        
        if self.direction == "Left":
            x -= SEG_SIZE
        elif self.direction == "Right":
            x += SEG_SIZE
        elif self.direction == "Up":
            y -= SEG_SIZE
        elif self.direction == "Down":
            y += SEG_SIZE
        
        # Check for collisions
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in self.segments):
            IN_GAME = False
            return
        
        # Move snake
        self.segments = [(x, y)] + self.segments[:-1]
        canvas.delete("snake")
        self.create_snake()
        
        # Check for food collision
        food_coords = canvas.coords(food)
        if (x, y) == (food_coords[0], food_coords[1]):
            self.segments.append(self.segments[-1])
            canvas.delete("food")
            create_food()
            
    def change_direction(self, event):
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            self.direction = event.keysym
            
    def bind_keys(self):
        root.bind("<KeyPress>", self.change_direction)

# Create the food
def create_food():
    global food
    x = random.randint(0, (WIDTH // SEG_SIZE) - 1) * SEG_SIZE
    y = random.randint(0, (HEIGHT // SEG_SIZE) - 1) * SEG_SIZE
    food = canvas.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="red", tag="food")

# Main game loop
def game_loop():
    if IN_GAME:
        snake.move()
        root.after(100, game_loop)
    else:
        canvas.create_text(WIDTH / 2, HEIGHT / 2, text="GAME OVER", fill="red", font="Arial 20 bold")

# Initialize the game
snake = Snake()
create_food()
game_loop()

# Start the main loop
root.mainloop()

