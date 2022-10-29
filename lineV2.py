import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1,y1,x2,y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    p = 2*dy - dx
    twoDx = 2 * (dy-dx)
    twoDy = 2 * dy

    if(x1 > x2):
        x = x2
        y = y2
        xEnd = x1
    
    x = x1
    y = y1
    xEnd = x2

    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while(x < xEnd):
        x = x + 1
        if(p < 0):
            p = twoDy
        else:
            y = y + 1
            p = twoDx

        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()