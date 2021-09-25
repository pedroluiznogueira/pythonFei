# Python 2D lists two dimensional list

# 2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream","banana"]

# -- Created 3 one dimensional lists --

food = [drinks, dinner, dessert]

# Here we create tree one dimensional lists
# but each element of the list will be a one dimensional list in the food list

print(food[0][0])
print(food[1][0])
print(food[2][0])
print("--------")
print("")

i = 0
for var in drinks:
    print(food[0][i], end="" + " ")
    print(food[1][i], end="" + " ")
    print(food[2][i], end="" + " ")
    i += 1
