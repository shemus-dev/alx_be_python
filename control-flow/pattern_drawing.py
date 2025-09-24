size = int(input("Enter the size of the pattern: "))

row = 0
while size > row:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1  # Increment to go to the next row