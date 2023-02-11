import calendar

from BudgetRepo import Budget


class BudgetService:
    def __init__(self, repo):
        self.all_amount = repo.get_all()

    def query(self, start, end):
        s_day, s_month, s_year = self.get_month_day(start)
        e_day, e_month, e_year = self.get_month_day(end)
        if s_year == e_year and s_month == e_month:
            year_month = start.strftime('%Y%m')
            if s_day == 1 and self.is_end_date(end):
                return self.get_one_month_amount(year_month).amount
            else:
                return self.get_one_day_amount(year_month, start) * ((end - start).days + 1)


    def is_end_date(self, date):
        day, _, _ = self.get_month_day(date)
        return day == self.get_number_of_day(date)

    def get_number_of_day(self, year_month):
        day, month, year = self.get_month_day(year_month)
        _, number = calendar.monthrange(year, month)
        return number

    def get_month_day(self, year_month):
        year = int(str(year_month.strftime('%Y')))
        month = int(str(year_month.strftime('%m')))
        day = int(str(year_month.strftime('%d')))
        return day, month, year

    def get_one_month_amount(self, year_month):
        return self.all_amount.get(year_month, Budget('', 0))

    def get_one_day_amount(self, year_month, date):
        one_month_amount = self.get_one_month_amount(year_month).amount
        number_days = self.get_number_of_day(date)
        one_day_amount = int(one_month_amount / number_days)
        return one_day_amount


