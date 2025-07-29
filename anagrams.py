#Anagram Program

#define Variables

#first word to compare
first_word = 0

#Verify input is good
while first_word == 0:

    try:
        first_word = input("What is the first word?  -  ")
        if not (first_word.isalpha()):
            raise ValueError
    except ValueError:
        print("That is not a valid iniput, please input Leters and spaces only")
        first_word = 0

#second word to compare
second_word = 0

#verify input is good
while second_word == 0:

    try:
        second_word = input("What is the second word?  -  ")
        if not (second_word.isalpha()):
            raise ValueError
    except ValueError:
        print("That is not a valid iniput, please input Leters and spaces only")
        second_word = 0


#Compare the two words

first = []
second = []
count1 = {}
count2 = {}
for letter in first_word:
    first.append(letter)

for letter in second_word:
    second.append(letter)

for letter in first:
    if letter in count1:
        count1[letter] += 1
    else:
        count1[letter] = 1
for letter in second:
    if letter in count2:
        count2[letter] += 1
    else:
        count2[letter] = 1




print(first)
print(second)
print(count1)
print(count2)