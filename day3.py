1. Series Calculation Program
# Calculate the series: 1 + (x^1)/1 + (x^2)/2 + ... + (x^(n-1))/(n-1)

n = int(input("Enter n: "))
x = int(input("Enter x: "))

sum = 1

for i in range(1, n):
    sum = sum + (x**i)/i

print("Result =", sum)

Example
Input: n = 3 , x = 2
Output: 4

2. Number Pattern (Repeated Row Pattern)
# Print pattern where each row contains the same number

for i in range(1, 5):        # Outer loop for rows
    for j in range(1, 5):    # Inner loop for columns
        print(i, end="")
    print()

Output

1111
2222
3333
4444
3. Sequential Number Pattern (1–16 Grid)
# Print numbers from 1 to 16 in a 4x4 grid

n = 1

for i in range(1, 5):
    for j in range(1, 5):
        print(n, end="\t")
        n = n + 1
    print()

Output

1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
4. Alphabet Pattern (A–P Grid)
# Print alphabets from A to P in a 4x4 grid

n = 65

for i in range(1, 5):
    for j in range(1, 5):
        print(chr(n), end="\t")
        n = n + 1
    print()

Output

A   B   C   D
E   F   G   H
I   J   K   L
M   N   O   P
5. Increasing Number Pattern
# Print pattern with increasing number repetition

for i in range(1, 5):
    for j in range(1, i + 1):
        print(i, end="")
    print()

Output

1
22
333
4444
6. Star Pattern (Decreasing)
# Print decreasing star pattern

for i in range(1, 5):
    for j in range(5 - i):
        print("*", end="\t")
    print()

Output

* * * *
* * *
* *
*
