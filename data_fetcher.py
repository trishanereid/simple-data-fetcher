import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

st.title("Stock Data Fetcher")

symbol = st.text_input(label="Symbol", placeholder="NVDA")
range = st.selectbox("range:", ("1mo", "1y"), )


def display_info():
    stock_data = yf.Ticker(symbol).info
    st.write(f"Company Name: {stock_data['longName']}")
    st.write(f"Industry: {stock_data['industry']}")
    st.write(f"Sector: {stock_data['sector']}")
    
    st.write(f"Full-time Employees: {stock_data['fullTimeEmployees']:,}")
    st.write(f"Current Price: ${stock_data['currentPrice']:,.2f}")
    st.write(f"Market Cap: ${stock_data['marketCap']:,.0f}")

def search_stock_data():
    display_info()
    
    stock_data = yf.Ticker(symbol)
    hist = stock_data.history(period=range)
    
    fig = go.Figure(data=[go.Candlestick(x=hist.index,
                                         open=hist['Open'],
                                         high=hist['High'],
                                         low=hist['Low'],
                                         close=hist['Close'])])
    st.plotly_chart(fig)



if st.button("Search"):
    search_stock_data()


