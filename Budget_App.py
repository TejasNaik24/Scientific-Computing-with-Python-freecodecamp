class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        """Add a deposit to the ledger"""
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        """Withdraw from the category if funds are available"""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        """Calculate and return the current balance"""
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def transfer(self, amount, category):
        """Transfer funds to another category"""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        """Check if there are sufficient funds for a withdrawal"""
        return amount <= self.get_balance()
    
    def __str__(self):
        """String representation of the category"""
        title = self.name.center(30, "*")
        lines = [title]
        
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}"
            amount = amount.rjust(7)
            lines.append(desc + amount)
        
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)
        
        return "\n".join(lines)


def create_spend_chart(categories):
    """Create a bar chart showing percentage spent by category"""
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)
    
    percentages = []
    for amount in spent_amounts:
        if total_spent > 0:
            percentage = (amount / total_spent) * 100
        else:
            percentage = 0
        percentages.append(int(percentage // 10) * 10)
    
    lines = ["Percentage spent by category"]
    
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + "|"
        for percentage in percentages:
            if percentage >= i:
                line += " o "
            else:
                line += "   "
        line += " "
        lines.append(line)
    
    dashes = "-" * (len(categories) * 3 + 1)
    lines.append("    " + dashes)
    
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        line = "    "
        for category in categories:
            if i < len(category.name):
                line += " " + category.name[i] + " "
            else:
                line += "   "
        line += " "
        lines.append(line)
    
    return "\n".join(lines)


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    
    auto = Category("Auto")
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)
    
    print(food)
    print()
    print(create_spend_chart([food, clothing, auto]))