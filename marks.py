The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored   Grade 
    100             S
  90 - 99           A
  80 - 89           B
  70 - 79           C
  60 - 69           D
  50 - 59           E
    <50             F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.


solution
a=int(input())
if a>100:
  print('invalid input')
elif a==100:
  print('S')
elif a>=90 and a<=99:
  print('A')
elif a>=80 and a<=89:
  print('B')
elif a>=70 and a<=79:
  print('C')
elif a>=60 and a<=69:
  print('D')
elif a>=50 and a<=59:
  print('E')
else:
  print('F')
