
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Bro Code"

first_name = name[:3]       # [0:3]
last_name = name[3:]        # [4:end]
funky_name = name[::2]      # [0:end:2]
reversed_name = name[::-1]  # [0:end:-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # walking backwards in the string

print(website1[slice]) # call the function slice as a index to the string
print(website2[slice]) # same
