import streamlit as st
import datetime
import random

def inject_custom_css():
    st.markdown("""
        <style>
        /* 全局背景设为极夜黑 (复刻原版 Radial Gradient) */
        .stApp {
            background-color: #0f0f10;
            background-image: radial-gradient(circle at 50% 40%, #1e1e21 0%, #0f0f10 100%);
            background-attachment: fixed;
            color: #888888;
        }
        
        /* 玻璃拟态卡片 (Glassmorphism) */
        .glass-card, .almanac-card, div[data-testid="stContainer"] {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 24px;
        }
        
        /* 按钮风格迁移 */
        .stButton button {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            color: #e2e8f0 !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(10px);
        }
        
        .stButton button:hover {
            background: rgba(129, 140, 248, 0.1);
            border-color: rgba(129, 140, 248, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        
        /* 标题和文字 */
        h1, h2, h3 {
            color: #e2e8f0 !important;
            font-weight: 300 !important;
            letter-spacing: 0.05em !important;
        }
        
        .footer-text {
            text-align: center;
            opacity: 0.3;
            font-size: 0.7rem;
            margin-top: 50px;
            letter-spacing: 0.2em;
            text-transform: uppercase;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header(title=None):
    today = datetime.datetime.now()
    date_str = today.strftime("%Y.%m.%d")
    
    # Random online count simulation
    online_count = random.randint(800, 1200)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        if title:
            st.markdown(f"<h2 style='margin:0;'>{title}</h2>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='margin:0;'>息 · Sleep Sanctuary</h2>", unsafe_allow_html=True)
            
    with col2:
        st.markdown(f"""
        <div style="text-align: right; opacity: 0.5; font-size: 0.8rem; font-family: monospace;">
            <span style="color: #818cf8;">●</span> {online_count} ONLINE
            <br>
            {date_str}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
