students={
    "Alice": 85,
    "Bob": 92,  
    "Charlie": 78,
    "David": 90,
}

#2.   Asks the user to input a student's name.
name=input  ("Enter the student's name: ")

if name in students:
    print(f"{name} exists with marks {students[name]}")

else:    
    print(f"{name} does not exist in the records.")