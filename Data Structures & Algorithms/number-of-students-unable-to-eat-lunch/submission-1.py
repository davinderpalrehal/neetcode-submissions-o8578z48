class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studs = {0: 0, 1: 0}
        for s in students:
            studs[s] += 1
        
        for s in sandwiches:
            if studs[s] <= 0:
                break
            studs[s] -= 1
        
        return studs[0] + studs[1]