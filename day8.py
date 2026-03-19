#Twosum
def twoSum(nums, target):
    num_map = {}   # value : index

    for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in num_map:
            return [num_map[remaining], i]

        num_map[nums[i]] = i

#fizzBuzz
  class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

# running sum
    class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result

# next largest number
arr = [4, 5, 2, 25]

for i in range(len(arr)):
    next_greater = -1
    
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            next_greater = arr[j]
            break
    
    print(next_greater, end=" ")

        return result
