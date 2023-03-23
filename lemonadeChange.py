class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {}

        for i in bills:
            temp = i
            d[temp] = 1 + d.get(temp, 0)
            change = temp - 5
            while change > 0:
                if change - 10 >= 0 and d.get(10,0) > 0:
                    d[10] -= 1
                    change -= 10
                elif change - 5 >= 0 and d.get(5,0) > 0:
                    d[5] -=  1
                    change -= 5
                else:
                    if change > 0:
                        return False
                
        return True 