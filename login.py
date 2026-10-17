#DEVELOPER SAGAR MEENA                  
from random import randint , randrange
from colorama import init, Fore, Style
import time

#USE ONLY FORMATIN FOR FRONT PAGE
print(Style.BRIGHT,Fore.BLUE + r'''
    ||-----------------------------------------------------------------------------------------------------------||
    ||-----------------------------------------------------------------------------------------------------------||
    ||                                      Welcome to Bank of India Bhopal                                      ||
    ||                                      A Govt. of India Undertaking                                         ||
    ||                                      Personal    Corporate   International                 Online         ||
    ||                                                                                            Services       ||
    ||  Digital Banking designed                      A smarter way to                                           ||
    ||  for your growth                               Use your cash digitally                     Apply          ||
    ||                                                                                            Online         ||
    ||                                                ----------------------------                               ||
    ||                                                |  Send, receive and use   |                Rates &        ||
    ||                                                | digital cash all through |                Charges        ||
    ||                                                | Bank of India App        |                               ||
    ||                                                ----------------------------                Branch         ||
    ||                                                                                            Locator        ||
    ||                                                                                                           ||
    ||       | CBDC now works | Programmables rules | Auto load that  | pinless transaction |                    ||
    ||       | with UPI       | for smartes control | keeps you ready | for quick payment   |                    ||
    ||-----------------------------------------------------------------------------------------------------------||
    ||-----------------------------------------------------------------------------------------------------------||
''')


# LOG IN FRONT PAGE
print(Fore.RED , Style.DIM + r'''
                                                Login with OTP
                                          Enter your log in details
      -----------------------------------------------------------------------------------------------------------
      ''')
print("\n")


#USER SE MOBILE NO LENE KE LIYE USE KIYA
def number():
    try:
        global num
        num = int(input(Fore.YELLOW + "Please Enter your number :"))
    except:
        print(Fore.RED + "Please enter a valid number...")
        number()
number()
print("\n \n")


# OTP SENDING PROGRESS
old = randint(1000,9999)
print(Fore.MAGENTA + f"<#> {old} is your Account  \nLogin OTP. DO NOT SHARE this \nwith Bank of India Operator or anyone.\nOTP valid for 15 mins. Send \nyour Mob.No {num}\nTeam BANK OF INDIA")
print("\n \n")


#USER SE OPT LENE JKE LIYE
def varification():
    try:
        global otp
        otp = int(input(Fore.YELLOW + "Please Enter OTP :"))
    except:
        print(Fore.RED + "Please enter a valid OTP...")
        varification()
varification()


# LOGIN FORM FUNCTION:
def write_otp():
    global branch , adhar , name, Address ,ifc
    print(Fore.BLUE + "------------------------------------------------------BANK OF INDIA LOGIN PAGE------------------------------------------------------")
    print("\n\n")
    name = input(Fore.YELLOW + "Enter Your Name :")
    branch = input(Fore.YELLOW + "Enter your Branch Name :")
    Address = Fore.YELLOW + f"AT & POST {branch.upper()} "
    ifc = input(Fore.YELLOW + "ENter your IFC CODE :")

    def cid():
        try:
             global customer_id
             customer_id = int(input(Fore.YELLOW +"Enter customer Id :"))
        except:
             print(Fore.RED + "Please Enter valid Customer Id....")
             cid()
    cid()

    def aadhar_Ver():
        global adhar
        try:
            adhar = int(input(Fore.YELLOW +"Enter your adhar NO. : "))
        except:
            print(Fore.RED + "Please ENter valid Aadhar No....")
            aadhar_Ver()
    aadhar_Ver()

    def acc_no():
        global account
        try:
            account = int(input(Fore.YELLOW + "Enter your account no :"))
        except:
            print(Fore.RED + "Please Enter valid account No...")
            acc_no()
    acc_no()

    print(Fore.GREEN + "Login Sucessful")
    print("\n\n")


#LOGIN PRINT FUNCTION
def pas_gen():
    print(Fore.WHITE + "\t\t\t\t\t\tYour PASSBOOK is Generating...")
    print("\n")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t10")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t9")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t8")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t7")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t6")
    time.sleep(0.5)
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t5")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t4")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t3")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t2")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\t1\n")
    time.sleep(0.5)
    print(Fore.GREEN + "\t\t\t\t\t\tSUCESSFULLY GENERETED!\n")

    print("\n\n\n\n\n\n\n\n\n\n")

    print(Fore.BLUE + f"\t\t\t\t\t\tWelcome to BANK OF INDIA {branch.upper()}")
    print('--------------------------------------------------------------------------------------------------------------------------------------------')
    print("\n")
    print(r''' 
    
    ______________________________________________________________________________________________________________________________________
    |                                      This pass book is system generated and does not require any initials                          |
    |                                                                                                                                    |
    |     ---------------------                                                                                                          |
    |     |                   |                                                                                                          |
    |     |                   |                                           WARNING                                                        |
    |     |                   |                                                                                                          |
    |     |                   |                       Beware of fincitious offers/messages/SMS anout lottery                             |
    |     |                   |                       winnings, cheap fund offers, employment offers, scholarship                        |
    |     |     PHOTOS        |                       offers, offer of emigration visa, offer of admission to reputed                    |
    |     |                   |                       universities abroad and similar such offers from fraudsters                        |
    |     |                   |                       within the country or from aborad.                                                 |
    |     |                   |                                                                                                          |
    |     ---------------------                                    Check Your Balance Call - 0223359****                                 |
    |                                                                                                                                    |
    |                                                                                                                                    |
    ______________________________________________________________________________________________________________________________________
                ''')
    
    print(Fore.YELLOW +f"\t\tBRANCH :\t\t{branch.upper()}\t\t\t\tAddress :\t\t{Address}")
    print(f"\t\tName : \t\t\t{name.capitalize()}\t\t\tIFC Code :\t\t{ifc}")
    print(f"\t\tAccount No.:\t\t{account}\t\t\tCustomer Id :\t\t{customer_id}")
    print(f"\t\tAadhar NO. :\t\t{adhar}")
    print("\n\n")
    print("\t\tFor your queries / enquiry\t\t\t\t\t\tGrievance Redress Officer, Zo:___________________")
    print("\t\tToll free no. of our call center : 18002****\t\t\t\tGrievance Redress Officer, Branch: Bank of India")
    print("______________________________________________________________________________________________________________________________________")
    print("\n\n")
    print(Fore.WHITE,Style.BRIGHT + "THANKYOU FOR VISITING BANK OF INDIA")
    print("\n\n\n\n\n\n\n")

# WRITE OTP SYSTEM
if otp == old:
    print(Fore.GREEN +  "Correct Otp !")
    print(Fore.GREEN + "Login Sucessful")
    print("\n\n")
    write_otp()
    pas_gen()
    

# WRONG OPT SYSTEM
elif otp != old:
    while True:
        if otp == old:
            print(Fore.GREEN +  "Correct Otp !")
            print(Fore.GREEN + "Login Sucessful")
            print("\n\n")
            write_otp()
            pas_gen()
            break
        elif otp == 555:
            print("\n")
            print("Thankyou for visiting BANK OF INDIA")
            print("\n\n")
            break
        else:
            print(Fore.RED + "Invalid OTP")
            print("For Exit press 555")
            try:
                otp = int(input(Fore.YELLOW + "Please Enter OTP :"))
            except:
                print("Please Enter Valid Number OTP>>>")