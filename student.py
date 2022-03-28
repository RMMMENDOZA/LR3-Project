"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
    
    def __eq__(self, other):
        """Returns whether the students' names are equal"""
        return self.getName() == other.getName()

    def __lt__(self, other):
        """Returns whether this student's name is less than the other student"""
        return self.getName() < other.getName()

    def __ge__(self, other):
        """Returns whether this student's name is greater than or equal to the other student"""
        return self.getName() >= other.getName()

def main():
    """A simple test."""
    student = Student("Ken", 5)
    student2 = Student("Po", 5)
    student3 = Student("Ken", 5) # Another student whose name is also Ken
    
    print("Testing for equality...")
    print(f"{student.getName()} == {student2.getName()}: {student == student2}")
    print(f"{student.getName()} == {student3.getName()}: {student == student3}")
    
    print("\nTesting for less than...")
    print(f"{student.getName()} < {student2.getName()}: {student < student2}")
    print(f"{student.getName()} < {student3.getName()}: {student < student3}")

    print("\nTesting for greater than or equal to...")
    print(f"{student.getName()} >= {student2.getName()}: {student >= student2}")
    print(f"{student.getName()} >= {student3.getName()}: {student >= student3}")

if __name__ == "__main__":
    main()


