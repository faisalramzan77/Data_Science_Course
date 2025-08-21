a = 20
b = 47
food = ["Biryani", "Pizza", "Burger", "Pasta", "Salad", "Sushi", "Tacos", "Nachos", "Fries",]
# Control Flow Statements
# 1. If-Else Statement
if a < b:
    print("a is less than b")   
else:
    print("a is not less than b")
# 2. If-Elif-Else Statement
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")
# 3. for Loop
for item in food:
    print(item)
    if item == "Pasta":
        print("Pasta is existing in the food list")
# 4. for Loop with range
for i in range(5):
    if food[i] == "Pizza":
        print("Pizza is found at index", i)
# 5. for Loop with else
for i in range(5):
    if food[i] == "Pizza":
        print("Pizza is found at index", i)
        break
else:
        print("Pizza is not found")
        
# 6. while Loop
i = 0
while i < len(food):
    print(food[i])
    i += 1
