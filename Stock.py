import yfinance as yf

class Stock:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def lynch_valuation(self):
        growth_1y = self.ticker.get_growth_estimates().loc["+1y", "stockTrend"] * 100
        dividend_yield = self.ticker.info.get("dividendYield")
        pe_ratio = self.ticker.info.get("trailingPE")

        if growth_1y and dividend_yield and pe_ratio:
            value = round((growth_1y + dividend_yield) / pe_ratio, 2)
            print("Lynch valuation is: ", value)

            if value < 1:
                print("OVER VALUED")
            elif 1 <= value < 1.5:
                print("FAIRLY VALUED")
            elif 1.5 <= value < 2:
                print("UNDER VALUED")
            else:
                print("VERY UNDER VALUED")
        else:
            print("Lynch Valuation is not available for this stock.")

    def peg_valuation(self):
        growth_1y = self.ticker.get_growth_estimates().loc["+1y", "stockTrend"] * 100
        pe_ratio = self.ticker.info.get("trailingPE")

        if growth_1y and pe_ratio:
            value = round(pe_ratio / growth_1y, 2)
            print("PEG ratio is: ", value)

            if value < 1:
                print("UNDER VALUED")
            elif value == 1:
                print("FAIRLY VALUED")
            else:
                print("OVER VALUED")
        else:
            print("PEG valuation is not available for this stock.")

    #def dcf_model(self):

    #def benjamin_graham_model(self):

    #def multiple_valuation(self):

    #def dividend_discount(self):