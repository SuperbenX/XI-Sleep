import streamlit as st
from utils.style import apply_global_style
from utils.audio_manager import render_sidebar_player

# 必须在其他 st 命令之前
st.set_page_config(page_title="栖息地", page_icon="🛖")

# 1. 样式注入
apply_global_style()

st.markdown("### 🛖 栖息地 · Habitat")
st.caption("整理羽毛，稍作休息。")

st.markdown("<br>", unsafe_allow_html=True)

# 卡片式布局
with st.container():
    st.markdown("""
    <style>
    .setting-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # 选项 1: 清理缓存
    st.markdown('<div class="setting-card">', unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown("**🧹 清理思绪 (Reset Cache)**")
        st.caption("如果遇到卡顿或异常，可以尝试重置。")
    with c2:
        if st.button("执行清理"):
            st.session_state.clear()
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # 选项 2: 版本信息
    st.markdown('<div class="setting-card">', unsafe_allow_html=True)
    st.markdown("**📦 关于 息 (XI Sleep)**")
    st.caption("Version 0.8.1 (Beta) · Build for Peace")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 侧边栏播放器驻留 (防止音乐中断或消失)
render_sidebar_player()
