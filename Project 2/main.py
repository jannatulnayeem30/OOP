from circle import circle
from rectangle import rectangle
def main():
    shape1 = circle(56)
    shape2 = rectangle(8, 8)

    print("Circle Area:", shape1.area())
    print("Rectangle Area:", shape2.area())

if __name__ == "__main__":
    main()