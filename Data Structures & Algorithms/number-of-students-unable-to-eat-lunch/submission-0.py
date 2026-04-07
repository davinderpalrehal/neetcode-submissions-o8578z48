class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sands = {0: 0, 1: 0}
        for s in students:
            sands[s] += 1
        
        for s in sandwiches:
            if sands[s] <= 0:
                break
            sands[s] -= 1
        
        return sands[0] + sands[1]