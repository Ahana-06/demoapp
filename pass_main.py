with open("password.txt","r") as p:
    pass_1=p.read()
    if(pass_1==""):
        pass_n1=input("enter a new password of six digit: ")
        if(len(pass_n1)==6):
            pass_n2=input("enter confirmed password: ")
            if(pass_n1==pass_n2):
                with open("password.txt","w") as p:
                    print(f"password set to: {pass_n1}" )
                    p.write(pass_n1)
            elif(pass_n1!=pass_n2):
                print("enter a valid password")
        else:
            print("enter password of six digit")
    elif(pass_1!=""):
        pass_lg=input("enter login password: ")
        if(pass_1==pass_lg):
            print("successfully logged in")
        elif(pass_1!=pass_lg):
            print("enter a valid password")
