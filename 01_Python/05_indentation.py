# Indentation means adding spaces or tabs at the beginning of a line of code to show which lines are 
# inside a block (like inside a function, loop, or if-statement).

a = 2 
c = 3
b = 23.7
print(a<c)
if a<c:
    print("a is less than c")  # This line is indented, so it's part of the if block
else:
    print("a is not less than c")
print(b<c)  # This line is not indented, so it's outside the if block
if b<c:
    print("b is less than c")  # This line is also indented, part of the if block   
else:
    print("b is not less than c")