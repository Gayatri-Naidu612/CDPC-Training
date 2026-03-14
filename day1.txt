Python Program – Reverse a Three Digit Number
no = int(input("Enter any value: "))

n1 = no % 10      # last digit
no = no // 10     # remove last digit
n2 = no % 10      # second digit
n3 = no // 10     # first digit

rev = n1*100 + n2*10 + n3
print(rev)

Example
Input: 123
Output: 321

Algorithms and Data Structures
Algorithm

An algorithm is a step-by-step set of instructions used to solve a problem in a program.

Example: sorting numbers, searching elements, calculating factorial.

Data Structure

A data structure is a way of organizing and storing data so it can be accessed and used efficiently.

Examples: Array, Linked List, Stack, Queue, Tree, Graph.

Classification of Data Structures
1. Primitive Data Structures

Basic built-in data types.

Examples:
Integer, Float, Character, String, Boolean

2. Non-Primitive Data Structures

Linear Data Structures
Elements are arranged sequentially.
Examples: Array, Linked List, Stack, Queue

Non-Linear Data Structures
Elements are arranged hierarchically or in networks.
Examples: Tree, Graph

Big O Notation

Big O notation describes the efficiency of an algorithm as the input size increases.

It shows how the running time or memory usage grows when the data becomes large.

Types of Complexity

Time Complexity
Measures how long an algorithm takes to run.

Space Complexity
Measures how much memory an algorithm uses.

Performance Cases

Best Case – Minimum time required
Average Case – Typical running time
Worst Case – Maximum time required

Common Big O Notations

O(1) → Constant time
O(n) → Linear time
O(log n) → Logarithmic time
O(n²) → Quadratic time
O(2ⁿ) → Exponential time

Other notations:
Ω (Omega) → Best case
Θ (Theta) → Average case

Rules for Measuring Complexity

Rule 1: Single statement → O(1)
Example:

a = 5

Rule 2: Single loop → O(n)

for i in range(n):
    print(i)

Rule 3: Nested loops → O(n²)

for i in range(n):
    for j in range(n):
        print(i, j)

Rule 4: Halving each step → O(log n)

n = 64
while n > 1:
    print(n)
    n = n // 2

Rule 5: Sequential statements → complexities are added.

Common Questions
Difference Between Big O and Big Omega

Big O (O) → Worst case complexity
Big Omega (Ω) → Best case complexity

Difference Between Linear and Non-Linear Data Structures

Linear → Data stored sequentially
Examples: Array, Stack, Queue

Non-Linear → Data stored hierarchically
Examples: Tree, Graph

Example of O(log n)
n = 64
while n > 1:
    print(n)
    n = n // 2

Sequence:
64 → 32 → 16 → 8 → 4 → 2 → 1

Steps ≈ log₂ n
