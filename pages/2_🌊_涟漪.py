import streamlit as st
from utils.page_setup import setup_page
from utils.audio_manager import play_track
from utils.mock_data import SOUNDSCAPES, MOVIE_LIST, MUSIC_LIST
from utils.literature_data import LITERATURE_VAULT

st.set_page_config(page_title="Ripples", page_icon="🌊")
setup_page()

st.title("🌊 涟漪")
st.caption("库藏内容与深度织造")

if "active_category" not in st.session_state:
    st.session_state.active_category = "books"

def render_list(items):
    for item in items:
        with st.container():
            c1, c2, c3 = st.columns([1, 4, 1.5])
            with c1:
                if 'icon' in item:
                    st.markdown(f"## {item['icon']}")
                elif 'coverImage' in item:
                    st.image(item['coverImage'], width=60)
                else:
                    st.markdown("## 💿")
            with c2:
                title = item.get('title') or item.get('name')
                desc = item.get('description') or item.get('whisper') or item.get('introText')
                st.markdown(f"**{title}**")
                if desc:
                    st.caption(desc[:60] + "..." if len(desc)>60 else desc)
            with c3:
                key_id = item.get('id')
                if st.button("▶ 播放", key=f"play_{key_id}"):
                    track_data = {
                        "title": title,
                        "artist": "XI Sleep · 息",
                        "url": item.get('url', 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'),
                        "cover": item.get('coverImage')
                    }
                    play_track(track_data)
        st.divider()

def render_cat_header(id, icon, title, sub):
    with st.container():
        c1, c2, c3 = st.columns([1, 4, 1.5])
        with c1: st.markdown(f"# {icon}")
        with c2: 
            st.markdown(f"### {title}")
            st.caption(sub)
        with c3: 
            if st.button("进入", key=f"btn_{id}"): 
                st.session_state.active_category = id
                st.rerun()

# 1. Books
render_cat_header("books", "📖", "故纸堆里的哈欠", "100 Masterpieces")
if st.session_state.active_category == "books":
    st.markdown("---")
    render_list(LITERATURE_VAULT[:10])

st.markdown("---")

# 2. Movies
render_cat_header("movies", "🎬", "光影的余烬", "Cinematic Atmosphere")
if st.session_state.active_category == "movies":
    st.markdown("---")
    render_list(MOVIE_LIST)

st.markdown("---")

# 3. Music
render_cat_header("music", "🎻", "琥珀色的慢板", "Classic Adagio")
if st.session_state.active_category == "music":
    st.markdown("---")
    render_list(MUSIC_LIST)

st.markdown("---")

# 4. Noise
render_cat_header("noise", "🌫️", "无剧情放映室", "Ambient Noise")
if st.session_state.active_category == "noise":
    st.markdown("---")
    render_list(SOUNDSCAPES)
