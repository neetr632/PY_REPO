# Define a dictionary named "course" containing information about different programming courses
course = {
    "php": {
        "duration": "2 months",  # Duration of the PHP course
        "fees": "15000",  # Fees for the PHP course
    },
    "python": {
        "duration": "2 months",  # Duration of the Python course
        "fees": "15000",  # Fees for the Python course
    },
    "java": {
        "duration": "2 months",  # Duration of the Java course
        "fees": "1500089",  # Fees for the Java course (incorrect value)
    },
}

# Update the fees for the Java course to the correct value
course["java"]["fees"] = 200000

# Update the duration for the Python course
course["python"]["duration"] = "3 months"

# Print the entire dictionary
print("Course information:", course)

# Access and print specific information
print(f"PHP course fees: {course['php']['fees']}")
print(f"Python course duration: {course['python']['duration']}")
print(f"Java course fees: {course['java']['fees']}")

# Loop through the dictionary and print each course information
print("\nCourse details:")
for course_name, course_details in course.items():
    print(f"\nCourse: {course_name}")
    print(f"Duration: {course_details['duration']}")
    print(f"Fees: {course_details['fees']}")
