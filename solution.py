student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# First, display the complete record using for loop, printing and some string formatting only
print("Complete student record:")
for key, value in student.items():
    print(f"{key}: {value}")
print()


# Check if there's a key called 'email'. If not, ask the user to enter an email
if "email" not in student:
    student["email"] = input("Please enter an email: ")


# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("Please enter a new city: ")
while new_city.strip() == "":
    new_city = input("City cannot be empty. Please enter a new city: ")
student["city"] = new_city


# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
if student.get("phone") is None:
    print("Phone number not found.")


# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
student["contact"] = {
    "phone": "13800001111",
    "email": student["email"]
}


# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys:
# 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}


# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead.
total_score = 0
course_count = 0
for score in student["courses"].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count


# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score.
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
if average_score >= 90:
    academic_status = "Excellent"
elif average_score >= 75:
    academic_status = "Good"
elif average_score >= 60:
    academic_status = "Pass"
else:
    academic_status = "At Risk"

student["academic_status"] = academic_status


# Add the logic to search for a course.
# If the course is found, print the course name and score. If not, print "Course not found".
search_course = input("Enter a course name to search: ")
if search_course in student["courses"]:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found")


# Add the logic to update a course score.
# Ask the user to enter the course name and the new score.
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
update_course = input("Enter the course name to update: ")

if update_course in student["courses"]:
    new_score_input = input("Enter the new score: ")

    while not new_score_input.isdigit() or not (0 <= int(new_score_input) <= 100):
        new_score_input = input("Invalid score. Please enter a number between 0 and 100: ")

    new_score = int(new_score_input)
    old_score = student["courses"][update_course]
    student["courses"][update_course] = new_score
    print(f"{update_course} score updated from {old_score} to {new_score}.")
else:
    print("Course not found. No score updated.")


# Recalculate the average score and update the academic status after the course score has been updated.
total_score = 0
course_count = 0
for score in student["courses"].values():
    total_score += score
    course_count += 1

average_score = total_score / course_count

if average_score >= 90:
    academic_status = "Excellent"
elif average_score >= 75:
    academic_status = "Good"
elif average_score >= 60:
    academic_status = "Pass"
else:
    academic_status = "At Risk"

student["academic_status"] = academic_status


# Display the final formatted student record with all the updated information, including the average score and academic status.
print()
print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print()
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print()
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print()
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score}")
print()
print(f"Average Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
print()
print("=====================================")