import sys




def main():
#GRID = 6

# Create a grid
    width, height = 6, 6;
    Matrix = [["X" for x in range(width)] for y in range(height)]

    print()
    for x in range(height):
        print(Matrix[x])

    print()

if __name__ == "__main__":
    main()
