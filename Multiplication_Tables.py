# Loop through rows (numbers 2 to 12)
for row in range(2, 13):
    # Loop through columns (multipliers 2 to 12)
    for col in range(2, 13):
        # Calculate product
        product = row * col
        # Print with a tab space (\t) instead of a new line
        print(f"{product}\t", end="")
    # Move to the next line after completing a row
    print()