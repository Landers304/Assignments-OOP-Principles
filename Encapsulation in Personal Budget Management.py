#Task 1:


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def display_category_details(self):
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")

# Example usage
if __name__ == "__main__":
    category = BudgetCategory("Groceries", 500)
    category.display_category_details()




#Task 2:


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_category_name):
        if isinstance(new_category_name, str):
            self.__category_name = new_category_name
        else:
            print("Error: Category name must be a string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if isinstance(new_allocated_budget, (int, float)) and new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
        else:
            print("Error: Allocated budget must be a non-negative number.")

    def display_category_details(self):
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")

# Example usage
if __name__ == "__main__":
    category = BudgetCategory("Groceries", 500)
    category.display_category_details()

    # Test setter methods
    category.set_category_name("Utilities")
    category.set_allocated_budget(700)
    category.display_category_details()




#Task 3:


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_category_name):
        if isinstance(new_category_name, str):
            self.__category_name = new_category_name
        else:
            print("Error: Category name must be a string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if isinstance(new_allocated_budget, (int, float)) and new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
            self.__remaining_budget = new_allocated_budget
        else:
            print("Error: Allocated budget must be a non-negative number.")

    def get_remaining_budget(self):
        return self.__remaining_budget

    def add_expense(self, expense_amount):
        if isinstance(expense_amount, (int, float)) and expense_amount >= 0:
            if expense_amount <= self.__remaining_budget:
                self.__remaining_budget -= expense_amount
                print(f"Expense of ${expense_amount} added to {self.__category_name}. Remaining budget: ${self.__remaining_budget}")
            else:
                print("Error: Expense amount exceeds remaining budget.")
        else:
            print("Error: Expense amount must be a non-negative number.")

    def display_category_details(self):
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")

# Example usage
if __name__ == "__main__":
    category = BudgetCategory("Groceries", 500)
    category.display_category_details()

    # Add expenses
    category.add_expense(100)
    category.add_expense(400)
    category.add_expense(150)
    category.add_expense(-50)  # Invalid expense amount
    category.display_category_details()




#Task 4:


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_category_name):
        if isinstance(new_category_name, str):
            self.__category_name = new_category_name
        else:
            print("Error: Category name must be a string.")

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_allocated_budget):
        if isinstance(new_allocated_budget, (int, float)) and new_allocated_budget >= 0:
            self.__allocated_budget = new_allocated_budget
            self.__remaining_budget = new_allocated_budget
        else:
            print("Error: Allocated budget must be a non-negative number.")

    def get_remaining_budget(self):
        return self.__remaining_budget

    def add_expense(self, expense_amount):
        if isinstance(expense_amount, (int, float)) and expense_amount >= 0:
            if expense_amount <= self.__remaining_budget:
                self.__remaining_budget -= expense_amount
                print(f"Expense of ${expense_amount} added to {self.__category_name}. Remaining budget: ${self.__remaining_budget}")
            else:
                print("Error: Expense amount exceeds remaining budget.")
        else:
            print("Error: Expense amount must be a non-negative number.")

    def display_category_summary(self):
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")

# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()
