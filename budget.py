
class Category:
    def __init__(self, categorie):
        self.name=categorie
        self.ledger=[] #saldo 
        self.balance=0.0
        
    def __str__(self) -> str:
        title= f"{self.name:*30\name}"
    
         
    def deposit(self, amount, description):
        description=''
        self.ledger.append({'amount':amount, 'description': description})
        self.balance+=amount #cuando se utiliza el simbolo "+=" es que se le esta sumando a get balance
        print (f'el balance en los depositos es de {self.balance}')
        
    def withdraw(self, amount, description):        
       description=''
       if (self.check_funds(amount)):
           self.ledger.append({'amount': -amount, 'description': description}) 
           return True
       return False 
       
    def  get_balance(self):
        return self.balance    
    
    def transfer(self, amount, category): 
        if (self.check_funds(amount)):
            self.withdraw(amount, "transfer to",category.name)
            category.deposit(amount, "transfer from", self.name)
            return True
        return False
    
    def check_funds(self, amount):
      
        if (self.balance >= amount):
            return True
        return False 
#esto que esta aqui abajo solo son pruebas para ver si funcionaba la app           
#food = Category("Food")
#print(food.deposit(1000, "initial deposit"))
#print(food.withdraw(10.15, "groceries"))
#print(food.withdraw(15.89, "restaurant and more food for dessert"))
#print(food.balance)

    
def create_spend_chart(categories):
    
    column="persentage spend by category\n"
    for i in range(100, -1, -10):
        column += f"{str(i)+'/':>4}\n"
        
    print(column) 
    
create_spend_chart([])       
    
    
