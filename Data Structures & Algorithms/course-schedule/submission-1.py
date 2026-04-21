class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}

        for course, required in prerequisites:
            if course not in prereq:
                prereq[course] = []
            prereq[course].append(required)
        
        course_done = set()

        def can_do_course(c, doing):
            if c in course_done:
                return True
            if c in doing:
                return False

            if c not in prereq:
                course_done.add(c)
                return True

            doing.add(c)
            for pre in prereq[c]:
                if not can_do_course(pre, doing):
                    doing.remove(c)
                    return False
                
            course_done.add(c)
            
            return True

        for course in range(numCourses):
            if course in course_done:
                continue
            
            doing = set()
            if not can_do_course(course, doing):
                return False
        
        return True