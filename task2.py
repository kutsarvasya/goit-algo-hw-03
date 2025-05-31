import turtle


def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def draw_koch_snowflake(level):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # найшвидша швидкість

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, 300, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0-6): "))
        if 0 <= level <= 6:
            draw_koch_snowflake(level)
        else:
            print("Рівень повинен бути в межах 0–6.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
