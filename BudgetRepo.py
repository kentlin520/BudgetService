class IBudgetRepo:
    def get_all(self):
        pass


class Budget:
    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount


class BudgetRepo(IBudgetRepo):
    def __init__(self, data):
        self.data = data

    def get_all(self):
        return self.data
