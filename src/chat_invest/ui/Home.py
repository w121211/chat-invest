import streamlit as st

# 設置頁面標題
st.set_page_config(page_title="股票分析主頁")


# 在標題和搜索區域之間添加空間
st.markdown(
    """
### 搜尋股票大小事

""",
    unsafe_allow_html=True,
)


# 搜索區域
search_container = st.container()

with search_container:
    col1, col2 = st.columns([4, 1])

    # 搜索欄位
    with col1:
        query = st.text_input(
            "輸入股票代號名稱",
            key="search_query",
            label_visibility="collapsed",
            placeholder="輸入股票代號、名稱",
        )

    # 提交按鈕
    with col2:
        search_button = st.button("搜索")

    # 搜索示例
    st.markdown(
        """例如

- 2330
- 台積電 
- 2330 現在適合買入嗎？
- 台積電 未來展望如何？
        """
    )


if search_button:
    if query:
        if "query" not in st.session_state:
            st.session_state["query"] = query

        st.success(f"您搜索的股票是：{query}")
    else:
        st.warning("請輸入股票代號或名稱")
