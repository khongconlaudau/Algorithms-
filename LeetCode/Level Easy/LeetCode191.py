# Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        index = findIndex(n)
        step = 0
        if index == 1:
            return 1
        else:
            for i in range(index - 1, -1, -1):
                if n >= 2 ** i:
                    n -= 2 ** i
                    step += 1
        return step
def findIndex(n) -> int:
    for i in range(1,32):
        if (2 ** i) == n:
            return 1
        elif (2 ** i) > n:
            return i

# Beats: 90.60%
z = "-32"
print(z.isdigit())
len()
z = int(-91283472332)
print(z)

print(-2**31)