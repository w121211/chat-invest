import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


# 設置頁面標題
st.set_page_config(page_title="股票分析")

st.markdown("# NVIDIA Corporation [$NVDA](http://example.com/nvda)")


# 繪製股票價格走勢圖
data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)
fig = go.Figure()
fig.add_trace(go.Scatter(x=data["Date"], y=data["AAPL.Close"], mode="lines"))
fig.update_layout(xaxis_title="日期", yaxis_title="價格", height=500)
st.plotly_chart(fig, use_container_width=True)


markdown_content = """
---

### 📈 當前走勢

目前XXX股票呈現出明顯的上升趨勢,日線圖顯示連續5天收紅,成交量也不斷放大。短期內有望突破前期高點,關注50元附近的阻力位。

#### 🤔 現在適合進場嗎？

...

[Source1](http://example.com/source1)  
[Source2](http://example.com/source2)  
[Source3](http://example.com/source3)  ...

#### 🤔 突破50元阻力位後,下一個目標位在哪裡?

根據當前的趨勢和成交量,如果能夠有效突破50元阻力位,下一個目標位可能在55-60元區間。但需要關注大盤的整體走勢,以及公司基本面的變化。

[Source1](http://example.com/source1)  
[Source2](http://example.com/source2)  
[Source3](http://example.com/source3)

#### 🤔 如果無法突破阻力位,是否會有較大的回調風險?

如果XXX股票在50元附近遇阻,確實存在回調的風險。投資者需要密切關注成交量的變化,如果放量無法突破,則可能引發獲利了結的賣壓。短期支撐位在45元附近,跌破該位置可能會進一步下探。

[Source1](http://example.com/source1) [Source2](http://example.com/source2) [Source3](http://example.com/source3)

---

## 💹 多空觀點

### 多方對XXX股票的看法是什麼?

多方認為XXX股票基本面良好,業績持續增長,市場份額不斷擴大。技術面上已經突破了前期的箱體,未來有望繼續上漲。

[Source1](http://example.com/source1) [Source2](http://example.com/source2) [Source3](http://example.com/source3)

### 空方對XXX股票有哪些擔憂?

空方認為XXX股票目前的估值已經較高,市盈率遠高於行業平均水準。同時,公司面臨激烈的市場競爭,毛利率有下降的風險。

[Source1](http://example.com/source1) [Source2](http://example.com/source2) [Source3](http://example.com/source3)

#### ⤷ 面對市場競爭,XXX公司有哪些應對措施?

XXX公司正在加大研發投入,推出新產品和服務,以應對市場競爭。同時,公司也在優化成本結構,提高運營效率,以維持毛利率水準。這些措施有望在未來幾個季度內取得成效。

[Source1](http://example.com/source1) [Source2](http://example.com/source2) [Source3](http://example.com/source3)

---

## 🕐 進場時機

### 問題1: 現在是否適合買入XXX股票?

從技術面來看,XXX股票目前處於上升通道中,MACD指標也顯示出買入信號。但考慮到近期大盤的波動,建議分批買入,可以在回調時逢低吸納。

### 問題2: XXX股票是否存在進一步下跌的風險?

雖然XXX股票目前走勢較強,但如果大盤出現明顯調整,仍有可能面臨下跌風險。建議關注60日均線的支撐,如果跌破該均線,可能引發進一步下跌。

## 數據來源

[Source1](http://example.com/source1) [Source2](http://example.com/source2) [Source3](http://example.com/source3)
"""

# 在 Streamlit 中呈現 Markdown 內容
st.markdown(markdown_content)
