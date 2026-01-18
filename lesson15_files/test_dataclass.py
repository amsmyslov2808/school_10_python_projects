from dataclasses import dataclass


@dataclass
class Circle:
    radius: float
    color: str


# Создание списка кругов
circles = [
    Circle(radius=5.0, color="red"),
    Circle(radius=10.2, color="blue"),
    Circle(radius=3.5, color="green"),
]

# Обращение к полям
circles[0].color = "green"
print(circles[0].color)  # red
print(circles[1])  # Circle(radius=10.2, color='blue')
