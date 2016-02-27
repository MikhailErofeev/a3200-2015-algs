import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().split(' ')

for i in range(len(nums)):
    nums[i] = int(nums[i])
nums.sort()

res = [0 for i in range(n + 2)]
res[0] = 1

for j in range(0, len(nums)):
    for i in range(1, n + 2):
        if (i - nums[j] >= 0):
            res[i] += res[i - nums[j]]

print(res[n])
