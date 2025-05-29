class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        length = len(s)
        step = 0
        while True:
            if s[step + minJump] == "0":
                step += minJump
            elif s[step + maxJump] == "0":
                step += maxJump
            else:
                break

            if step == length - 1:
                return True
        return False


sol = Solution()
s = "011010"
print(sol.canReach(s, 2, 3))