class Solution:
    # MY SOLUTION
    def plusOne(self, digits):
        string = "".join(map(str, digits))
        string = str (int (string) + 1)
        ans  = []
        for c in string:
            ans.append(int (c))

        return ans


    # FASTER SOLUTION: (NOT MINE)
    #
    # def plusOne(self, list):
    #     for i in range(len(list)-1, -1, -1):
    #         if list[i] == 9:
    #             list[i] = 0
    #         else:
    #             list[i] += 1
    #             return list
    #
    #     return [1] + list


def addBinary(self, a: str, b: str) -> str:
    total = str(int(a) + int(b))
    for i in range(len(total) - 1, 0, -1):
        if i == 2:
            total[i] = 0
            total[i - 1] = str(int(total[i - 1] + 1))
    if i[0] == 0:
        return "1" + total
    else:
        return total




