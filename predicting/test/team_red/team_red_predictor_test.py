'''
Created on 23.11.2017

Module for testing of predicting components

@author: jtymoszuk
'''
import unittest
from model.CompanyEnum import CompanyEnum
from definitions import PERIOD_1
from utils import read_stock_market_data
from predicting.predictor.team_red.team_red_predictor import TeamRedStockAPredictor

class TeamRedPredictorTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStockANnPredictor(self):
        # Get stock A data
        stock_market_data = read_stock_market_data([CompanyEnum.COMPANY_A], [PERIOD_1])
        stock_data = stock_market_data.get_for_company(CompanyEnum.COMPANY_A)

        # Load stock A predictor
        predictor = TeamRedStockAPredictor()

        # Check prediction
        stock_prediction = predictor.doPredict(stock_data)
        self.assertEqual(stock_prediction, 0.0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TeamRedPredictorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)      