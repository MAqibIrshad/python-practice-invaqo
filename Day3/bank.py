class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self._transactions = 0
        self.total_deposits = 0.0
        self.total_withdrawls = 0.0
        self.bank_report = {}
    
    def get_bank_report(self):
        keys = ["Transactions", "Total Deposits", "Total Withdrawls"]
        values = [self._transactions,
              self.total_deposits,
              self.total_withdrawls]

        return dict(zip(keys, values))

    @property
    def transactions(self):
        return {
            "Deposits": self.total_deposits,
            "Withdrawls":self.total_withdrawls,
            "total_transactions": self._transactions
        }

    
    def add_transactions(self, choice):
        self._transactions += 1

        if choice.lower() == "d":
            self.total_deposits += 1
        elif choice.lower() == "w":
            self.total_withdrawls += 1

        # self._transactions = len(self.total_deposits) + len(self.total_withdrawls)


        
class Account(Bank):
    def __init__(self, customer_name:str, customer_id:str, balance:float, operation_status=None, deposit_no=0, withdrawl_no=0):
        # initialize base Bank with default values
        super().__init__(bank_name="")
        self.deposit_no = deposit_no
        self.withdrawl_no = withdrawl_no
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.operation_status = operation_status
        self.balance = balance

    def deposit(self, operation_status, amount: float):
        if operation_status is not None:
            self.balance = self.balance + amount
            self.deposit_no = self.deposit_no + 1
            self.add_transactions("D", amount)
            
        

    def withdraw(self, operation_status, amount: float):
        if operation_status is not None and self.balance >= amount:
            self.balance = self.balance - amount
            self.withdrawl_no = self.withdrawl_no + 1

    def getAccountDetail(self):
        return {
            "Customer Name": self.customer_name,
            "Customer ID": self.customer_id,
            "Balance": self.balance,
            "Deposit No": self.deposit_no,
            "Withdrawl No": self.withdrawl_no
        }
    @property
    def deposits(self):
        return self.deposit_no
    
    @property
    def withdrawls(self):
        return self.withdrawl_no
    
    def balance(self):
        return self.balance
    
    def set_balance(self, value):
        self.balance = value
    
    def transactions(self, data:dict):
        return super().transactions(data)


Bank = Bank(bank_name="MyBank")
Account = Account(customer_name="John Doe", customer_id="12345", balance=1000.0)
Account.deposit(operation_status=True, amount=500.0)
print(Account.balance)
print(Account.getAccountDetail())
print(Bank.get_bank_report())
print(Bank.transactions)

