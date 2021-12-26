# You are given two integer arrays students and sandwiches where sandwiches[i] is
# the type of the i^th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the
# preference of the j^th student in the initial queue (j = 0 is the front of the queue).
# Return the number of students that are unable to eat.

def countstudents(sandwiches, students):
    while sandwiches[0] in students:
        if sandwiches[0] == students[0]:
            sandwiches.pop(0)
            students.pop(0)
        else:
            students.append(students[0])
            students.pop(0)
        if len(sandwiches) == 0: break

    return len(students)