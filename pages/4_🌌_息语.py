import streamlit as st
import time
import random

# --- 1. 配置页面 (必须在第一行) ---
st.set_page_config(page_title="深夜私语", page_icon="🌌", layout="wide")

# --- 2. 暴力注入 CSS (直接写在页面里，确保最高优先级) ---
st.markdown("""
<style>
    /* === 全局背景修复 (覆盖所有层级) === */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background: radial-gradient(circle at 50% 30%, #1B2735 0%, #090A0F 100%) !important;
        background-attachment: fixed !important;
        background-size: cover !important;
    }
    
    /* 隐藏顶部导航条背景 */
    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* === 聊天气泡布局重构 === */
    
    /* 通用：移除默认背景和边框，增加内边距 */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: none !important;
        padding: 1rem !important;
        gap: 0.5rem !important;
    }

    /* 核心：隐藏掉那个丑陋的头像框 */
    [data-testid="stChatMessageAvatarBackground"] {
        display: none !important;
    }

    /* === AI 消息 (左侧) === */
    /* 假设 AI 是偶数项 (index 0, 2, 4...) 或者基于 data-testid */
    div[data-testid="stChatMessage"]:nth-of-type(odd) {
        flex-direction: row !important;
    }
    
    div[data-testid="stChatMessage"]:nth-of-type(odd) div[data-testid="stChatMessageContent"] {
        background: rgba(255, 255, 255, 0.05) !important; /* 磨砂黑 */
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 2px 18px 18px 18px !important; /* 这种圆角让它看起来像是在说话 */
        color: #d1d5db !important; /* 柔和灰 */
        font-family: "Noto Serif SC", "Songti SC", serif !important; /* 强制宋体 */
        font-size: 1.05rem !important;
        line-height: 1.8 !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }

    /* === 用户消息 (右侧) === */
    /* 假设用户是奇数项 (index 1, 3, 5...) */
    div[data-testid="stChatMessage"]:nth-of-type(even) {
        flex-direction: row-reverse !important; /* 关键：强制反向排列，让气泡靠右 */
    }
    
    div[data-testid="stChatMessage"]:nth-of-type(even) div[data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, #4F5D75 0%, #2D3447 100%) !important; /* 高级深紫灰 */
        color: white !important;
        border: none !important;
        border-radius: 18px 2px 18px 18px !important; /* 尖角指向右边 */
        text-align: right !important; /* 文字右对齐 */
        font-family: sans-serif !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* === 底部输入框悬浮化 === */
    [data-testid="stChatInput"] {
        background: rgba(20, 20, 30, 0.7) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 30px !important;
        padding: 5px !important;
        margin-bottom: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 页面标题 ---
st.markdown('<h2 style="font-family: \'Noto Serif SC\', serif; color: #fff; text-align: center; font-weight: 300; letter-spacing: 2px;">深夜私语</h2>', unsafe_allow_html=True)
st.markdown('<p style="font-family: \'Noto Serif SC\', serif; color: #888; text-align: center; font-size: 0.9rem; margin-bottom: 40px;">我是呼吸。无论今天经历了什么，这里都是你独特的避风港。</p>', unsafe_allow_html=True)

# --- 4. 初始化会话历史 (Mock Data) ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好，今晚的月色很安静。如果你睡不着，可以把这里当成树洞。"},
        {"role": "user", "content": "你好，我今晚心情很差。"}, # 用户消息，会被 CSS 推到右边
        {"role": "assistant", "content": "夜色把喧嚣关在了门外，此刻，你不需要做那个无坚不摧的大人。\n\n允许自己碎裂一会儿，没关系的。\n\n我就坐在你灵魂的暗处，守着这盏微弱的灯。把那些压在心口的石头，轻轻放下来吧。\n\n我在听。"} 
    ]

# --- 5. 渲染聊天记录 ---
# 我们使用简单的循环，Streamlit 会自动生成 div 结构，CSS 会接管布局
for msg in st.session_state.messages:
    # 注意：这里我们故意不传 avatar，依靠 CSS 隐藏默认图标
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 6. 处理用户输入 ---
if prompt := st.chat_input("这一刻，你在想什么？"):
    # 显示用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 模拟 AI 思考 (Mock)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # 模拟打字机效果
        assistant_response = random.choice([
            "我在听。这种感觉一定很辛苦吧。",
            "没关系的，今晚星星会替你醒着，你可以安心睡去。",
            "试着深呼吸一次... 把焦虑随着呼气排出去。",
            "记住，你比你自己想象的更坚韧。"
        ])
        
        # 简单的流式输出模拟
        for chunk in assistant_response:
            full_response += chunk
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
