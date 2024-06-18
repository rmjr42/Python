import random

grades = [100, 90, 77, 66, 99]
#write a for loop to add the the grades
def sum_grades(grades):
        # code goes here
    return 0
# call the sum function then get the average
def average_grades(grades):
        # code goes here
    return 0
#pass the average and return the grade depending the grade
def grade_letter(average):
        # code goes here
    return 'F'

def main():
    print("Original Grades:", grades)
    print("Sum:", sum_grades(grades))
    print("Average:", average_grades(grades))
    print("Grade:", grade_letter(average_grades(grades)))
    
    # Create a random array of grades
    random_grades = [random.randint(50, 100) for _ in range(10)]
    print("\nRandom Grades:", random_grades)
    print("Sum:", sum_grades(random_grades))
    print("Average:", average_grades(random_grades))
    print("Grade:", grade_letter(average_grades(random_grades)))

if __name__ == "__main__":
    main()