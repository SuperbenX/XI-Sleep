import streamlit as st
import random
import time
from utils.style import apply_global_style
from utils.mock_data import SOUNDSCAPES

# 1. 应用全局样式
apply_global_style()

# 2. 初始化/检查状态
if "deep_dive_track" not in st.session_state:
    st.session_state.deep_dive_track = random.choice(SOUNDSCAPES)

# --- 逻辑函数 ---
def switch_track():
    """切歌"""
    new_track = random.choice(SOUNDSCAPES)
    while new_track['id'] == st.session_state.deep_dive_track['id'] and len(SOUNDSCAPES) > 1:
        new_track = random.choice(SOUNDSCAPES)
    st.session_state.deep_dive_track = new_track

def stop_playback():
    """安全停止播放"""
    st.session_state.deep_dive_track = None
    # 强制刷新以移除播放器
    st.rerun()

def extend_session():
    """续播"""
    st.toast(f"🌘 已延长播放时间...", icon="⏳")

# --- UI 渲染 ---
st.markdown("""
<style>
    header {visibility: hidden;}
    .stApp {background-color: #02040a !important;}
    
    .album-card {
        background: linear-gradient(180deg, #1e272e 0%, #000000 100%);
        padding: 40px 20px;
        border-radius: 20px;
        border: 1px solid #333;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    .track-title { font-family: 'Noto Serif SC', serif; font-size: 1.8rem; color: #f1f2f6; margin: 15px 0 5px 0; }
    .track-desc { color: #747d8c; font-size: 0.9rem; letter-spacing: 1px; }
    
    /* 停止状态的空卡片样式 */
    .empty-card {
        padding: 60px 20px;
        border: 1px dashed #333;
        border-radius: 20px;
        text-align: center;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("### ⚓ 深潜电台 · Deep Dive FM")

# === 核心播放区容器 (关键修复：使用占位符) ===
player_container = st.empty()

# 获取当前曲目
track = st.session_state.deep_dive_track

with player_container.container():
    if track:
        # --- 播放状态 ---
        st.markdown(f"""
        <div class="album-card">
            <div style="font-size: 80px; margin-bottom: 10px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.2));">💿</div>
            <div class="track-title">{track['name']}</div>
            <div class="track-desc">正在播放 · 随机助眠频率</div>
        </div>
        """, unsafe_allow_html=True)
        
        # 音频组件
        st.audio(
            track.get('url'), 
            format="audio/mp3", 
            start_time=0, 
            autoplay=True 
        )
    else:
        # --- 停止状态 (显示"重新开始"界面) ---
        st.markdown("""
        <div class="empty-card">
            <h3>🌑 已停止</h3>
            <p>世界已安静。点击下方按钮重新潜入。</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# === 控制区 ===
if track:
    # 播放时的控制栏
    c1, c2, c3 = st.columns([1, 1, 1])
    
    with c1:
        if st.button("🔀 换一首", use_container_width=True):
            switch_track()
            st.rerun()
            
    with c2:
        # 这里的停止按钮现在是安全的
        if st.button("■ 停止", type="primary", use_container_width=True):
            stop_playback()
            
    with c3:
         if st.button("🔁 续播", use_container_width=True):
            extend_session()
            
else:
    # 停止时的控制栏
    if st.button("▶ 重新开始深潜", type="primary", use_container_width=True):
        st.session_state.deep_dive_track = random.choice(SOUNDSCAPES)
        st.rerun()
