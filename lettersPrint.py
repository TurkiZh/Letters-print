
letters = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            ",", "."
            ]

output = ""
letterscounter = 0
textcounter = 0
FINISH = True

print("Enter text:")
text = input()

while FINISH:
    print(output + letters[letterscounter])
    
    if(text[textcounter] == letters[letterscounter]):
        output = output + letters[letterscounter]

        letterscounter = 0
        textcounter = textcounter + 1
        if(textcounter == (text.__len__())):
            FINISH = False
        
    else:
        letterscounter = letterscounter + 1
