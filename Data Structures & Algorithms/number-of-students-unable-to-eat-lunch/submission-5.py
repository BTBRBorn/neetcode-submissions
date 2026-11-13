from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        counter = 0
        while counter <= len(students):
            s = students.popleft()
            if sandwiches[0] == s:
                sandwiches.popleft()
                counter = 0
            else:
                students.append(s)
            counter += 1
        return len(students)
                

        