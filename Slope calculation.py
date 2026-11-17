def calculate_slope():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if x2 - x1 == 0:
            print("Error: Division by zero. The line is vertical (undefined slope).")
        else:
            m = (y2 - y1) / (x2 - x1)
            print(f"Slope (m) = {m}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    calculate_slope()