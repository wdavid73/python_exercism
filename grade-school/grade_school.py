from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list) 

    def add_student(self, name, grade):
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        return [name for grade in sorted(self.students) for name in self.students[grade]]      

    def grade(self, grade_number):
        return [name for name in self.students[grade_number]]
