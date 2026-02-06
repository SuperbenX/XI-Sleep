import streamlit as st

# --- 1. 这里也要加上 CSS 样式 (或者你可以把它封装到 utils 里导入) ---
def load_ios_style():
    st.markdown("""
        <style>
        /* 这里复制刚才那一大段 CSS 代码，为了简洁我省略了，请确保 .ios-card 在里面 */
        html, body, [class*="css"] {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        }
        .ios-card {
            background-color: white;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        /* ... 其他 CSS ... */
        </style>
    """, unsafe_allow_html=True)

# --- 2. 调用样式 ---
load_ios_style()

# --- 3. 页面标题 ---
st.title("🛖 栖息地")

# --- 4. 这里的代码就是你要放的位置！ ---
st.markdown('<div class="ios-card">', unsafe_allow_html=True)

st.subheader("🌙 睡眠偏好")
st.toggle("开启白噪音", value=True)
st.slider("默认音量", 0, 100, 30)

st.markdown('</div>', unsafe_allow_html=True)


# --- 5. 你可以再复制一份，做第二个卡片 ---
st.markdown('<div class="ios-card">', unsafe_allow_html=True)

st.subheader("👤 账号设置")
st.text_input("昵称", value="Superben")
st.button("注销")

st.markdown('</div>', unsafe_allow_html=True)