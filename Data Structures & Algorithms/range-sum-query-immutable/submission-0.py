class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []

        for i, n in enumerate(nums):
            if i == 0:
                self.prefix.append(n)
            else:
                self.prefix.append(self.prefix[i - 1] + n)

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 < 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)