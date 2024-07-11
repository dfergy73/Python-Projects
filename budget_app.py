'''This program contains a class that is able to instantiate objects
   based on different budget categories and a function that makes a bar
   chart. The function takes a list of categories as an argument and
   returns a string that is a bar chart which shows the percentage spent
   in each category passed in to the function.'''

class Category:
    
    def __init__(self, category):
        # Need attributes for the category name and a list of transactions.
        self.category = category
        self.ledger = []

    
    # Helper method to calculate the current balance in the ledger.
    def _get_balance(self):
        balance = 0
        for amounts in self.ledger:
            balance += amounts['amount']
        return balance

    
    # Helper method to determine if the budget category has sufficient
    # funds.
    def _check_funds(self, amount):
        if amount > self._get_balance():
            return False
        else:
            return True

    
    # Method to make a deposit to the budget category.
    def deposit(self, amount, description=''):
        # Each deposit is a dictionary appended to the ledger list.
        self.ledger.append({'amount': amount, 'description': description})

    
    # Method to make a withdrawal from the budget category.
    def withdraw(self, amount, description=''):
        # Check for sufficient funds before withdrawing.
        if self._check_funds(amount):
            # Each withdrawal is a dictionary appended to the ledger list.
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    
    # Method to withdraw an amount from one category and deposit it into
    # another.
    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.category}'):
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False
    
    
    # Reformtting object's string representation to return a formatted
    # ledger.
    def __str__(self):
        # First, center the category name among asterisks with a total
        # length of 30 characters.
        cat_str = self.category
        length = len(cat_str)
        stars = 30 - length
        if stars % 2 == 0:
            string = '*' * int(stars / 2)
            string += cat_str
            string += '*' * int(stars / 2)
        else:
            string += '*' * (stars // 2)
            string += cat_str
            string += '*' * ((stars // 2) + 1)
        
        # Extract the amounts and descriptions for each transaction into
        # two different lists.
        numbers = []
        descriptions = []
        for transaction in self.ledger:
            for value in transaction.values():
                if type(value) == int or type(value) == float:
                    numbers.append(value)
                else:
                    descriptions.append(value)

        # Make a dictionary that has descriptions as the keys and the
        # amounts as the values.
        tran_dic = {descriptions[i]: numbers[i] for i in range(len(descriptions))}
        
        # Compose strings with a length of 30 characters that contain
        # the description on the left and amount on the right.
        for description, amount in tran_dic.items():
            tran_str = f'{description[:23]}'
            length = 30 - len(tran_str)
            amt_str = '%7.2f'%(amount)
            spaces = ' ' * (length - 7)
            all_str = tran_str + spaces + amt_str
            string += f'\n{all_str}'

        # Final line will be the remaining total.
        total = self._get_balance()
        total_str = '\nTotal:%7.2f'%(total)
        string += total_str

        return string


# Function to create a bar graph representing percentage spent by each
# category.
def create_spend_chart(categories):
    string = 'Percentage spent by category\n'
    # Make dictionaries to hold the totals spent by each category and
    # what percent of the sum total was spent by each category.
    cat_totals = {}
    per_dict = {}
    # Set the sum total to 0 to start.
    spend_total = 0
    # Go through each category to find their respective spending totals.
    for category in categories:
        cat_total = 0
        for transaction in category.ledger:
            for value in transaction.values():
                # Find which values are withdrawals and add them to the
                # category spending total.
                if (type(value) == int or type(value) == float) and value < 0:
                    cat_total += -value
        # Add entry for category total into dictionary. Add category total
        # to total spending.
        cat_totals[category.category] = cat_total
        spend_total += cat_total

    # Find what percent of the sum total was spent by each category.
    # Record the percent and respective category in percents dictionary.
    for key, value in cat_totals.items():
        percentage = (value / spend_total) * 100
        percentage = int(percentage // 10) * 10
        per_dict[key] = percentage
    
    # Loop through each percentage to craft the y-axis and include an
    # 'o' for each category that reaches the percentage.
    for percent in range(100,-1, -10):
        string += f'{percent:3d}| '
        for key, value in per_dict.items():
            if value >= percent:
                string += 'o  '
            else:
                string += '   '
        string += '\n'
    
    # Make a dashed line for the x-axis depending on how mnay categories
    # are included.
    cat_num = 0
    for key in per_dict.keys():
        cat_num += 1
    string += '    -'
    for dash in range(cat_num):
        string += '---'
    string += '\n'
    
    # Print each category vertically and side-by-side. The number of rows
    # will be the length of the longest category name.
    cat_names = []
    for category in categories:
        cat_names.append(category.category)
    longest_name = ''
    for name in cat_names:
        if len(name) > len(longest_name):
            longest_name = name
    for letter in range(len(longest_name)):
        string += '     '
        for name in cat_names:
            try:
                string += f'{name[letter]}  '
            except:
                string += '   '
        string += '\n'
    string = string.rstrip('\n')
    return string

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
categories = [food, clothing]
print(create_spend_chart(categories))
print(food)

