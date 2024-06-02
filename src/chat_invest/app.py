import streamlit as st

# 設置頁面標題
st.set_page_config(page_title="問卷調查")

# 問卷問題列表
questions = [
    "請問您的性別是？",
    "請問您的年齡範圍是？",
    "請問您對我們的產品滿意度如何？",
    "請問您會向朋友推薦我們的產品嗎？"
]

# 問卷選項列表
options = [
    ["男", "女"],
    ["18歲以下", "18-25歲", "26-35歲", "36-45歲", "46歲以上"],
    ["非常滿意", "滿意", "一般", "不滿意", "非常不滿意"],
    ["會", "不會"]
]

# 儲存用戶回答的列表
answers = []

# 顯示問卷標題
st.title("問卷調查")

# 逐個顯示問題並獲取用戶回答
for i, question in enumerate(questions):
    st.subheader(question)
    answer = st.radio("請選擇您的答案", options[i])
    answers.append(answer)
    
    # 在每個問題後添加一個分隔線，除了最後一個問題
    if i < len(questions) - 1:
        st.markdown("---")
        
# 顯示提交按鈕
if st.button("提交"):
    st.success("感謝您完成問卷調查！")
    
    # 顯示用戶的回答
    st.subheader("您的回答：")
    for i, answer in enumerate(answers):
        st.write(f"{questions[i]}: {answer}")