# a=int(input("Enter any value"))
# b=int(input("Enter any value"))
# print(a+b)

# second program (sum of 2 digit of number)
a=int(input("Enter any value"))
c=a//10
d=a%10
print(c+d)

# third program. (sum of 2 digit of number)
a=int(input("Enter any value"))
c=a//10
d=a%10
e=c//10
f=c%10
print (d+e+f)

# third program. (sum of 5 digit of number)
a=int(input("Enter any value"))
c=a//10
d=a%10
e=c//10
f=c%10
g=e//10
h=e%10
i=g//10
j=g%10
print(d+f+h+j+i)

# peterson number
sum=0
b=int(input("enter the number"))
x=b
while b>0:
    a=b%10
    f=1
    for i in range(1,a+1):
        f*=i
    sum+=f 
    b=b//10
if sum==x:
    print("It is peterson")
else:
    print("It is not peterson")

# no of digit
b=int(input("enter the number"))
count=0
while b>0:
    n=b%10
    count+=1
    b=b//10
print(count)

# sum of digit 
b=int(input("enter the number"))
sum=0
while b>0:
    n=b%10
    sum+=n
    b=b//10
print(sum)

# find the missing number in the list
count=1
a=["1","2","3","4","5","6","7","8","10"]
for i in a:
    if i!=str(count):
        print(count)
        break
    count+=1

# armstrong number
b=int(input("enter the number"))
temp=b
c=b
count=0
while b>0:
    n=b%10
    count+=1
    b=b//10
sum=0
while temp>0:
    n=temp%10
    sum+=(n**count)
    temp=temp//10
if sum == c:
    print("Armstrong")
else:
    print("not Armstrong")

# armstrong no from 0 to n
n=int(input("enter range"))
for i in range(1,n):
    temp=i
    c=i
    count=0
    while i>0:
        n=i%10
        count+=1
        i=i//10
    sum=0
    while temp>0:
        n=temp%10
        sum+=(n**count)
        temp=temp//10
    if sum == c:
        print(sum)

# Day 3

# code 1
n=int(input("enter range"))
sum=1
m=int(input("enter number"))
for i in range(1,n):
    sum+=((m**i)/i)
print(sum)

# code 2 pattern printing
n=int(input("Enter the row"))
m=int(input("Enter the coloumn"))
for i in range(0,n):
    for j in range(0,m):
        print(i+1,end="")
    print()

# code 3 pattern printing
n=int(input("Enter the row"))
m=int(input("Enter the coloumn"))
for i in range(1,n):
    for j in range(1,m):
        print(j,end="")
    print()

# code 4
o=int(input("Enter the row"))
m=int(input("Enter the coloumn"))
n=1
for i in range(1,0):
    for j in range(1,m):
        print(n,end="\t")
        n+=1
    print()

# code 5 ascii character pattern
n=int(input("Enter the row"))
m=int(input("Enter the coloumn"))
x=65
for i in range(1,n):
    for j in range(1,m):
        print(chr(x),end="\t")
        x+=1
    print()

# code 6 increasing number pattern
n=int(input("Enter the row"))
x=1
for i in range(0,n):
    for j in range(1,x):
        print(j,end="\t")
    x+=1
    print()

# code 7 same number on increasing order
n=int(input("Enter the row"))
x=1
for i in range(0,n):
    for j in range(0,x):
        print(x,end="\t")
    x+=1
    print()

# code 8 star printing
n=int(input("Enter the row"))
x=n
for i in range(0,n):
    for j in range(1,x):
        print("*",end="\t")
    x-=1
    print()

# Day 4
# code 1
ls="gayatri"
a=len(ls)
b=[]
for i in range(a-1,0,-1):
    b.append(ls[i])
print(b)
