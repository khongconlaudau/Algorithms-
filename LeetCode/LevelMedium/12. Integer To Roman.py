class Solution:
    def intToRoman(self, num: int) -> str:
        rs = ""
        table = {
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
        }
        for key, value in table.items():
            while num >= value:
                num = num - value
                rs += key
            if num == 0:
                return rs
        return rs
