#HACKEREARTH
L = int(input())
N = int(input())
for i in range(N):
    W, H = map(int, input().split())
    if W < L or H < L:
        print("UPLOAD ANOTHER" )
    elif W==H:
        print("ACCEPTED")
    else:
        print("CROP IT")

# rotation
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    K = K % N  
    
    result = arr[N-K:] + arr[:N-K]
    
    print(*result)

# lower upper
s = input()
result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()

print(result)

#find majority element (element that appers for than n/2 times) in an array 
arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
n = len(arr)

for num in arr:
    if arr.count(num) > n // 2:
        print(num)
        break
else:
    print("No majority element")

#Product of array except self 
#given an array return an arraywhere each element is the product of all the element in the array except itself
arr=[1, 2, 3, 4]
arr = list(map(int, input().split()))
n = len(arr)

result = []

for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= arr[j]
    result.append(product)

print(*result)
