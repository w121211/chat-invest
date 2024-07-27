import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)

fig = make_subplots(
    rows=2,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    subplot_titles=("AAPL Stock Price", "Volume"),
    row_width=[0.2, 0.7],
)

fig.add_trace(
    go.Candlestick(
        x=df["Date"],
        open=df["AAPL.Open"],
        high=df["AAPL.High"],
        low=df["AAPL.Low"],
        close=df["AAPL.Close"],
        name="Price",
    ),
    row=1,
    col=1,
)
fig.add_trace(go.Bar(x=df["Date"], y=df["AAPL.Volume"], showlegend=False), row=2, col=1)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["AAPL.Close"].rolling(window=20).mean(),
        name="20-Day MA",
        line=dict(color="purple", width=1),
    ),
    row=1,
    col=1,
)
fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["AAPL.Close"].rolling(window=50).mean(),
        name="50-Day MA",
        line=dict(color="blue", width=1),
    ),
    row=1,
    col=1,
)

# 添加支撐和阻力線，將線命名並在滑鼠移過時顯示詳細資訊
fig.add_shape(
    type="line",
    x0="2016-11-15",
    y0=110,
    x1="2017-01-15",
    y1=110,
    xref="x",
    yref="y",
    line=dict(color="green", width=2, dash="dash"),
    name="Long-term Support (Strong, High Volume)",
)
fig.add_shape(
    type="line",
    x0="2016-12-01",
    y0=118,
    x1="2017-01-15",
    y1=118,
    xref="x",
    yref="y",
    line=dict(color="red", width=2, dash="dash"),
    name="Short-term Resistance (Weak, Historical High)",
)

# 添加分析師和YouTuber預測點，標註在超出現價格的右側
last_date = datetime.strptime(df["Date"].iloc[-1], "%Y-%m-%d")
analyst_predict_date = last_date + timedelta(days=90)
youtuber_predict_date = last_date + timedelta(days=90)

fig.add_trace(
    go.Scatter(
        x=[analyst_predict_date],
        y=[130],
        mode="markers",
        marker=dict(size=10, color="blue"),
        name="Analyst Price Target: $130",
    )
)
fig.add_trace(
    go.Scatter(
        x=[youtuber_predict_date],
        y=[125],
        mode="markers",
        marker=dict(size=10, color="red"),
        name="YouTuber Price Prediction: $125",
    )
)

# 添加時間範圍選擇器
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1D", step="day", stepmode="backward"),
                    dict(count=5, label="5D", step="day", stepmode="backward"),
                    dict(count=3, label="3M", step="month", stepmode="backward"),
                    dict(count=6, label="6M", step="month", stepmode="backward"),
                    dict(step="all", label="All"),
                ]
            )
        ),
        rangeslider=dict(visible=False),
        type="date",
    ),
    title="AAPL Stock Price Trend Analysis",
    yaxis_title="Price",
)

fig.show()
