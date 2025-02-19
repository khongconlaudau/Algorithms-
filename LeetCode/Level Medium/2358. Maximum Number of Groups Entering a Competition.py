from typing import List


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)
        group, totalgrade, maxgrade  = 1, 0, 0
        totalstudent, maxstudent = 0, 1

        for i in grades[1:len(grades)]:
            totalgrade += i
            totalstudent += 1
            if totalgrade > grades[0] and (totalgrade < maxgrade or maxgrade == 0) and totalstudent > maxstudent:
                maxgrade = totalgrade
                totalgrade = 0
                group += 1
                maxstudent = totalstudent
        return group


sol =  Solution()
grades = [10,6,12,7,3,5]
print(sol.maximumGroups(grades))
