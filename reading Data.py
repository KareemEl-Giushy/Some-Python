def main():
    x = input("What Do Ypu Want To Write In The file ")
    file = open("text.txt", "a")
    file.write(x)
    file.close()
    readf = open("text.txt", "r")
    for reader in readf:
        print(reader,"\n")
    readf.close()
main()
print(input("Press Enter To Exit "))
