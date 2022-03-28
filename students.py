"""
File: students.py
Generate a shuffled list of students, then use the sort method
"""

import random
from student import Student

def output(list):
    sentence = "["
    for iteration, elem in enumerate(list):
        sentence += F"\"{elem.getName()}\""
        if iteration < len(list)-1:
            sentence += ","
    sentence += "]"

    print(sentence)

def main():
    """Simple test"""

    # Generate a shuffled list
    NUM_OF_SCORES = 5
    students = []
    names = ["Phil","Sam","George","Greg","Ken","Bob","Childe"]
    while len(names) > 0:
        # Add to list of students a random name from the list of names
        students.append( Student(random.choice(names),NUM_OF_SCORES) )
        names.pop()
        
    print("Shuffled list:")
    output(students)
    
    students.sort(key=lambda x: x.getName()) # Sort the list

    print("\nSorted list:")
    output(students)
    print("")

if __name__ == "__main__":
    main()
