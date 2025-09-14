import yfinance as yf
from Stock import Stock

def main():
    stock = Stock(input_ticker())
    stock.lynch_valuation()
    stock.peg_valuation()

def input_ticker():
    ticker = str(input("Enter a ticker: "))
    return ticker

if __name__ == '__main__':
    main()