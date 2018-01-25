def function6ii(name , new_salary):
    if name in employee:
            employee[name]=new_salary
    else:
           return "Name is not in the dictionary"
    print(name, "makes", employee[name], "dollars")
employee = {"Rayyan": 1000, "Zain": 399, "Asif":1}

function6ii("Rayyan", 293847)
