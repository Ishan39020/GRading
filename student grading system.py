Read skill `python-fact-grounded-coding`
Completed with input: {"skill":"python-fact-grounded-coding"}

I’ll check the empty grading file and a few small existing scripts so I can describe an implementation that matches their simple style.

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\student grading system.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\easy.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\date_to_number.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\calculator_clean.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\README.md"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\own.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\it.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\make.py"
}

Read 
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\numberpad.py"
}

Read , lines 1 to 100
Completed with input: {
  "path": "C:\\Users\\vasis\\OneDrive\\Desktop\\Python\\calculator.py",
  "view_range": [
    1,
    100
  ]
}

The target file `student grading system.py` is empty. I can’t edit files in this read-only agent mode, but this simple version should fit the straightforward style of `it.py`. It assumes grades are percentages from 0 to 100 and uses a common plus/minus scale.

```python
math_grade = float(input("Enter your math grade: "))
science_grade = float(input("Enter your science grade: "))
ela_grade = float(input("Enter your ELA grade: "))

average = (math_grade + science_grade + ela_grade) / 3

if average >= 97:
    letter_grade = "A+"
elif average >= 93:
    letter_grade = "A"
elif average >= 90:
    letter_grade = "A-"
elif average >= 87:
    letter_grade = "B+"
elif average >= 83:
    letter_grade = "B"
elif average >= 80:
    letter_grade = "B-"
elif average >= 77:
    letter_grade = "C+"
elif average >= 73:
    letter_grade = "C"
elif average >= 70:
    letter_grade = "C-"
elif average >= 67:
    letter_grade = "D+"
elif average >= 63:
    letter_grade = "D"
elif average >= 60:
    letter_grade = "D-"
else:
    letter_grade = "F"

print(f"Average: {average:.2f}")
print(f"Letter grade: {letter_grade}")
```

Paste it into the file and run it with Python.