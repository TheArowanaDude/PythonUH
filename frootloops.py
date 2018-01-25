grades = 0.0
for subject in ['Math', 'Calc', 'Phys', 'Hist', 'Lit', 'COSC']:
    grades = grades + float(input("Please enter grade for" + subject + "\n"))
    print("In loop: value of subject is", subject)
    print("Cumulative grades so far is", grades)
    counter= counter + 1
print("Total subjects is", counter)
gpa = grades/counter
print("Your GPA is", gpa)
