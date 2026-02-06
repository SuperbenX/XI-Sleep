import streamlit as st

# --- 把这段 CSS 函数放在 app.py 最开头 ---
def load_ios_style():
    st.markdown("""
        <style>
        /* 1. 全局字体：强制使用苹果系统字体 */
        html, body, [class*="css"] {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
        }

        /* 2. 圆角按钮：让按钮像 iOS 的药丸形状 */
        .stButton > button {
            border-radius: 20px !important;
            border: none !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
            font-weight: 600 !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.2s ease;
        }
        .stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
        }

        /* 3. 输入框：圆润化处理 */
        .stTextInput > div > div > input {
            border-radius: 12px !important;
            border: 1px solid #E5E5EA !important;
            background-color: #FFFFFF !important;
        }
        
        /* 4. 侧边栏：去掉默认的粗糙感，改成磨砂白 */
        [data-testid="stSidebar"] {
            background-color: #F2F2F7 !important;
            border-right: 1px solid #E5E5EA;
        }

        /* 5. 卡片容器：在这个容器里的内容会有卡片效果 (可选) */
        .ios-card {
            background-color: white;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        
        /* 6. 去掉 Streamlit 默认的右上角菜单和页脚 (显得更像 App) */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# --- 在主程序一开始就调用它 ---
load_ios_style()

# ... 下面是你原来的代码 ...
# st.title("瞬息") ...
import streamlit as st
import time
import datetime
from utils.page_setup import setup_page
from utils.ai_helper import generate_daily_almanac

st.set_page_config(
    page_title="息 - Sleep",
    page_icon="🌑",
    layout="wide",
    initial_sidebar_state="auto"
)

setup_page()

# --- Splash Screen ---
if "first_visit" not in st.session_state:
    st.session_state.first_visit = True

if st.session_state.first_visit:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        .splash-container {
            height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #0f0f10;
            color: #e2e8f0;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .splash-logo {
            font-size: 5rem;
            font-weight: 100;
            letter-spacing: 0.2em;
            margin-bottom: 20px;
        }
        .splash-text {
            font-size: 1rem;
            opacity: 0.5;
            letter-spacing: 0.5em;
            text-transform: uppercase;
        }
        </style>
        <div class="splash-container">
            <div class="splash-logo">息</div>
            <div class="splash-text">请你好好睡觉</div>
        </div>
        """, unsafe_allow_html=True)
    
    time.sleep(2.5)
    placeholder.empty()
    st.session_state.first_visit = False

# --- Home Dashboard (Magazine Layout) ---
st.markdown("""
<style>
    /* 巨大数字 */
    .big-date {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 140px;
        font-weight: 100;
        line-height: 1;
        color: #E0E0E0;
        letter-spacing: -5px;
    }
    /* 标题 */
    .hero-title {
        font-family: 'Noto Serif SC', serif !important;
        font-size: 28px;
        font-weight: 600;
        color: #E0E0E0;
        margin-bottom: 10px;
    }
    /* 正文 (蓝紫色) */
    .hero-body {
        font-family: 'Noto Serif SC', serif !important;
        font-size: 16px;
        color: #8da4ef; /* 参考图中的淡蓝紫色 */
        line-height: 1.6;
    }
    /* 图片容器 */
    .poster-card {
        margin-top: 30px;
        width: 100%;
        height: 400px;
        background-size: cover;
        background-position: center;
        border-radius: 30px;
        position: relative;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        overflow: hidden;
    }
    /* 底部毛玻璃条 */
    .glass-bar {
        position: absolute;
        bottom: 20px;
        left: 20px;
        right: 20px;
        background: rgba(20, 20, 40, 0.6);
        backdrop-filter: blur(12px);
        padding: 15px 25px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        color: white;
        font-family: 'Noto Serif SC', serif;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .yi-icon {
        background: #6c5ce7;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

today = datetime.datetime.now()

@st.cache_data(ttl=3600*6)
def get_cached_almanac(date_str):
    return generate_daily_almanac(date_str)

data = get_cached_almanac(today.strftime("%Y-%m-%d"))

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

col_left, col_right = st.columns([1.1, 1], gap="large")

with col_left:
    st.markdown(f"""
    <div>
        <div class="big-date">{data['day']}</div>
        <div style="font-size:14px; letter-spacing:2px; margin-bottom:30px; opacity:0.6; text-transform:uppercase;">{data['date_str']} · {data['lunar']}</div>
        <div class="hero-title">{data['title']}</div>
        <div class="hero-body">{data['body']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("进入梦模式 · Deep Dive", use_container_width=True, type="primary"):
        st.switch_page("pages/3_⚓_深潜.py")

with col_right:
    # 使用 HTML 渲染带毛玻璃遮罩的海报
    st.markdown(f"""
    <div class="poster-card" style="background-image: url('{data['image_url']}');">
        <div class="glass-bar">
            <div class="yi-icon">宜</div>
            <div>
                <div style="font-size:12px; opacity:0.8; letter-spacing:1px;">{data['action_title']}</div>
                <div style="font-size:14px;">{data['action_desc']}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
