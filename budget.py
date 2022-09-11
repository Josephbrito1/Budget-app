 class Category:
    def __init__(self, categorie):
        self.name=categorie
        self.ledger=[] #saldo Guardado
        self.balance=0.0
        
    def __str__(self) -> str:
        title= f"{self.name:*30\name}"
    
         
    def deposit(self, amount, description):
        description=''
        self.ledger.append({'amount':amount, 'description': description})
        self.balance+=amount #cuando se utiliza el simbolo "+=" es que se le esta sumando a get balance
        
        
    def withdraw(self, amount, description='undefined'):        
       description=''
       if (self.check_funds(amount)):
           self.ledger.append({'amount': -amount, 'description': description}) 
           return True
       return False
         
       
    def  get_balance(self):
        return self.balance    
    
    def transfer(self, amount,  category): 
        if (self.check_funds(amount)):
            self.withdraw(amount, category.name) #"transfer to",
            category.deposit(amount,  self.name) #"transfer from",                  
            return f'the transfer  it was  successfully from {self.name} to {category.name}'
             
        return False
    
    def check_funds(self, amount):
      
        if (self.balance >= amount):
            return True
        return False 
 #estas son simples pruebas que tambien se encuentran en el main.py         
#food = Category("Food")
#food.deposit(1000, "initial deposit")
#food.withdraw(10.15, "groceries")
#food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
#clothing = Category("Clothing")
#print(food.transfer(50, clothing))
#clothing.withdraw(25.55)
#clothing.withdraw(100)
#auto = Category("Auto")
#auto.deposit(1000, "initial deposit")
#auto.withdraw(15)


    
def create_spend_chart(categories):
    
    row="persentage spend by category\n"
    for i in range(100, -1, -10):
        row += f"{str(i)+'/':>4}\n"
        
    print(row) 
    
create_spend_chart([])  
    
    
