import yfinance as yf

class Stock:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    #lynch valuation
    def lynch_valuation(self):
        #fetch financials from yfinance
        growth_1y = self.ticker.get_growth_estimates().loc["+1y", "stockTrend"] * 100
        dividend_yield = self.ticker.info.get("dividendYield")
        pe_ratio = self.ticker.info.get("trailingPE")

        if growth_1y and dividend_yield and pe_ratio:
            #use lynch valuation formula
            value = round((growth_1y + dividend_yield) / pe_ratio, 2)
            str_value = "Lynch valuation is: " + str(value)

            #determine stock value
            if value < 1:
                str_value = str_value + "\nOVER VALUED"
            elif 1 <= value < 1.5:
                str_value= str_value + "\nFAIRLY VALUED"
            elif 1.5 <= value < 2:
                str_value = str_value + "\nUNDER VALUED"
            else:
                str_value = str_value + "\nVERY UNDER VALUED"
        else:
            str_value = "Lynch Valuation is not available for this stock."
        return str_value

    #price-earnings-growth valuation
    def peg_valuation(self):
        #fetch financials from yfinance
        growth_1y = self.ticker.get_growth_estimates().loc["+1y", "stockTrend"] * 100
        pe_ratio = self.ticker.info.get("trailingPE")

        #use peg valuation formula
        if growth_1y and pe_ratio:
            value = round(pe_ratio / growth_1y, 2)
            str_value = "PEG ratio is: " + str(value)

            if value < 1:
                str_value = str_value + "\nUNDER VALUED"
            elif value == 1:
                str_value= str_value + "\nFAIRLY VALUED"
            else:
                str_value = str_value + "\nOVER VALUED"
        else:
            str_value = "PEG Valuation is not available for this stock."
        return str_value

    #def dcf_model(self):

    #def benjamin_graham_model(self):

    #def multiple_valuation(self):

    #def dividend_discount(self):