











import yfinance as yf
import pandas as pd
stock_names=['BHARTIARTL.NS',"SBIN.NS","DRREDDY.NS","GSPL.NS","JSWSTEEL.NS","JSWENERGY.BO","RELIANCE.NS","YESBANK.NS","TATAMOTORS.NS","LAURUSLABS.NS","NTPC.NS","SAIL.BO"]
stocks=None
for stock in range(len(stock_names)):
    df=yf.download(stock_names[stock], start="2015-01-01", end="2023-01-01") 
    df["stock"]=stock_names[stock]
    df["Difference"]=df["Close"]-df["Open"]
    df=df.drop("Adj Close",axis=1)
    if stock!=0:
        stocks=pd.concat([stocks,df])
    else:
        stocks=df
stocks=stocks.sort_index()        
stocks=stocks.reset_index(drop=False) 

amount=100000
profit=0 
dates=sorted(set(stocks["Date"])) 


selected_stocks=[]
stock_history=pd.DataFrame({"Date":[],"Name of the stocks":[],"Transaction Price":[],"Event(Sell/Buy)":[],"Total Units":[]}) 

every_stock_history={}
for value in stock_names:
    every_stock_history[value]={"previous_price":0,"no_of_stocks":0,"previous_total_amount":0}    


def buy_at_opening(stock_name,date,opening_price,closing_price,volume,stocks_to_sold_evening):
    history_row={"Date":[],"Name of the stocks":[],"Transaction Price":[],"Event(Sell/Buy)":[],"Total Units":[]}
    no_of_stocks=20000000
    global amount
    global stock_history 
#     if volume<no_of_stocks:
#         no_of_stocks=volume
    
    amount_to_spend=no_of_stocks*opening_price 
    
    amount_we_get=(no_of_stocks * closing_price)*0.95
    
    if amount_to_spend < amount and amount_we_get > amount_to_spend:
       
        amount-=amount_to_spend 
        
        history_row["Date"].append(date)
        history_row["Name of the stocks"].append(stock_name)
        history_row["Transaction Price"].append(opening_price) 
        history_row["Event(Sell/Buy)"].append("BUY")
        history_row["Total Units"].append(no_of_stocks)  
        
        every_stock_history[stock_name]["previous_price"]=opening_price 
        every_stock_history[stock_name]["no_of_stocks"]=no_of_stocks 
        every_stock_history[stock_name]["previous_total_amount"]=amount_to_spend
        stock_history=pd.concat([stock_history,pd.DataFrame(history_row)]) 
        stocks_to_sold_evening.append(stock_name) 
    elif amount_to_spend > amount:
        max_stocks_we_can_buy = amount // opening_price 
        if max_stocks_we_can_buy<=0:
            return 
        amount_to_spend = max_stocks_we_can_buy * opening_price 
        amount_we_get= (max_stocks_we_can_buy* closing_price)*0.95 
        if amount_we_get > amount_to_spend:
           
            amount-=amount_to_spend 
            
           
            history_row["Date"].append(date)
            history_row["Name of the stocks"].append(stock_name)
            history_row["Transaction Price"].append(opening_price) 
            history_row["Event(Sell/Buy)"].append("BUY")
            history_row["Total Units"].append(max_stocks_we_can_buy)  

            every_stock_history[stock_name]["previous_price"]=opening_price 
            every_stock_history[stock_name]["no_of_stocks"]=max_stocks_we_can_buy 
            every_stock_history[stock_name]["previous_total_amount"]=amount_to_spend
            stock_history=pd.concat([stock_history,pd.DataFrame(history_row)]) 
            stocks_to_sold_evening.append(stock_name) 
    
def sell_at_evening(stock_name,date,opening_price,closing_price,volume,stocks_to_sold_evening): 
    global amount 
    global stock_history 
    history_row={"Date":[],"Name of the stocks":[],"Transaction Price":[],"Event(Sell/Buy)":[],"Total Units":[]}
    current_stock_history=every_stock_history[stock_name] 
    sold_price=(current_stock_history["no_of_stocks"]*closing_price)*0.95
#     print(amount,end=" ")
    amount+=sold_price
    history_row["Date"].append(date)
    history_row["Name of the stocks"].append(stock_name)
    history_row["Transaction Price"].append("Close") 
    history_row["Event(Sell/Buy)"].append("SELL")
    history_row["Total Units"].append(current_stock_history["no_of_stocks"]) 
    stock_history=pd.concat([stock_history,pd.DataFrame(history_row)]) 
    stocks_to_sold_evening.remove(stock_name)
    every_stock_history[stock_name]["previous_price"]=0
    every_stock_history[stock_name]["no_of_stocks"]=0
    every_stock_history[stock_name]["previous_total_amount"]=0


    
for value in stock_names:
    every_stock_history[value]={"previous_price":0,"no_of_stocks":0}
# print(every_stock_history)   
template={"Date":[],"Name of the stocks":[],"Transaction Price":[],"Event(Sell/Buy)":[],"Total Units":[]}
for date in dates:
    stocks_on_date=stocks[stocks["Date"]==date]
    stocks_on_date=stocks_on_date.sort_values("Difference",ascending=False)
    # print(stocks_on_date)
    stocks_to_sold_evening=[]
    stocks_left_with_out_buying_at_opening=[]
    for stock in range(len(stocks_on_date)):
        stock=stocks_on_date.iloc[stock] 
        opening_price=stock["Open"]
        closing_price=stock["Close"]
        volume=stock["Volume"]
        stock_name=stock["stock"]
        if opening_price<closing_price:
            buy_at_opening(stock_name,date,opening_price,closing_price,volume,stocks_to_sold_evening)
        elif closing_price<opening_price:
            stocks_left_with_out_buying_at_opening.append(stock_name)
            
    for stock in range(len(stocks_on_date)):
        stock=stocks_on_date.iloc[stock] 
        opening_price=stock["Open"]
        closing_price=stock["Close"]
        volume=stock["Volume"]
        stock_name=stock["stock"]
        if stock_name in stocks_to_sold_evening:
            sell_at_evening(stock_name,date,opening_price,closing_price,volume,stocks_to_sold_evening)
    print("Amount After Every Day:",amount,date)        

print(amount-100000)
stock_history.to_csv("stock_history2.csv",index=False)







    






