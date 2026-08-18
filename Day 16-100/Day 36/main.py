import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY= "9ZJ1QFUVHQ3ZWQ5R"
NEWS_API_KEY= "87653d3a99d94e8f8632fc20670c65cd"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_clothing_price = yesterday_data["4. close"]
print(yesterday_clothing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_clothing_price = day_before_yesterday["4. close"]
print(day_before_yesterday_clothing_price)
difference = abs(float(yesterday_clothing_price) - float(day_before_yesterday_clothing_price))
diff_percent = (difference/float(yesterday_clothing_price))*100
print(diff_percent)

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if diff_percent > 0:
    news_param = {
        "apikey":"87653d3a99d94e8f8632fc20670c65cd",
        "qInTitle":COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_param)
    articles = news_response.json()['articles']

three_articles= articles[:3]
print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python COULDN'T DO IT BECAUSE THERE IS NO FREE TRIAL IN TWILIO
    #to send a separate message with each article's title and description to your phone number. 

