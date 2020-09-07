import random
class Icici:
    def __init__(self,id,name):
        self.balance=1000000
        self.id=id
        self.name=name
        print("Hello ",self.name," welcome to ICICI bank")
    def getId(self):
        return self.id
    def deposit(self):
        amount=float(input("enter amount to deposit "))
        self.balance+=amount
        print("\n amount deposited ",amount ,"\n your transaction id is ",random.randint(1000,10000))
        ask=input("would you like to withdraw yes|No ")
        if ask=="yes" or ask=="YES":

            self.withdraw()
            
        else:
           print(" thank you for choosing ICICI")
        #self.display() 
            
    def withdraw(self):
        amount=float(input("enter amount to withdraw  "))
        if self.balance >=amount:
            self.balance-=amount
            print(" your withdrawn amount ",amount,"\n your transaction id is ",random.randint(1000,10000))
            print(" available balance ",self.balance)
            print(" thank you for choosing ICICI")
            
        else:
            print("\n your excided the balance amount  ")
            
    def display(self):
        print(" Net Available balance ",self.balance)
        print(" thank you for choosing ICICI")

def main():
    names=["satish kumar","Prashanth","Raju","shankar","adarsh kumar","jyothi"]
    account=Icici(8335,names[random.randint(0,4)])
    max_limit=3
    while True:
        
        id=int(input("\n Enter account pin : "))
        while id < 1000 or id > 9999:
            if max_limit >=0:
                id=int(input(" \n Invalid Id ,. Re - Enter the pin : "))
                max_limit-=1
            else:
                #print(" sorry , you are excided daily limit")
                break
        if account.getId()==id:
                print("\n 1 - Deposit \t 2 - Withdraw \t 3 - display ")
                selection = int(input("\nEnter your selection: "))
                if selection == 1:
                    account.deposit()
                    break

                elif selection ==2:
                    account.withdraw()
                    break
                elif selection == 3:
                    account.display()
                    break
                else:
                    print(" are howle  choose correct option")
        else:
            if max_limit >=0:
                
                print(" Sorry,enter  correct pin")
                max_limit-=1
            else:
                print(" sorry , you are excided daily limit")
                break
main()
                
    
