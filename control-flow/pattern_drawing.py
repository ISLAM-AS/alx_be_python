## pattern_drawing.py

# Prompt user for pattern size:
pattern = int(input("Enter the size of the pattern: "))

# Draw the Pattern:
row = 0

while row < pattern:
    for _ in range(pattern):
        print("*", end="")
        
    print()

    row += 1