class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        b = int(sqrt(c))
        
        while a <= b:
            squaresum = a * a + b * b
            if squaresum == c:
                return True 
            elif squaresum < c:
                a += 1
            else:
                b -= 1
