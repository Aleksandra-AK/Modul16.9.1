from figures import Rectangle, Circle

rect_1 = Rectangle(4, 8, 40, 80)
rect_2 = Rectangle(9, 13, 90, 130)

circle_1 = Circle(3, 4, 6)
circle_2 = Circle(8, 12, 50)

forms = [rect_1, rect_2, circle_1, circle_2]
for figure in forms:
    print(figure.get_figure())

