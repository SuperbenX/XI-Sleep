from utils.style import apply_global_style
from utils.audio_manager import render_sidebar_player, init_audio_state

def setup_page():
    """
    Standard setup for all pages:
    1. Injects global CSS (True Black Theme, Noto Serif SC)
    2. Initializes audio state
    3. Renders Sidebar Player (Ghost Player)
    """
    apply_global_style()
    init_audio_state()
    render_sidebar_player()
