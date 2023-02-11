from BudgetRepo import Budget


class BudgetService:
    def __init__(self, repo):
        self.all_amount = repo.get_all()

    def query(self, start, end):
        year_month = start.strftime('%Y%m')
        return self.get_one_month_amount(year_month).amount

    def get_one_month_amount(self, year_month):
        return self.all_amount.get(year_month, Budget('', 0))
