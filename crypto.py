import gdax, time, json, ast, requests
import numpy as np
from datetime import datetime


def cmc():
    #pulling from coinmarketcap datatbase


    r = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=100")

    top100 = r.json()
    # top 100 coin dictionaries


    #prints #1 coin which is currently bitcoin
    print(top100[0])
    # print(top100)
    # print(type(top100))
    # print(d[0])
    # btc_dict = d[0]
    # bitcoin_price = btc_dict["price_usd"]
    # print(bitcoin_price)
    # price = float(bitcoin_price)


def historical():

    #trying to measure returns

def corr():
    #finding correlations


def xcdata(pair):
    '''
    takes in trading pair (ticker separated by hyphen)
    and returns statistics over period of trading

    '''
    public_client = gdax.PublicClient()
    prices = public_client.get_product_historic_rates('ETH-USD', granularity=60)

    time_list = []
    price_list = []
    low_list = []
    high_list = []
    open_price_list = []
    close_price_list = []
    vol_list = []

    for i in prices:
        time = i[0]
        low = i[1]
        high = i[2]
        open_price = i[3]
        close_price = i[4]
        vol = i[5]
        man_time = datetime.fromtimestamp(time).strftime("%A, %B %d, %Y %I:%M:%S")
        time_list.append(man_time)
        low_list.append(low)
        high_list.append(high)
        open_price_list.append(open_price)
        close_price_list.append(close_price)
        vol_list.append(vol_list)
    mean = np.mean(close_price_list)
    min = np.min(low_list)
    max = np.max(high_list)
    summary_stats_list = [mean, min, max, open_price_list[0], close_price_list[-1]]
    d = {}
    d["summary_stats"] = summary_stats_list
    d["closing_prices"] = close_price_list

    return d




def strat1(pair):
    output = xcdata(pair)
    [mean, min, max, first_open, last_close] = output["summary_stats"]
    close_price_list = output["closing_prices"]

    close_price_list_train = close_price_list[0:40]
    training_mean = np.mean(close_price_list_train)

    #buy one coin each time it's below training_mean

    expenditures = 0
    shares = 0

    for i in close_price_list:
        if i < training_mean:
            # buy the price
            expenditures -= i
            shares += 1
        if i > training_mean and shares > 0:
            expenditures += i
            shares -= 1
        profit = expenditures + shares * i
        # print(profit)
    #     print(expenditures)
    #     print(shares)
    # print(expenditures)
    # print(shares)

    # print(profit)
        
    #random strat
    profit = 0
    expenditures = 0
    shares = 0
    for i in range(len(close_price_list)):
        if i%2 == 0:
            expenditures -= close_price_list[i]
            shares += 1
        if i%4 == 0:
            expenditures += close_price_list[i]
            shares -= 1
        profit = expenditures + shares * close_price_list[i]
    return profit


