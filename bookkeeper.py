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


    noDonut = False
    crystalBall = False
    noCreditCard = False
    transactions = None

    def __init__(self):
        r = requests.post(self.SOURCE_URL, data=json.dumps(self.DATA), headers=self.HEADERS)
        #f = open('source_capone.txt', 'r')
        # source_data = json.loads(r.text)
        # self.transactions = json.loads(f.read())["transactions"]
        self.transactions = json.loads(r.text)["transactions"]

    def includePredictedTransactions(self, transactions):
        now = datetime.now()
        cur_year = now.year
        cur_month = now.month

        url = "https://2016.api.levelmoney.com/api/v2/core/projected-transactions-for-month"
        data = self.DATA
        data["year"] = cur_year
        data["month"] = cur_month

        r = requests.post(url, data=json.dumps(self.DATA), headers=self.HEADERS)
        predictedTransactions = json.loads(r.text)["transactions"]
        for p in predictedTransactions:
            transactions.append(p)

        return transactions

    def excludeCreditCardTransactions(self, transactions):
        #assumption: transactions list is sorted by transaction-time
        cc_transactions = set([])
        ts = transactions
        index = 0
        for transaction in ts:
            transc_time = datetime.strptime(transaction["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')
            transc_id = transaction["transaction-id"]
            amount = transaction["amount"]

            next_index = index+1
            if next_index >= len(ts):
                break
            nextDateTime = datetime.strptime(ts[next_index]["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')
            while (transc_time + timedelta(hours=24) > nextDateTime and next_index < len(transactions)):
                if amount == -(transactions[next_index]["amount"]):
                    cc_transactions.add(transaction["transaction-id"])
                    cc_transactions.add(transactions[next_index]["transaction-id"])
                    break

                next_index += 1
                if next_index >= len(ts):
                    break
                nextDateTime = datetime.strptime(ts[next_index]["transaction-time"],'%Y-%m-%dT%H:%M:%S.%fZ')

            index+=1

        temp_new_transactions = []
        for transaction in ts:
            if transaction["transaction-id"] not in cc_transactions:
                temp_new_transactions.append(transaction)
            else:
                print 'transaction id:{0}, merchant:{1}'.format(transaction["transaction-id"], transaction["merchant"])



        ts = temp_new_transactions

        return ts
        # print len(self.transactions)

    def parseData(self, transactions):
        monthlyMap = {}
        ts = transactions

        if self.crystalBall:
            ts = self.includePredictedTransactions(ts)

        if self.noCreditCard:
            ts = self.excludeCreditCardTransactions(ts)

        for t in ts:
            year_month = t["transaction-time"][:7]
            if self.noDonut:
                if ("krispy kreme donuts" in t["merchant"].lower() or
                    "dunkin #336784" in t["merchant"].lower()):
                    continue

            if year_month not in monthlyMap:
                monthlyMap[year_month] = [t]
            else:
                monthlyMap[year_month].append(t)

        return monthlyMap


    def showMonthlyIncomeExpenditure(self, monthlyData):
        totalSpent = 0
        totalIncome = 0

        for ym in sorted(monthlyData.keys()):
            spent = 0
            income = 0
            for transc in monthlyData[ym]:
                #normalize from centocent to dollar
                amount = float(transc["amount"]/20000)

                if amount < 0:
                    spent += math.fabs(amount)
                else:
                    income += amount

            totalSpent += spent
            totalIncome += income
            print '{0}      spent: ${1:,.2f}        income: ${2:,.2f}'.format(ym, spent, income)

        monthCounts = len(monthlyData.keys())
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
    # if len(sys.argv) == 1:
    #     book.parseData()
    if args.donut:
        book.noDonut = True
    if args.crystal:
        book.crystalBall = True
    if args.nocc:
        book.noCreditCard = True

    mmap = book.parseData(book.transactions)
    book.showMonthlyIncomeExpenditure(mmap)
if __name__ == '__main__':
    main()
