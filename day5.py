1. Solve Me First (HackerRank)

Program to add two numbers.

def solveMeFirst(a, b):
    return a + b

num1 = int(input())
num2 = int(input())

res = solveMeFirst(num1, num2)
print(res)

Example
Input

2
3

Output

5
2. Simple Array Sum (HackerRank)

Program to find the sum of elements in an array.

def simpleArraySum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))

result = simpleArraySum(ar)
print(result)

Example
Input

5
1 2 3 4 5

Output

15
3. Find Maximum and Minimum in an Array
def maxmin(ar):
    largest = ar[0]
    smallest = ar[0]

    for i in ar:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    print("Largest:", largest)
    print("Smallest:", smallest)


n = int(input("Enter range: "))
ar = []

for i in range(n):
    x = int(input("Enter number: "))
    ar.append(x)

maxmin(ar)
4. Different Ways to Take Input in Python
1. Single Input
n = int(input())
2. Two Inputs
a = int(input())
b = int(input())
3. Multiple Inputs in One Line
a, b = map(int, input().split())
4. List Input
ls = list(map(int, input().split()))
5. Using eval()
arr = eval(input())
5. Remove Duplicates from a List
def remove_duplicates(ar):
    result = []

    for i in ar:
        if i not in result:
            result.append(i)

    return result


n = int(input("Enter range: "))
ar = []

for i in range(n):
    x = int(input("Enter number: "))
    ar.append(x)

print(remove_duplicates(ar))

Example
Input

5
1 2 2 3 4

Output

[1, 2, 3, 4]
6. Pattern Using While Loop
i = 1
j = 10

while i < j:

    if i == 3 and j == 8:
        i += 1
        j -= 1
        continue

    print(i, "\t", j)

    i += 1
    j -= 1

Output

1    10
2    9
4    7
5    6
7. Alternating Positive and Negative Numbers in an Array
arr = [1, -2, 3, -4, -1, 4]

pos = []
neg = []

# separate positive and negative numbers
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []
i = j = 0

# arrange alternately
while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1

# add remaining elements
result.extend(pos[i:])
result.extend(neg[j:])

print(result)

Output

[1, -2, 3, -4, 4, -1]
