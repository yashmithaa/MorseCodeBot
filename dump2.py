


def convertTuple(tup):
    str = ' '.join(tup)
    
    return str
 
def playnext():
    if len(text) > 0:
        for i in text:
            if i =='.':
                print("")
            elif i=="-":
                print("")
            elif i=='/' or i==' ':
                print("")
            else:
                print("invalid") 
    else:
        if text =='.':
            print("")
        elif text=="-":
            print("")
        else:
            print("invalid")

# Driver code
tuple = ('..-.', '--..', '..', '....', '--')
str = convertTuple(tuple)
text = list(str)
print(text)
print(len(str))
print(type(str))

