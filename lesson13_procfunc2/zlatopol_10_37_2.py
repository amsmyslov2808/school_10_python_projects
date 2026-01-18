def draw_line(count_symbols):
    print("*" * count_symbols)


def draw_react(rows, cols):
    for i in range(rows):
        draw_line(cols)


draw_react(10, 6)
