
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
          
food = Category("Food")
print(food.deposit(1000, "initial deposit"))
print(food.withdraw(10.15, "groceries"))
print(food.withdraw(15.89, "restaurant and more food for dessert"))
print(food.balance)

    
def create_spend_chart(categories):
    
    row="persentage spend by category\n"
    for i in range(100, -1, -10):
        row += f"{str(i)+'/':>4}\n"
        
    print(row) 
    
create_spend_chart([])       
    
#   chart= "Percentage spent by category\n"
#   percentList = []
#   totalSpent= 0
 
#   #get percent
#   for category in categories:
#     wthdrAmount = -(category.ledger[1]["amount"])
#     totalSpent += wthdrAmount
#   for category in categories:
#     wthdrAmount = -(category.ledger[1]["amount"])
#     percentList.append(int((wthdrAmount/totalSpent)*100))

#   #make bars
#   top=100
#   while top >= 0:
#     i = 0
#     if len(str(top)) < 3:
#       while i < (3-len(str(top))):
#         chart += (' ')
#         i += 1
#     chart = chart + str(top) + '|'
#     i = 0
#     while i < len(categories):
#       if (percentList[i] >= top):
#         chart += " o "
#       else: chart += "   "
#       i += 1
#     chart += " \n"
#     top -= 10
#   #line
#   chart = chart + "    " + ("---"* len(categories)) + "-"
#   #categories
#   maxLength= 0
#   for category in categories:
#     if len(category.name) > maxLength:
#       maxLength = len(category.name)
#   i = 0
#   while i < maxLength:
#     chart += "\n    "
#     for category in categories:
#       try:
#         chart = chart + ' ' + category.name[i] + ' '
#       except:
#         chart += "   "
#     chart += " "
#     i += 1
#   chart 
#   return chart
    