import yfinance as yf
from Stock import Stock

#instantiates stock and runs valuations
def main():
    stock = Stock(input_ticker())
    stock.lynch_valuation()
    stock.peg_valuation()

#get a ticker from the user
def input_ticker():
    ticker = str(input("Enter a ticker: "))
    return ticker

#call main function
if __name__ == '__main__':
    main()