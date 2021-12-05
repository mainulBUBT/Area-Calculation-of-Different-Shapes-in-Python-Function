import math


def Area(choice):
    if choice == "circle":
        radius = int(input("Enter Radius: "))
        area = math.pi * (radius * radius)
        return area
    elif choice == "rectangle":
        length = int(input("Enter Length: "))
        width = int(input("Enter width: "))
        area = float(width * length)
        return area
    elif choice == "square":
        side = int(input("Enter side: "))
        area = float(side * side)
        return area
    elif choice == "triangle":
        base = int(input("Enter Base: "))
        height = int(input("Enter Height: "))
        area = float((base * height) / 2)
        return area
    elif choice == "trapezium":
        base_a = int(input("Enter Base a: "))
        base_b = int(input("Enter Base b: "))
        height = int(input("Enter Height: "))
        area = float((height * (base_a + base_b)) / 2)


print("Shape choose: Circle, Rectangle, Triangle, Square or Trapezium")
while True:
    choice = input("Enter a shape choice for Area: ").lower()
    result = Area(choice)
    if result != None:
        print("Area of " + choice + " is", format(result, ".2f"))
    else:
        print("Enter a Valid Shape")
