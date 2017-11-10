import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')
import simplejson
import requests


query=input("Enter company name:")
yahoo_stock_code="http://d.yimg.com/autoc.finance.yahoo.com/autoc?query="
yahoo_excess_code="&region=1&lang=en"
stock_url=yahoo_stock_code+query+yahoo_excess_code
response=requests.get(stock_url)

#CONEVRT THE JSON FILE INTO UTF-8 FORMAT FOR PARSING
data=simplejson.loads(response.content.decode("utf-8"))

#FETCH THE FIRST COMPANY CODE
code=data['ResultSet']['Result'][0]['symbol']
print(code)


start=dt.datetime(2010,1,1)
end=dt.datetime(2016,12,31)

df=web.DataReader(code,'yahoo',start,end)
#df.to_csv('google')

#df=pd.read_csv('google.csv',parse_dates=True, index_col=0)
print(df.head())

#df.plot()
#plt.show()

