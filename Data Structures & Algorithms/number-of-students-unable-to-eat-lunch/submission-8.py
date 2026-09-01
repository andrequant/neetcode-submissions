from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_q = deque(students)
        sandwiches_q = deque(sandwiches)

        while sandwiches_q and sandwiches_q[0] in student_q:
            if student_q[0] == sandwiches_q[0]:
                student_q.popleft()
                sandwiches_q.popleft()
            else:
                student_q.append(student_q.popleft())

        return len(student_q)