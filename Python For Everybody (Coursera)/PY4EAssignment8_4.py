"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word in lst:
            continue
        else:
            lst.append(word)
            
lst.sort()
print(lst)

