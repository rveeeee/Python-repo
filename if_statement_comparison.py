name = input("What is your name: ")

if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print ('Name can be a maximum of 50 characters')
else:
    print("Name looks good!")
print(len(name)) # I added the len function here to visualize what it does
# My error here is that in the first try i didn't use the len function at first which results to an error.
# I forgot that the name string cannot be compared to an integer, so I need to use len in order to compare these two.