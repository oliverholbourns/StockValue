import tkinter as tk
from Stock import Stock

class GUI:
    def __init__(self):
        self.root = tk.Tk()

        #update window information
        self.root.title("StockValue")
        self.root.minsize(600, 300)

        #create label, entry and button
        tk.Label(self.root, text="Ticker").grid(row=0, column=0)
        self.e1 = tk.Entry(self.root)
        self.e1.grid(row=0, column=1)
        tk.Button(self.root, text="Search", command=lambda: self.search_ticker(self.e1.get())).grid(row=0, column=2)

        #create a text box
        self.t1 = tk.Text(self.root, width = 52, height = 10)
        self.t1.grid(row=1, column=0, columnspan=3)

    def main(self):
        self.root.mainloop()

    #instantiates stock and runs valuations
    def search_ticker(self, input_ticker):
        if input_ticker != "":
            #clear text box
            self.t1.delete(1.0, tk.END)
            text = ""

            #store valuations in string
            stock = Stock(input_ticker)
            text = text + stock.lynch_valuation()
            text = text + "\n" + stock.peg_valuation()
            self.update_ticker_value(text)

    #update the text box containing the stock evaluation
    def update_ticker_value(self, text):
        self.t1.insert(tk.END, text)