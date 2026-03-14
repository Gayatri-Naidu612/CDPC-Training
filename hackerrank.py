Q1. Say "Hello, World!" in Python
print("Hello, World!")

Output

Hello, World!
Q2. Python If–Else (Weird / Not Weird)
n = int(input())

if n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")

Explanation

Odd number → Weird

Even number between 2–5 → Not Weird

Even number between 6–20 → Weird

Even number >20 → Not Weird

Q3. Arithmetic Operators
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

Output shows:

Addition

Subtraction

Multiplication

Q4. Python Division
a = int(input())
b = int(input())

print(a // b)   # Integer division
print(a / b)    # Float division

Example
Input: 4 , 3

Output

1
1.3333333333
Q5. Loops (Print Squares)
n = int(input())

for i in range(n):
    print(i ** 2)

Example
Input

5

Output

0
1
4
9
16
