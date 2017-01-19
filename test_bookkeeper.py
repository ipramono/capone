import unittest
from bookkeeper import BookKeeper

class BookKeeperTestCase(unittest.TestCase):
    """Tests for `showMonthlyIncomeExpenditure.py`."""


    def testParseData(self):
        """no options given"""
        book = BookKeeper()
        transactions =   [{
      "amount": -93700,
      "is-pending": False,
      "payee-name-only-for-testing": "DAIRY QUEEN",
      "aggregation-time": 1465232460779,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465285080000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465285080000",
      "raw-merchant": "DAIRY QUEEN",
      "categorization": "Restaurants",
      "merchant": "Dairy Queen",
      "transaction-time": "2016-06-06T00:00:00.000Z"
    },
    {
      "amount": -69200,
      "is-pending": False,
      "payee-name-only-for-testing": "Krispy Kreme Donuts",
      "aggregation-time": 1465341883147,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465477800000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465477800000",
      "raw-merchant": "Krispy Kreme Donuts",
      "categorization": "Restaurants",
      "merchant": "Krispy Kreme Donuts",
      "transaction-time": "2016-06-07T00:00:00.000Z"
    }]

        expectedResult = {'2016-06': [{'merchant': 'Dairy Queen', 'aggregation-time': 1465232460779, 'is-pending': False, 'categorization': 'Restaurants', 'account-id': 'nonce:comfy-cc/hdhehe', 'memo-only-for-testing': 'Example Memo', 'transaction-id': '1465285080000', 'transaction-time': '2016-06-06T00:00:00.000Z', 'payee-name-only-for-testing': 'DAIRY QUEEN', 'amount': -93700, 'clear-date': 1465285080000, 'raw-merchant': 'DAIRY QUEEN'}, {'merchant': 'Krispy Kreme Donuts', 'aggregation-time': 1465341883147, 'is-pending': False, 'categorization': 'Restaurants', 'account-id': 'nonce:comfy-cc/hdhehe', 'memo-only-for-testing': 'Example Memo', 'transaction-id': '1465477800000', 'transaction-time': '2016-06-07T00:00:00.000Z', 'payee-name-only-for-testing': 'Krispy Kreme Donuts', 'amount': -69200, 'clear-date': 1465477800000, 'raw-merchant': 'Krispy Kreme Donuts'}]}
        self.assertEquals(expectedResult, book.parseData(transactions))

    def testParseDataCompleteFlags(self):
        """test with all flags are being on"""
        book = BookKeeper()
        book.noDonut = True
        book.crystalBall = True
        book.noCreditCard = True
        transactions =   [{
      "amount": -93700,
      "is-pending": False,
      "payee-name-only-for-testing": "DAIRY QUEEN",
      "aggregation-time": 1465232460779,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465285080000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465285080000",
      "raw-merchant": "DAIRY QUEEN",
      "categorization": "Restaurants",
      "merchant": "Dairy Queen",
      "transaction-time": "2016-06-06T00:00:00.000Z"
    },
    {
      "amount": -69200,
      "is-pending": False,
      "payee-name-only-for-testing": "Krispy Kreme Donuts",
      "aggregation-time": 1465341883147,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465477800000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465477800000",
      "raw-merchant": "Krispy Kreme Donuts",
      "categorization": "Restaurants",
      "merchant": "Krispy Kreme Donuts",
      "transaction-time": "2016-06-07T00:00:00.000Z"
    },
    {
      "amount": 5194500,
      "is-pending": False,
      "aggregation-time": 1415041080000,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1415042820000,
      "transaction-id": "1415042820000",
      "raw-merchant": "CREDIT CARD PAYMENT",
      "categorization": "Unknown",
      "merchant": "Credit Card Payment",
      "transaction-time": "2014-11-03T18:58:00.000Z"
    },
    {
      "amount": -5194500,
      "is-pending": False,
      "aggregation-time": 1415048280000,
      "account-id": "nonce:comfy-checking/hdhehe",
      "clear-date": 1415193660000,
      "transaction-id": "1415193660000",
      "raw-merchant": "CC PAYMENT",
      "categorization": "Unknown",
      "merchant": "CC Payment",
      "transaction-time": "2014-11-03T20:58:00.000Z"
    } ]
        expected_result = {'2016-06': [{'merchant': 'Dairy Queen', 'aggregation-time': 1465232460779, 'is-pending': False, 'categorization': 'Restaurants', 'account-id': 'nonce:comfy-cc/hdhehe', 'memo-only-for-testing': 'Example Memo', 'transaction-id': '1465285080000', 'transaction-time': '2016-06-06T00:00:00.000Z', 'payee-name-only-for-testing': 'DAIRY QUEEN', 'amount': -93700, 'clear-date': 1465285080000, 'raw-merchant': 'DAIRY QUEEN'}], u'2017-01': [{u'merchant': u'Zenpayroll', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.8325712314062954', u'transaction-time': u'2017-01-27T00:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'ZENPAYROLL', u'amount': 17079300, u'categorization': u'Unknown', u'clear-date': 1485689460000, u'raw-merchant': u'ZENPAYROLL'}, {u'merchant': u'Sweeneys Chevrolet', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.818332127033348', u'transaction-time': u'2017-01-26T00:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'SWEENEYS CHEVROLET', u'amount': -2418700, u'categorization': u'Unknown', u'clear-date': 1485488340000, u'raw-merchant': u'SWEENEYS CHEVROLET'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.8910651671763682', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1484965800000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.16674555265020535', u'transaction-time': u'2017-01-24T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1485544440000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.06735763018224294', u'transaction-time': u'2017-01-31T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1486031940000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 3', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.12515094980391553', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 3', u'amount': -479300, u'categorization': u'Uncategorized', u'clear-date': 1484925180000, u'raw-merchant': u'Dummy expenses for day 3'}, {u'merchant': u'Dummy Expenses For Day 3', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.1891696120520188', u'transaction-time': u'2017-01-25T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 3', u'amount': -479300, u'categorization': u'Uncategorized', u'clear-date': 1485591900000, u'raw-merchant': u'Dummy expenses for day 3'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.45186803368529105', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1484901360000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--2.483996943973294', u'transaction-time': u'2017-01-20T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1485143400000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.3869597917926635', u'transaction-time': u'2017-01-27T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1485518100000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:cleared-0.8558761614990683', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1484810340000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.1115747443769767', u'transaction-time': u'2017-01-21T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1485125160000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.8339116613291794', u'transaction-time': u'2017-01-28T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1485632760000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.5571932770640157', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485064620000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.23739693581063898', u'transaction-time': u'2017-01-22T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485330660000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.063737292086206', u'transaction-time': u'2017-01-29T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485843720000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 4', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.8839204194852146', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 4', u'amount': -460100, u'categorization': u'Uncategorized', u'clear-date': 1484864700000, u'raw-merchant': u'Dummy expenses for day 4'}, {u'merchant': u'Dummy Expenses For Day 4', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.873027648483336', u'transaction-time': u'2017-01-26T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 4', u'amount': -460100, u'categorization': u'Uncategorized', u'clear-date': 1485534720000, u'raw-merchant': u'Dummy expenses for day 4'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.07525591322435127', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1484843100000, u'raw-merchant': u'Dummy expenses for day 1'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.493171309925633', u'transaction-time': u'2017-01-23T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1485294540000, u'raw-merchant': u'Dummy expenses for day 1'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--1.3321908197061576', u'transaction-time': u'2017-01-30T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1486013700000, u'raw-merchant': u'Dummy expenses for day 1'}]}
        res = book.parseData(transactions)
        self.assertEquals(expected_result, res)

    def testNoDonut(self):
        """test no donut feature"""
        book = BookKeeper()
        book.noDonut = True
        transactions =   [{
      "amount": -93700,
      "is-pending": False,
      "payee-name-only-for-testing": "DAIRY QUEEN",
      "aggregation-time": 1465232460779,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465285080000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465285080000",
      "raw-merchant": "DAIRY QUEEN",
      "categorization": "Restaurants",
      "merchant": "Dairy Queen",
      "transaction-time": "2016-06-06T00:00:00.000Z"
    },
    {
      "amount": -69200,
      "is-pending": False,
      "payee-name-only-for-testing": "Krispy Kreme Donuts",
      "aggregation-time": 1465341883147,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1465477800000,
      "memo-only-for-testing": "Example Memo",
      "transaction-id": "1465477800000",
      "raw-merchant": "Krispy Kreme Donuts",
      "categorization": "Restaurants",
      "merchant": "Krispy Kreme Donuts",
      "transaction-time": "2016-06-07T00:00:00.000Z"
    }]
        #expected result should not have donut's transaction"
        expectedResult = {'2016-06': [{'merchant': 'Dairy Queen', 'aggregation-time': 1465232460779, 'is-pending': False, 'categorization': 'Restaurants', 'account-id': 'nonce:comfy-cc/hdhehe', 'memo-only-for-testing': 'Example Memo', 'transaction-id': '1465285080000', 'transaction-time': '2016-06-06T00:00:00.000Z', 'payee-name-only-for-testing': 'DAIRY QUEEN', 'amount': -93700, 'clear-date': 1465285080000, 'raw-merchant': 'DAIRY QUEEN'}]}
        self.assertEquals(expectedResult, book.parseData(transactions))


    def testIncludePredictedTransactions(self):
        """test include predicted transactions"""
        book = BookKeeper()
        transactions = []
        res = book.includePredictedTransactions(transactions)
        expectedResult = [{u'merchant': u'Zenpayroll', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.8325712314062954', u'transaction-time': u'2017-01-27T00:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'ZENPAYROLL', u'amount': 17079300, u'categorization': u'Unknown', u'clear-date': 1485689460000, u'raw-merchant': u'ZENPAYROLL'}, {u'merchant': u'Sweeneys Chevrolet', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.818332127033348', u'transaction-time': u'2017-01-26T00:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'SWEENEYS CHEVROLET', u'amount': -2418700, u'categorization': u'Unknown', u'clear-date': 1485488340000, u'raw-merchant': u'SWEENEYS CHEVROLET'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.8910651671763682', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1484965800000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.16674555265020535', u'transaction-time': u'2017-01-24T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1485544440000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 2', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.06735763018224294', u'transaction-time': u'2017-01-31T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 2', u'amount': -422000, u'categorization': u'Uncategorized', u'clear-date': 1486031940000, u'raw-merchant': u'Dummy expenses for day 2'}, {u'merchant': u'Dummy Expenses For Day 3', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.12515094980391553', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 3', u'amount': -479300, u'categorization': u'Uncategorized', u'clear-date': 1484925180000, u'raw-merchant': u'Dummy expenses for day 3'}, {u'merchant': u'Dummy Expenses For Day 3', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.1891696120520188', u'transaction-time': u'2017-01-25T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 3', u'amount': -479300, u'categorization': u'Uncategorized', u'clear-date': 1485591900000, u'raw-merchant': u'Dummy expenses for day 3'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.45186803368529105', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1484901360000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--2.483996943973294', u'transaction-time': u'2017-01-20T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1485143400000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 5', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.3869597917926635', u'transaction-time': u'2017-01-27T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 5', u'amount': -537700, u'categorization': u'Uncategorized', u'clear-date': 1485518100000, u'raw-merchant': u'Dummy expenses for day 5'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:cleared-0.8558761614990683', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1484810340000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.1115747443769767', u'transaction-time': u'2017-01-21T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1485125160000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 6', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.8339116613291794', u'transaction-time': u'2017-01-28T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 6', u'amount': -384200, u'categorization': u'Uncategorized', u'clear-date': 1485632760000, u'raw-merchant': u'Dummy expenses for day 6'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.5571932770640157', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485064620000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.23739693581063898', u'transaction-time': u'2017-01-22T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485330660000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 7', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.063737292086206', u'transaction-time': u'2017-01-29T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 7', u'amount': -419300, u'categorization': u'Uncategorized', u'clear-date': 1485843720000, u'raw-merchant': u'Dummy expenses for day 7'}, {u'merchant': u'Dummy Expenses For Day 4', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-1.8839204194852146', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 4', u'amount': -460100, u'categorization': u'Uncategorized', u'clear-date': 1484864700000, u'raw-merchant': u'Dummy expenses for day 4'}, {u'merchant': u'Dummy Expenses For Day 4', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.873027648483336', u'transaction-time': u'2017-01-26T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 4', u'amount': -460100, u'categorization': u'Uncategorized', u'clear-date': 1485534720000, u'raw-merchant': u'Dummy expenses for day 4'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending-0.07525591322435127', u'transaction-time': u'2017-01-19T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1484843100000, u'raw-merchant': u'Dummy expenses for day 1'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--0.493171309925633', u'transaction-time': u'2017-01-23T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1485294540000, u'raw-merchant': u'Dummy expenses for day 1'}, {u'merchant': u'Dummy Expenses For Day 1', u'account-id': u'nonce:comfy-cc/hdhehe', u'aggregation-time': 189302400000, u'memo-only-for-testing': u'Example Memo', u'transaction-id': u'pending:pending--1.3321908197061576', u'transaction-time': u'2017-01-30T07:00:00.000Z', u'is-pending': True, u'payee-name-only-for-testing': u'Dummy expenses for day 1', u'amount': -454300, u'categorization': u'Uncategorized', u'clear-date': 1486013700000, u'raw-merchant': u'Dummy expenses for day 1'}]
        self.assertEquals(expectedResult, res)

    def testExcludeCreditCardTransactions(self):
        """test exclude credit card transactions"""
        book = BookKeeper()
        transactions = [{
      "amount": -99900,
      "is-pending": False,
      "aggregation-time": 1414995900000,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1415023140000,
      "transaction-id": "1415023140000",
      "raw-merchant": "Spotify.com",
      "categorization": "Unknown",
      "merchant": "Spotify.com",
      "transaction-time": "2014-11-03T06:25:00.000Z"
    },
    {
      "amount": 5194500,
      "is-pending": False,
      "aggregation-time": 1415041080000,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1415042820000,
      "transaction-id": "1415042820000",
      "raw-merchant": "CREDIT CARD PAYMENT",
      "categorization": "Unknown",
      "merchant": "Credit Card Payment",
      "transaction-time": "2014-11-03T18:58:00.000Z"
    },
    {
      "amount": -5194500,
      "is-pending": False,
      "aggregation-time": 1415048280000,
      "account-id": "nonce:comfy-checking/hdhehe",
      "clear-date": 1415193660000,
      "transaction-id": "1415193660000",
      "raw-merchant": "CC PAYMENT",
      "categorization": "Unknown",
      "merchant": "CC Payment",
      "transaction-time": "2014-11-03T20:58:00.000Z"
    }]
        res = book.excludeCreditCardTransactions(transactions)
        expectedResult = [{
      "amount": -99900,
      "is-pending": False,
      "aggregation-time": 1414995900000,
      "account-id": "nonce:comfy-cc/hdhehe",
      "clear-date": 1415023140000,
      "transaction-id": "1415023140000",
      "raw-merchant": "Spotify.com",
      "categorization": "Unknown",
      "merchant": "Spotify.com",
      "transaction-time": "2014-11-03T06:25:00.000Z"
    }]
        self.maxDiff = None
        self.assertEquals(expectedResult, res)

if __name__ == '__main__':
    unittest.main()
