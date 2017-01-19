import requests
import json
import argparse
import sys
import math
import datetime
from datetime import datetime, timedelta

# print r.text

class BookKeeper:
    SOURCE_URL = "https://2016.api.levelmoney.com/api/v2/core/get-all-transactions"
    DATA = {"args": {
                "uid": 1110590645,
                "token": "4ED35F5F77D45D3541DB3FAD6AEA2056",
                "api-token": "AppTokenForInterview",
                "json-strict-mode": False,
                "json-verbose-response": False}}
    HEADERS = {'Content-type': 'application/json',
               'Accept': 'application/json'}


    monthlyData = {}
    noDonut = False
    crystalBall = False
    noCreditCard = False
    transactions = None

    def __init__(self):
        #r = requests.post(self.SOURCE_URL, data=json.dumps(self.DATA), headers=self.HEADERS)
        f = open('source_capone.txt', 'r')
        # source_data = json.loads(r.text)
        self.transactions = json.loads(f.read())["transactions"]

    def includePredictedTransactions(self):
        now = datetime.datetime.now()
        cur_year = now.year
        cur_month = now.month

        url = "https://2016.api.levelmoney.com/api/v2/core/projected-transactions-for-month"
        data = self.DATA
        data["year"] = cur_year
        data["month"] = cur_month

        r = requests.post(url, data=json.dumps(self.DATA), headers=self.HEADERS)
        predictedTransactions = json.loads(r.text)["transactions"]
        self.transactions += predictedTransactions

    def excludeCreditCardTransactions(self):
        #assumption: transactions list is sorted by transaction-time
        cc_transactions = set([])
        index = 0
        for transaction in self.transactions[:-1]:
            transc_time = datetime.strptime(transaction["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')
            transc_id = transaction["transaction-id"]
            amount = transaction["amount"]
            neighborsDateTime = datetime.strptime(self.transactions[index+1]["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')
            while (transc_time + timedelta(hours=24) > neighborsDateTime and index < len(self.transactions)):
                neighborsDateTime = datetime.strptime(self.transactions[index]["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')
                if amount == -(self.transactions[index]["amount"]):
                    cc_transactions.add(transaction["transaction-id"])
                    cc_transactions.add(self.transactions[index]["transaction-id"])
                index += 1

        # print len(self.transactions)
        temp_new_transactions = []
        for transaction in self.transactions:
            if transaction["transaction-id"] not in cc_transactions:
                temp_new_transactions.append(transaction)

        self.transactions = temp_new_transactions
        # print len(self.transactions)

    def parseData(self):
        if self.crystalBall:
            self.includePredictedTransactions()

        if self.noCreditCard:
            self.excludeCreditCardTransactions()

        for transc in self.transactions:
            year_month = transc["transaction-time"][:7]
            if self.noDonut:
                if ("krispy kreme donuts" in transc["merchant"].lower() or
                    "dunkin #336784" in transc["merchant"].lower()):
                    continue

            if year_month not in self.monthlyData:
                self.monthlyData[year_month] = [transc]
            else:
                self.monthlyData[year_month].append(transc)


    def showMonthlyIncomeExpenditure(self):
        totalSpent = 0
        totalIncome = 0

        for ym in sorted(self.monthlyData.keys()):
            spent = 0
            income = 0
            for transc in self.monthlyData[ym]:
                #normalize from centocent to dollar
                amount = float(transc["amount"]/20000)

                if amount < 0:
                    spent += math.fabs(amount)
                else:
                    income += amount

            totalSpent += spent
            totalIncome += income
            print '{0}      spent: ${1:,.2f}        income: ${2:,.2f}'.format(ym, spent, income)

        monthCounts = len(self.monthlyData.keys())
        averageSpent = totalSpent/monthCounts
        averageIncome = totalIncome/monthCounts

        print 'average      spent: ${0:,.2f}        income: ${1:,.2f}'.format(averageSpent, averageIncome)

def main():
    #setting up 
    parser = argparse.ArgumentParser(description='Track your incomes and expenditures')
    parser.add_argument('-d', '--ignore-donuts', dest='donut', action='store_true', default=False,
                        help='I love my donuts so much that I don\'t need to include it on my budget')
    parser.add_argument('-b', '--crystal-ball', dest='crystal', action='store_true', default=False,
                        help='Turn on expenditure and income predictions for the rest of this month')
    parser.add_argument('-c', '--ignore-cc-payments', dest='nocc', action='store_true', default=False,
                        help='Ignore credit card payments')

    args = parser.parse_args()

    book = BookKeeper()

    #Default case
    if len(sys.argv) == 1:
        book.parseData()
    if args.donut:
        book.noDonut = True
    if args.crystal:
        book.crystalBall = True
    if args.nocc:
        book.noCreditCard = True

    book.parseData()
    book.showMonthlyIncomeExpenditure()
if __name__ == '__main__':
    main()
