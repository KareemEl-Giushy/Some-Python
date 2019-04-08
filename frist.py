def fun():
    o_username = ["admin", "ahmed", "kareem", "heba"]
    o_password = ["123456789"]

    username = input("Yor User Name: ")
    password = input("Enter Your Password: ")


    if username == o_username and password == o_password :
        print("Your Are Wellcome Here")
    else :
        print("sign up")
        n_user = input("Your Name: ")
        n_password = input("Your password: ")
        o_username.append(n_user)
        o_password.append(n_password)
        print(o_username)
        print(o_password)
        fun()

fun()
