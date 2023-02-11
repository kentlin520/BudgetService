import datetime
import unittest

from BudgetRepo import BudgetRepo, Budget
from BudgetService import BudgetService


class MyTestCase(unittest.TestCase):
    def test_all_month(self):
        data = {
            '202301': Budget('202301', 31000),
            '202302': Budget('202302', 31000),
            '202303': Budget('202303', 31000),
            '202304': Budget('202304', 30000),
            '202305': Budget('202305', 31000),
        }
        budget_repo = BudgetRepo(data)
        budget_service = BudgetService(budget_repo)
        start = datetime.datetime(2023, 4, 1)
        end = datetime.datetime(2023, 4, 30)
        self.assertEqual(30000, budget_service.query(start, end))

    def test_oneday_amount(self):
        data = {
            '202305': Budget('202305', 31000),
        }
        budget_repo = BudgetRepo(data)
        budget_service = BudgetService(budget_repo)
        start = datetime.datetime(2023, 5, 1)
        end = datetime.datetime(2023, 5, 1)
        self.assertEqual(1000, budget_service.query(start, end))

    def test_days_amount(self):
        data = {
            '202305': Budget('202305', 31000),
        }
        budget_repo = BudgetRepo(data)
        budget_service = BudgetService(budget_repo)
        start = datetime.datetime(2023, 5, 1)
        end = datetime.datetime(2023, 5, 3)
        self.assertEqual(3000, budget_service.query(start, end))


if __name__ == '__main__':
    unittest.main()
