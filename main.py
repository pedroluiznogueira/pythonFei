# list = used to store multiple items in a single variable

food = ["apple", "zannit", "pizza","hamburger","hotdog","spaghetti","pudding"]

# food[0] = "sushi" # changing "pizza" to "sushi"

food.append("ice cream") # insert something in the end of the list
food.remove("hotdog") # delete something from the list
food.pop(0) # remove by index
food.insert(2,"cake") # it is like append but in the beggining, first argument index and second argument element
food.sort() # sorts in alphabetical order
food.clear() # clears the list

for f in food:
    print(f)