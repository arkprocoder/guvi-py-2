class Bankaccount():
    def __init__(self,account_number,account_holder_name,accountopendate,city,branch,phonenumber):
        self.account_number=account_number
        self.account_holder=account_holder_name
        self.accountopendate=accountopendate
        self.city=city
        self.branch=branch
        self.phonenumber=phonenumber


    def persondetails(self):
        print(f"\n account number: {self.account_number} \n account holder name: {self.account_holder}\n account open date: {self.accountopendate}\n holder city: {self.city}\n holder branch: {self.branch}\n holder phn number: {self.phonenumber}")


    @classmethod
    def addBalance(self,cls):
        self.balance=cls
        print("Balance has been set")


    def showBalance(self):
        print(f"{self.account_number} Has the balance of {self.balance} Rs")

    @staticmethod
    def publicholiday():
        print("15th august is public holiday.....")

holder1=Bankaccount("123456789xxxxx45","sravanthi","22/12/2023","vijayawada","vijayawada",6734251689)       
holder2=Bankaccount("4875963210XXX12","roshini","21/12/2023","avanigadda","avanigadda",6424251689)
holder1.persondetails()
holder2.persondetails()

holder1.addBalance(50000)
holder1.showBalance()

holder2.addBalance(10000)
holder2.showBalance()


holder1.publicholiday()
holder2.publicholiday()