import fileinput

def search_and_enter(phonenum, newtext):
    filename = "text_file.txt"
    file = open(filename, "r")
    linefile = open("linefile.txt", "w+")
    num = 1
    for num, line in enumerate(file, 1):
        print(num)
        #if line == :
        #    print("after the if")
        #    open(filename, "a")
        #    file.write(phonenum)
        #    file.write(newtext)
        if phonenum in line:
            break
    file.close()
    file = open(filename, "r")
    for x in range (0, num-1):
        linefile.write(file.readline())
    newtext = file.readline().rstrip() + ", " + newtext;
    linefile.write(newtext)
    for line in file:
        linefile.write(file.readline())
    linefile.close()
    file.close()

def main():
    phonenum = "8675309"
    newtext = "Jeremy"
    #phonenum, newtext = tuple
    search_and_enter(phonenum, newtext)

if __name__ == "__main__":
    main()
