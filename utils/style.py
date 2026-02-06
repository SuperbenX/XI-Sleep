import streamlit as st

def apply_global_style():
    """
    注入全局样式：
    1. 引入 Noto Serif SC (宋体)。
    2. 强制应用字体到所有元素。
    3. 定义基础按钮和卡片样式。
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200;300;400;700&display=swap');
        
        /* 全局字体强制为宋体 */
        html, body, [class*="css"] {
            font-family: 'Noto Serif SC', serif !important;
        }
        
        /* 覆盖所有文本元素 */
        h1, h2, h3, h4, h5, h6, p, div, span, label, button, input, textarea, .stMarkdown {
            font-family: 'Noto Serif SC', serif !important;
        }
        
        /* 标题优化 */
        h1, h2, h3 {
            font-weight: 200 !important;
            letter-spacing: 0.08em !important;
        }
        
        /* 按钮样式微调 */
        .stButton button {
            border-radius: 16px;
            font-weight: 300 !important;
            background-color: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #e0e0e0 !important;
            transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
            backdrop-filter: blur(10px);
        }
        
        .stButton button:hover {
            background-color: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-1px);
        }
        
        /* 隐藏顶部红线 (Streamlit Decoration) */
        header[data-testid="stHeader"] {
            background: transparent;
        }
        .stApp > header {
            background: transparent;
        }
        </style>
    """, unsafe_allow_html=True)

def render_breathing_loader(text="正在织造..."):
    """
    渲染呼吸感加载动画
    """
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 60px;">
            <div style="
                width: 8px; height: 8px; 
                border-radius: 50%; 
                background-color: #e0e0e0;
                box-shadow: 0 0 15px rgba(224, 224, 224, 0.6);
                animation: breathe 3s infinite ease-in-out;
            "></div>
            <div style="
                margin-top: 24px; 
                font-size: 0.85rem; 
                color: rgba(224, 224, 224, 0.4); 
                letter-spacing: 0.3em; 
                animation: fadeText 3s infinite ease-in-out;
            ">{text}</div>
        </div>
        <style>
        @keyframes breathe {{
            0%, 100% {{ transform: scale(0.5); opacity: 0.2; box-shadow: 0 0 0 rgba(224,224,224,0); }}
            50% {{ transform: scale(1.5); opacity: 0.8; box-shadow: 0 0 20px rgba(224,224,224,0.4); }}
        }}
        @keyframes fadeText {{
            0%, 100% {{ opacity: 0.2; }}
            50% {{ opacity: 0.7; }}
        }}
        </style>
    """, unsafe_allow_html=True)
