#better cesear cipher

word = 0
while word == 0:
    try:
        word = input("Enter your word - ")
        for char in word:
            if not (char.isalnum or char == " "):
                raise ValueError
        else:
            continue
    except ValueError:
        word = 0
    if word == 0:
        print("Please input a combination of numbers and letters")


shift =  0

while shift == 0:
    try: 
        shift = int(input("How many characters do you want to shift?   "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect Shift Value")


cipher = ""
for char in word:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char
#for char in cipher:
   # print(char, ord(char))
print(cipher) 

