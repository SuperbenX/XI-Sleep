import streamlit as st

def inject_fonts():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200;300;400;700&display=swap');
        
        /* 强制全局宋体 */
        html, body, [class*="css"] {
            font-family: 'Noto Serif SC', serif !important;
        }
        
        /* 标题样式 */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Noto Serif SC', serif !important;
            font-weight: 300 !important;
            letter-spacing: 0.05em !important;
        }
        
        /* 按钮文字 */
        .stButton button {
            font-family: 'Noto Serif SC', serif !important;
            font-weight: 400 !important;
        }
        
        /* 输入框文字 */
        .stTextInput input, .stTextArea textarea {
            font-family: 'Noto Serif SC', serif !important;
        }
        </style>
    """, unsafe_allow_html=True)

def render_breathing_loader(text="正在织造梦境..."):
    """
    渲染一个呼吸感的加载动画，替代 st.spinner
    """
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 40px; margin-top: 20px;">
            <div style="
                width: 60px; height: 60px; 
                border-radius: 50%; 
                background: radial-gradient(circle, rgba(129,140,248,0.4) 0%, rgba(0,0,0,0) 70%);
                animation: breathe 3s infinite ease-in-out;
            "></div>
            <div style="
                margin-top: 20px; 
                font-size: 0.8rem; 
                color: rgba(255,255,255,0.5); 
                letter-spacing: 0.2em; 
                animation: fadeText 3s infinite ease-in-out;
            ">{text}</div>
        </div>
        <style>
        @keyframes breathe {{
            0%, 100% {{ transform: scale(0.8); opacity: 0.3; }}
            50% {{ transform: scale(1.2); opacity: 0.8; }}
        }}
        @keyframes fadeText {{
            0%, 100% {{ opacity: 0.3; }}
            50% {{ opacity: 0.8; }}
        }}
        </style>
    """, unsafe_allow_html=True)

def render_sidebar_player():
    """
    在侧边栏底部渲染迷你播放器
    """
    if "current_audio" in st.session_state and st.session_state.current_audio:
        audio = st.session_state.current_audio
        with st.sidebar:
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"<div style='font-size: 0.8rem; opacity: 0.7; margin-bottom: 5px;'>🎧 正在播放</div>", unsafe_allow_html=True)
            st.markdown(f"**{audio.get('title', 'Unknown Track')}**")
            if 'category' in audio:
                st.caption(audio['category'])
                
            # 使用 key 防止组件重绘导致的闪烁，但 Streamlit session 刷新仍会重置播放进度
            # 这是一个已知限制，但至少 UI 还在
            st.audio(audio.get('url'), start_time=0) 
