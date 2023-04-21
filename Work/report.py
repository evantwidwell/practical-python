# report.py
import csv


def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                 'name'   : row[0],
                 'shares' : int(row[1]),
                 'price'   : float(row[2])
            }
            portfolio.append(stock)

    return portfolio


def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


portfolio = read_portfolio('./Data/portfolio.csv')
prices = read_prices('./Data/prices.csv')


# Calculate the total cost of the portfolio
def total_cost(p):
    total_cost = 0.0
    for s in p:
        total_cost += s['shares']*s['price']
    return total_cost


# Compute the current value of the portfolio
def current_value(p, cost):
    total_value = 0.0
    for s in p:
        total_value += s['shares']*prices[s['name']]

    print('Current value', total_value)
    print('Gain', total_value - cost)
    

def print_report(port):
    tcost = total_cost(port)
    print('Total cost', tcost)
    current_value(port, tcost)



