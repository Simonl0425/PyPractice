

def printHello():
    print "hello\n"

def getHello():
    return "hello"

for i in range(5):
    printHello()

count = 0
while(count < 3):
    print "while " + getHello() + "\n";
    count = count + 1
