import numbers


print("Welcome to State bank of Micah")
p=int(input("Enter your 4 digit pin number: "))
m = 25000
while  c < 3:  
    if(p == 1234):
        print("1-Withdraw")
        print("2-Balance Enquiry")
        print("3-Fast Cash")
        print("4-Deposit")
        print("5-Transfer")
        c = int(input("Please choose transactions: "))
        if (c == 1):
            w=int(input("Enter withdraw amount: "))
            if (w < m and w%100 == 0):
                print("Please take your amount:", w)

        elif(c==2):
            print("Your available amount : ",m)

        elif (c == 3):
            print("1->5,000")
            print("2->10,000")
            print("3->15,000")
            print("4->20,000")
            f = int(input("Enter fast cash option: "))
            if (f == 1 and 5000 < m):
                print("please take cash 5000")
            elif (f == 2 and 10000 < m):
                print("please take cash 10000")
            elif (f == 3 and 15000 < m):
                print("please take cash 15000")
            elif (f == 4 and 20000 < m):
                print("please take cash 20000")
            else:
                print("Invalid fast cash option, wrong choice, wrong pin number")

        elif (c == 4):
            def deposit(self):
                amount = float(input("Enter amount to be deposited: "))
                self.balance += amount
                print("\n Amount Deposited:", amount)

        elif (c == 5):
                def transfer(customers):
                    print ("You've chosen to transfer money.")
                    for i, customer in enumerate(customers):
                        print("{}. {}".format(i, customer.name))
                    i = int(input("Select the number of the account from which "
                                "you'd like to transfer money: "))
                    fro = customers[i]
                    amount = float(input("How much would you like to transfer: "))
                    if fro.balance < amount:
                        print ("The process can't be done. Please check your account balance.")
                        return

                    for i, customer in enumerate(customers):
                        print("{}. {}".format(i, customer.name))
                    i = int(input("Select the number of the account to which "
                                "you'd like to transfer money: "))        
                    to = customers[i]

                    fro.balance -= amount
                    to.balance += amount
                    print ("You have transfered money from {}'s account to {}'s account. "
                        "The new balance of {}'s account is {}. ".format(
                            fro.name, to.name, fro.name, fro.balance))