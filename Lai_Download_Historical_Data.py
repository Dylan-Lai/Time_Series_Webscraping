import yfinance as yf
import datetime
# Create Ticker variables
goog = yf.Ticker("GOOGL")
#Set the time range
goog_hist = goog.history(start=datetime.datetime(2010, 1, 1),end=datetime.datetime.today())

goog_hist.to_csv('Lai_Historical_Data.csv', index=True)