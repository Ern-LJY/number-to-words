#Inspired from https://www.youtube.com/watch?v=PIeiiceWe_w

while True:
    try:
        userInput = int(input('Hi, enter phone number: '))
        break
    except:
        print("Only numbers!")

mylist = ["apple", "orange", "flower", "foo", "foobar", "cat", "emo", "food"]
mylist.sort(key=len)
mylist.reverse()
myListConverted = []
myListConvertedStore = []
myTargetedString = ""

class checkKeypadAlphabets:
    def number(z):
        myTargetedString = z
        num2List = ["a", "b", "c"]
        num3List = ["d", "e", "f"]
        num4List = ["g", "h", "i"]
        num5List = ["j", "k", "l"]
        num6List = ["m", "n", "o"]
        num7List = ["p", "q", "r", "s"]
        num8List = ["t", "u", "v"]
        num9List = ["w", "x", "y", "z"]

        for x in num2List:
            myTargetedString = myTargetedString.replace(x, "2")
        for x in num3List:
            myTargetedString = myTargetedString.replace(x, "3")
        for x in num4List:
            myTargetedString = myTargetedString.replace(x, "4")
        for x in num5List:
            myTargetedString = myTargetedString.replace(x, "5")
        for x in num6List:
            myTargetedString = myTargetedString.replace(x, "6")
        for x in num7List:
            myTargetedString = myTargetedString.replace(x, "7")
        for x in num8List:
            myTargetedString = myTargetedString.replace(x, "8")
        for x in num9List:
            myTargetedString = myTargetedString.replace(x, "9")

        myListConverted.append(myTargetedString)

position = 0
myUserInput = str(userInput)
#Convert to Numbers
for x in range(len(mylist)):
    checkKeypadAlphabets.number(mylist[x])

#Convert to Num3
for y in myListConverted:
    if y in str(userInput):
        for x in range(len(mylist)):
            myUserInput = myUserInput.replace(y, "-"+mylist[position]+"-")
    position = position + 1

#print list

for y, x in zip(myListConverted, mylist):
    print(x+": "+ y)

print("==============================================")
checkDone = any(c.isalpha() for c in myUserInput)
if checkDone == False:
    print("No word can be found in your number.")
else:
    for x in myUserInput:
        if myUserInput[len(myUserInput)-1] == "-":
            myUserInput = myUserInput[:-1]
    print(myUserInput)