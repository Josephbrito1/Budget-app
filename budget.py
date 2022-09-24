class Category:
    def __init__(self, categorie):
        self.name=categorie
        self.ledger=[] #saldo Guardado
        self.balance=0.0
        
    def __str__(self) -> str:
        #este ticket se dividira en las sigueientes partes:
        #1.membrete
        #2.parte de deposito
        #3.parte de retiro
        #4.parte de transferencia
        #5.total de todo
        

        width=26
        title=self.name.center(width, '*') + "\n"
        
        value=0
        
        for item in self.ledger:
            title +=f"{item['description']}{item['amount']:>{30-len(item['description'])}}\n"
            value += item['amount']
        return title          
        

    def deposit(self, amount, description=''):
    
        self.ledger.append({'amount':amount, 'description': description})
        self.balance+=amount
        
        


    def withdraw(self, amount, description=''):        
    
       if (self.check_funds(amount)):
           self.ledger.append({'amount': -amount, 'description': description})
           self.balance-=amount
           
           return True
       return False               
        
    def  get_balance(self):
        return self.balance    
    
    def transfer(self, amount,  category):
         
        if (self.check_funds(amount) == True):
            self.withdraw(amount, f"Transfer to {category.name}") #"discounted from",
            self.deposit(amount,  f"Transfer from {self.name}") #"transfer to",  
                            
            return True
             
        return False   

    def check_funds(self, amount):
      
        if (self.balance >= amount):
            return True
        return False
          





    

        
def create_spend_chart(categories):
  category_names = [] # this list with the one below will have a correlation of indices
  spent = [] # each element in the list is the sum of the withdraws for each category
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']  #sum of withdraws from a category
    spent.append(round(total, 2)) # adding the category's total withdraws to the list
    category_names.append(category.name) 

  for category_amount in spent:
    spent_percentages.append(round(category_amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -1 , -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0
  
  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length - 1:
      graph += "\n     "

  return(graph)    
    
      
    



