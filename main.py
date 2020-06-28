import turtle
import Tkinter as tk

def startGame():
    game = turtle.Screen()
    game.title("Initial window")
    game.setup(width=600, height=600)
    game.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    turtle.mainloop()

app = tk.Tk(screenName="Snake",baseName="Snake", className="Snake")
app.title("Snake Game")
button = tk.Button()
button["text"] = "Start Game!"
button["command"] = startGame
button2 = tk.Button(app, text = "Exit Game", command = quit)
button.pack()
button2.pack()
app.mainloop()
