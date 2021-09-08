# while loop =  a statement that will execute it's block of code,
#               as long as it's condition remains true

name = "" # that is the of making the variable name to exist, is kind of like the do while loop

while len(name) == 0: # while the input is nothing
    name = input("Enter your name: ")

print("Hello "+name)