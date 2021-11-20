class Category:
    ledger = list()
    name = ''
    def __init__(self, nam):
        self.name = nam
        self.ledger= []
    def deposit(self, amount, description= ''):
        am = 'amount'
        desc = 'description'
        temp= { am: amount , desc:description }
        self.ledger.append(temp)    #{"amount": amount, "description": description}  

    def withdraw(self, amount, description= '' ):        
        if self.check_funds(amount):
            am = 'amount'
            desc = 'description'
            temp= { am: -amount , desc:description }
            self.ledger.append(temp) 
            return True
        else:
            return False
        
    def get_balance(self):
        balance = 0.0
        for i in range(len(self.ledger)):
            balance +=  float(self.ledger[i]['amount'] )
        return balance

    def transfer( self, amount, category):
        if self.check_funds(amount):
            am = 'amount'
            descript = 'Transfer to ' + category.name 
            desc = 'description'
            temp= { am: -amount, desc: descript }
            self.ledger.append(temp) 
            try:
                temp2 = {am: amount, desc: 'Transfer from ' + self.name}
                category.ledger.append(temp2)
            except:
                pass
            return True
        else: 
            return False

    def check_funds (self, amount): 
        balance = self.get_balance()
        if amount > balance:
            return False
        else:             
            return True

    def __str__(self):
        report = ''
        cat_name = self.name
        x = len(cat_name)
        y = 15 - int(x / 2)
        for i in range(y):
            report += '*'
        report += cat_name
        for i in range( 15 - int(x/2) - x%2):
            report += '*'
        report += '\n'
        sumtotal = 0
        for i in range (len(self.ledger)):
            disc = self.ledger[i]['description']
            disclen = len(disc)
            if disclen > 23:
                disc = disc[:23]
                space = 7
            else: 
                space = 23 - len(disc) + 7
            report += disc
            xx = ' %.2f' % float(self.ledger[i]['amount'])
            xx = '%*s' % (space, xx[:7])
            report += xx

            sumtotal += float(self.ledger[i]['amount'])
            report += '\n'
        report += 'Total: ' 
        report += '%.2f' % (sumtotal)
        return report

def create_spend_chart (categories):
    spending = dict()
    totalspending = 0.0
    percentage = dict()
    names = list()
    total = 0.0
    response = ''
    for i in range(len(categories)):
        for j in range (len(categories[i].ledger)):
            if float(categories[i].ledger[j]['amount']) < 0:
                total += float(categories[i].ledger[j]['amount'])
        spending[categories[i].name] = total        
        total = 0.0
    for i in range(len(categories)):
        totalspending += spending[categories[i].name]
    for i in range(len(categories)):
        percentage[categories[i].name]= spending[categories[i].name]  * 100/ totalspending
    i = 100
    response += 'Percentage spent by category\n'
    while i >= 0:
        response += '%*s' % (3, i)
        response += '|'
        s = 0
        for j in range(len(categories)):
            if j == 0:
                sp = 2
            else:
                sp = 3
            if percentage[categories[j].name] >= i:    
                response += '%*s' % (sp, 'o') 
                s += 1    
            else:
                s += 1
                response += '%*s' % (sp, '')            

        i -= 10 
        response += '%*s' % (3, "\n") 
    response += '%*s' % (5, '-')
    for i in range(3*len(categories)):
        response += '-'
    response += '\n'
    namelength = 0

    for j in range(len(categories)):        
        names.append(categories[j].name)
        if len(categories[j].name) > namelength:
            namelength = len(categories[j].name)

    for i in range(namelength):      
        for j in range(len(names)):
            if j == 0:
                sp = 6
            else:
                sp = 3
            try:            
              response += '%*s' % (sp, names[j][i])        
            except: 
              response += '%*s' % (sp, ' ')
                
        if i == namelength-1:          
          response += '%*s' % (2, '')
        else:
          response += '%*s' % (3, '\n')
        
    return response
