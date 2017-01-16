import turtle
import sandpile_generator
import sandpile_deserializer


def paint_sandpile_fractal(screen, turtle, dotsize, colors, sandpile):
    """
    Paints a sandpile fractal on a given screen
    :param screen: Screen to paint ont
    :param turtle: Turtle to be used for painting
    :param dotsize: Size of the dots to be painted
    :param colors: Availabile colors for different no of sandpiles. Format: {n: "color" }
    :param sandpile: The sandpile fractal to paint
    :return: None
    """
    for i, ((x, y), sand) in enumerate(sandpile.items()):
        turtle.goto(x * dotsize, y * dotsize)
        turtle.pencolor(colors[sand])
        turtle.dot(dotsize)


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.tracer(1500, 1)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    colors = {
        0: "black",
        1: "green",
        2: "lightblue",
        3: "purple",
        4: "green"
    }

    sandpile = sandpile_generator.generate_sandpile_matrix(20000, 3)
    paint_sandpile_fractal(screen, pen, 2, colors, sandpile)

    screen.exitonclick()
