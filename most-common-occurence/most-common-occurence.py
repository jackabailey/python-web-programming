# A Simple Python program to count the number of occurences of each item in a list of items
        # Items in the form of a CSV string.

#import os
#from tracemalloc import stop
#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))


with open("text/data.txt", "r") as f:
    input_string = f.read()

#print("\nYour input string is: " + input_string)
# Locate Unique Items
unique = []

for i in input_string.split(","):
    # Seperate the values by comma and run through each item

    exists = False # Assume the item doesn't exist
    for item in unique:
        # For each item in the list of unique items...

        if item == i:
            # If the item exists...
            exists = True
    if exists is False:
        # If the item doesnt exist, append it to the end of the unique items list
        unique.append(i)

print()
#for x in range(len(unique)):
    #print("Unique Item: " + unique[x])


# Count Occurences of each item
occurencelist = []

list = input_string.split(",")

for uniqueitem in unique:
    # For each unique item

    cnt = 0
    for word in list:
        # Take each word in the list...

        if word == uniqueitem:
            # And check it against the current unique item

            cnt = cnt + 1 # Increase the counter if a copy of the item is found

    occurencelist.append([uniqueitem, cnt])
    # Add the item, and the count of that item to the end of occurencelis

print("\nList of occurences per item")
print(*occurencelist)

numoccurences = 0
mostitemslist = []

for index in occurencelist:
    # For each item count in occurencelist

    if index[1] > numoccurences:
        # If the item count is less than the count currently stored
        numoccurences = index[1] # Set the count to the number of occurences



for index in occurencelist:
    if index[1] == numoccurences:
        mostitemslist.append(index)


print("\nThe most commonly occuring item(s) is:")
print(mostitemslist)