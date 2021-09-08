# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "": # it will stay in the loop unless it is != than ""
        break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-": # skips "-"
#         continue
#     print(i, end="")

for i in range(1,15):
    if i == 13: # in the output will be missing number 13
        pass
    else:
        print(i)