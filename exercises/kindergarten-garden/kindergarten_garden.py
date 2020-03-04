class Garden:
    PLANTS = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    DEFAULT_STUDENTS = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.row_1, self.row_2 = diagram.split()
        self.students = sorted(students)

    def plants(self, student):
        result = ""
        start_idx = self.students.index(student) * 2
        end_idx = start_idx + 2
        result += self.row_1[start_idx:end_idx]
        result += self.row_2[start_idx:end_idx]

        return [self.PLANTS[letter] for letter in result]
