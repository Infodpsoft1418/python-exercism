from collections import defaultdict


class School:
    def __init__(self):
        self._db = defaultdict(list)

    def add_student(self, name, grade):
        self._db[grade].append(name)

    def roster(self):
        result = []
        for grade, names in sorted(self._db.items()):
            result += sorted(names)
        return result

    def grade(self, grade_number):
        return sorted(self._db[grade_number])
