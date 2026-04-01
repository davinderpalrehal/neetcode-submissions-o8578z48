class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = True

        for i in reversed(range(len(digits))):
            if overflow:
                overflow = False
                digits[i] += 1
                if digits[i] >= 10:
                    digits[i] = digits[i] % 10
                    overflow = True
        
        if overflow:
            digits.insert(0, 1)
        
        return digits