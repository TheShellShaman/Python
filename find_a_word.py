first = input("What is the first word?  -  ")

second = input("What is the second string?  -  ")

for l in first:
    exists = (second.find(l))
    if exists == -1:
            print("This word does not exist inside the other word")
            break
else:
            print("All letters exist in the other sentence/string")
            


print(second.find("t"))