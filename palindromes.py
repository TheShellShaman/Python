#Is it a palindrome?
word = 0
#verify inputs for isalpha
while word == 0:
    try:
        word = input("Please input a word to see if its a palindrome  -  ")
        for char in word:
            if not (char.isalpha() or char == " "):
                raise ValueError
        else:
            continue
    except ValueError:
        word = 0
    if word == 0:
       print("Please input only letters and spaces")

print("Your word is ", word)
word = word.lower()

#check if it is a palindrome and print
iteration = 0
word_len = 0
new_word = ""
for char in word:
    if char == " ":
        continue
    if char.isalpha():
        word_len += 1
        new_word += char

while not iteration == word_len -1:

    if new_word[iteration] != new_word[-iteration -1]:
        print(word.capitalize(), "is not a palindrome")
        break
    iteration += 1
else:
    print(word.capitalize(), "is a palindrome!")