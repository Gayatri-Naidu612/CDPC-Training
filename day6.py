#rotate an array to  right by a given numbers of stepsarr = [1, 2, 3, 4, 5]
num = 2
rotate = arr[-num:]+arr[:-num]
print(rotate)

n=1
arr=[1, 2, 3, 4, 5]
for x in range(n):
    temp=arr[-1]
    for i in range (len(arr),0,-1):
        arr[i]=arr[i-1]
        arr[0]=[temp]
print(temp)

# compareTriplets
def compareTriplets(a, b):
    alice = 0
    bob = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
            
    return [alice, bob]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)

print(result[0], result[1])

# aVeryBigSum
def aVeryBigSum(arr):
    total = 0
    for num in arr:
        total = total + num
    return total

n = int(input())                 # size of array
arr = list(map(int, input().split()))

result = aVeryBigSum(arr)
print(result)

#diagonalDifference
def diagonalDifference(arr, n):
    primary = 0
    secondary = 0
    
    for i in range(n):
        primary = primary + arr[i][i]
        secondary = secondary + arr[i][n-i-1]
        
    return abs(primary - secondary)

n = int(input())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

result = diagonalDifference(arr, n)
print(result)

# plusMinus
def plusMinus(arr, n):
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")


n = int(input())
arr = list(map(int, input().split()))

plusMinus(arr, n)
