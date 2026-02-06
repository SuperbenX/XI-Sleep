import streamlit as st

def init_audio_state():
    """初始化音频状态"""
    if "current_track" not in st.session_state:
        st.session_state.current_track = None

def play_track(track_info):
    """
    播放指定音轨
    track_info: {'title': '...', 'artist': '...', 'url': '...', 'cover': '...'}
    """
    st.session_state.current_track = track_info
    st.rerun()

def stop_track():
    """停止播放并清空状态"""
    st.session_state.current_track = None
    st.rerun()

def render_sidebar_player():
    """
    在侧边栏底部渲染全局播放器
    (包含防报错机制)
    """
    track = st.session_state.get("current_track")
    
    with st.sidebar:
        # 底部留白，把播放器挤下去 (可选)
        st.markdown("<br>" * 5, unsafe_allow_html=True)
        st.divider()
        
        # === 关键修复：使用占位符容器 ===
        # 所有会动态出现/消失的音频组件，都必须在这个容器里渲染
        player_container = st.empty()
        
        with player_container.container():
            if track:
                # --- A. 播放模式 ---
                # 封面与信息
                c1, c2 = st.columns([1, 2])
                with c1:
                    # 使用 Markdown 渲染图片可以避免 st.image 的某些布局问题，或者直接用 st.image
                    if track.get('cover'):
                        st.image(track['cover'], use_container_width=True)
                    else:
                        st.markdown("💿")
                with c2:
                    st.markdown(f"**{track.get('title', '未知曲目')}**")
                    st.caption(track.get('artist', 'XI Sleep'))
                
                # 音频组件 (自动播放)
                # key 是为了确保切歌时组件重置
                st.audio(track.get('url'), start_time=0)
                
                # 停止按钮 (点击后只负责改状态，rerun 会自动清空容器)
                if st.button("⏹ 停止播放", key="global_stop_btn", use_container_width=True):
                    stop_track()
                    
            else:
                # --- B. 静默模式 ---
                st.caption("🌊 息 · 此时无声")
                # 这里不渲染任何 st.audio 组件，从而避免 DOM 残留
