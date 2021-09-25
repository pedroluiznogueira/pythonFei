# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bro",21,"male") # lists we use "[....]" and in tuples we use "(....)"

print(student.count("Bro")) # go inside of the tuple student and use the function count
                            # wich will count the number of "Bro"(s) in the tuple
print(student.index("male")) # go inside of the tuple studente and use the function index
                             # wich will return the index of "male" in the tuple

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")