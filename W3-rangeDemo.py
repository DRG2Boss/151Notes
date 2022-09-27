for number in range(50, 1000, 100):
    # This states: start at 50, and go up to (but not including) 1000 by increments of 100.
    print(f"If I was a line at x position: {number}")

for number in range(1000, 100, -100):
    # Notice that in order to count backwards, the "increment" number needs to be negative.
    print(f"If I was a line at x position: {number}")