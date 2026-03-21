# https://leetcode.com/problems/palindrome-number/
 class Solution(object):
     def isPalindrome(self, x):
         og=x
         reverse=0
         while x>0:
             temp=x%10
             reverse=reverse*10 + temp
             x=x//10
         return reverse==og

# Input: x = 121
# Output: true

# https://leetcode.com/problems/richest-customer-wealth/
 class Solution(object):
     def maximumWealth(self, accounts):
         br=[]
         for i in accounts:
             ar=i
             sum=0
             for j in ar:
                 sum + = j
             br.append(sum)
         return max(br)

# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/
 n = int(input())
 ar = list(map(int, input().split()))
 mod = 10**9 + 7

 answer = 1
 for i in range(n):
     answer = (answer * ar[i]) % mod

 print(answer)
# Sample Input
 5
 1 2 3 4 5
# Sample Output
 120

# https://www.hackerrank.com/challenges/staircase/problem
#!/bin/python3

 import math
 import os
 import random
 import re
 import sys

# # Complete the 'staircase' function below.
# # The function accepts INTEGER n as parameter.

 def staircase(n):
     for i in range(1, n+1):
         print(" "*(n-i)+"#"*i)
 if __name__ == '__main__':
     n = int(input().strip())

     staircase(n)

# Input (stdin)
 6
# Your Output (stdout)
      #
     ##
    ###
   ####
  #####
 ######

# Magic Matrix: 
 8  1  6
 3  5  7
 4  9  2

# https://www.hackerrank.com/challenges/mini-max-sum/problem
#!/bin/python3

 import math
 import os
 import random
 import re
 import sys

# # Complete the 'miniMaxSum' function below.
# # The function accepts INTEGER_ARRAY arr as parameter.

 def miniMaxSum(arr):
     grt=arr[0]
     smt=arr[0]
     sgrt=0
     ssmt=0
     for num in (arr):
         if num>grt:
             grt = num
         if num<smt:
             smt=num
     for i in range(len(arr)):
         sgrt=sgrt+arr[i]
         ssmt=ssmt + arr[i]
     sgrt=sgrt-grt
     ssmt=ssmt-smt
     print(sgrt, ssmt)
  if __name__ == '__main__':
     arr = list(map(int, input().rstrip().split()))

     miniMaxSum(arr)

# Input (stdin)
 1 2 3 4 5
# Your Output (stdout)
 10 14

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
 #!/bin/python3

 import math
 import os
 import random
 import re
 import sys

# # Complete the 'birthdayCakeCandles' function below.
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY candles as parameter.

 def birthdayCakeCandles(candles):
     return candles.count(max(candles))
   
 if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')
     candles_count = int(input().strip())
     candles = list(map(int, input().rstrip().split()))
     result = birthdayCakeCandles(candles)
     fptr.write(str(result) + '\n')
     fptr.close()
   
# Input (stdin)
 4
 3 2 1 3
# Expected Output
 2

# https://www.hackerrank.com/challenges/time-conversion/problem
 #!/bin/python3

 import math
 import os
 import random
 import re
 import sys

# # Complete the 'timeConversion' function below.
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.

 def timeConversion(s):
     temp=0
     if s[8:10]=="AM" and s[0:2]!="12":
         return s[0:8]
     elif s[8:10]=="PM" and s[0:2]!="12":
         temp=int(s[0:2])+12
         s=str(temp)+s[2:]
         return s[0:8]
     elif s[0:2]=="12" and s[8:10]=="AM":
         s="00"+s[2:]
         return s[0:8]
     elif s[0:2] == "12" and s[8:10] == "PM":
         return s[0:8]

 if __name__ == '__main__':
     fptr = open(os.environ['OUTPUT_PATH'], 'w')
     s = input()
     result = timeConversion(s)
     fptr.write(result + '\n')
     fptr.close()

