import yfinance as yf
import streamlit as st
import time

st.title("Stock Watcher")

st.write("""Type in a ticker below""")

ticker = st.text_input("Ticker", "AMZN")

submitted = st.button("Get Quote")

if submitted:
    price_history_vol = yf.Ticker(ticker).history(period='5y',  # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                                                  interval='1wk',
                                                  # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                                                  actions=False)
    price_history_vol = price_history_vol.reset_index(drop=False)
    price_history_vol = price_history_vol.drop(['Open', 'High', 'Low'], axis=1)
    price_history = price_history_vol.drop('Volume', axis=1)

    print(price_history.iloc[0]['Date'])

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = price_history.iloc[0]

    print(last_rows['Date'], last_rows['Close'], 'hi')
    chart = st.line_chart(price_history.iloc[[0]], x='Date', y='Close')
    # chart = st.line_chart(price_history.iloc[0:100], x='Date', y='Close')

    for i in range(1, len(price_history) - 1):
        per_complete = (i / (len(price_history) - 1))
        chart.line_chart(price_history.iloc[0:i], x='Date', y='Close')
        status_text.text("%i%% Complete" % (per_complete * 100))
        progress_bar.progress(per_complete)
        time.sleep(0.01)
    progress_bar.empty()






