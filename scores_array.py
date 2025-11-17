import sys

# If arguments are passed, use them
if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    # If no arguments passed (optional fallback)
    scores = list(map(int, input("Enter scores separated by space: ").split()))

total = sum(scores)
average = total / len(scores)


print("Sum of scores:", total)
print("Average of scores:", average)
