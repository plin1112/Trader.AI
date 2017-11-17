'''
Created on 09.11.2017

Module for testing of all predicting components

@author: rmueller
'''
import unittest
from predicting.predictor.nn_predictor import StockANnPredictor
from predicting.predictor.nn_predictor import StockBNnPredictor
from model.CompanyEnum import CompanyEnum
from utils import read_stock_market_data_conveniently

class NnPredictorTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
       
    def testStockANnPredictor(self):
        # Get stock A data
        stock_market_data = read_stock_market_data_conveniently([CompanyEnum.COMPANY_A], ['1962-2011'])
        stock_data = stock_market_data.get_stock_data_for_company(CompanyEnum.COMPANY_A)

        # Load stock A predictor
        predictor = StockANnPredictor()

        # Check that prediction is within 10% of the most recent stock value
        stock_value = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_A)
        self.assertGreaterEqual(predictor.doPredict(stock_data), stock_value * 0.9)
        self.assertLessEqual(predictor.doPredict(stock_data), stock_value * 1.1)

    def testStockBNnPredictor(self):
        # Get stock B data
        stock_market_data = read_stock_market_data_conveniently([CompanyEnum.COMPANY_B], ['1962-2011'])
        stock_data = stock_market_data.get_stock_data_for_company(CompanyEnum.COMPANY_B)

        # Load stock B predictor
        predictor = StockBNnPredictor()

        # Check that prediction is within 10% of the most recent stock value
        stock_value = stock_market_data.get_most_recent_price(CompanyEnum.COMPANY_B)
        self.assertGreaterEqual(predictor.doPredict(stock_data), stock_value * 0.9)
        self.assertLessEqual(predictor.doPredict(stock_data), stock_value * 1.1)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(NnPredictorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)