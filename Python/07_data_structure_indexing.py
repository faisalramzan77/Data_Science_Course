# List
food = ["Biryani", "Pizza", "Burger", "Pasta"]
print(food[0])
print(food[1:3])  # Slicing to get a sublist
print(food[-1])  # Accessing the last element
food.append("Salad")  # Adding a new item
print(food)  # Display the modified list

# Set
strecord = ("Faisal","Ali", "Ahmed", "Hamza",3,4,6)
print(strecord)


print(strecord)
# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(person)
person["name"] = "Faisal"  # Updating the name
print(person)

# Tuple
fruits = ("Apple", "Banana", "Cherry")
print(fruits[0])    
print(fruits[1:])  # Slicing to get a subtuple
print(fruits[-1])  # Accessing the last element
fruits = ("Mango",) + fruits[0:]  # Tuples are immutable, but we can create a new one
print(fruits)  # Display the modified tuple