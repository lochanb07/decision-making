Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
solution:
a=int(input())
b=int(input())
if a==b:
    print(a,'eqauls to',b)
elif a>b:
     print(a,'greater than',b)
else:
    print(a,'less than',b)

