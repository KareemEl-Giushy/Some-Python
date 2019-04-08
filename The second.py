import datetime
def main():
    year = input("The Year You was born ")
    if(year == ""):
        print("Please Input A Number")
        main()
    now = datetime.datetime.now().year
    age = now - int(year)
    print("You are {} years old".format(age))
main()
print(input("Press Enter To Exit"))
