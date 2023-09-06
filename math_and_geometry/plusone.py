class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1

        for i in range(len(digits)-1,-1,-1):
            if not c:
                break
                
            v = digits[i]+c
            r = v % 10
            c = v // 10
            digits[i] = r
        
        if c:
            digits = [1]+digits

        return digits
