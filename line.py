import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1,y1,x2,y2):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(1, dx + 1):
        print(p)
        if p >= 0:
            y = y + 1 if y < y2 else y - 1
            # y = y + 1
            p = p + (2 * (dy - dx))
        else:
            p = p + (2 * dy)

        x = x + 1 if x < x2 else x - 1
        # x = x + 1

        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Masukkan koordinat x1: "))
    y1 = int(input("Masukkan koordinat y1: "))
    x2 = int(input("Masukkan koordinat x2: "))
    y2 = int(input("Masukkan koordinat y2: "))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()