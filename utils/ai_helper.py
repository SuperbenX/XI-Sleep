import streamlit as st
import google.generativeai as genai
import json
import random
import time

# --- 1. 配置 AI ---
def configure_ai():
    try:
        # 优先尝试从 secrets 获取，如果没有则尝试从环境变量
        api_key = st.secrets.get("GOOGLE_API_KEY")
        if not api_key:
            import os
            api_key = os.getenv("GOOGLE_API_KEY")
            
        if api_key:
            genai.configure(api_key=api_key)
            return True
    except Exception as e:
        print(f"AI Config Error: {e}")
    return False

# --- 2. 首页黄历 (JSON 生成) ---
def generate_daily_almanac(date_str=None, weather=None):
    """
    尝试生成结构化黄历数据。失败则返回 Mock。
    """
    # === 静态兜底数据 (Fallback) ===
    fallback_data = {
        "day": "06",
        "date_str": "2 月 2026",
        "lunar": "农历腊月十九",
        "title": "晨露微光，森林的呼吸。(离线)",
        "body": "网络似乎睡着了。但没关系，风吹过风铃，发出清脆的叮当声，远处的云朵像巨大的棉花糖。",
        "action_title": "宜 · 采撷新芽",
        "action_desc": "整理旧物，清理内心的缓存。",
        "image_url": "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?q=80&w=1920&auto=format&fit=crop"
    }

    if not configure_ai():
        return fallback_data

    try:
        model = genai.GenerativeModel('gemini-1.5-flash') # 使用轻量级模型以提速
        
        # 强制要求 JSON 格式
        prompt = f"""
        你是王家卫风格的城市游吟诗人。请为今天({date_str})写一份“深夜黄历”。
        严格以 JSON 格式返回，包含以下字段：
        - day: 日期数字 (如 "06")
        - date_str: 年月 (如 "2 月 2026")
        - lunar: 农历日期
        - title: 一句极短的、有画面感的标题 (10字以内)
        - body: 一段疏离、冷静、有都市感的描写 (50字以内)
        - action_title: 宜 · [两字动词]
        - action_desc: 对应的心理建议
        - image_url: "https://images.unsplash.com/photo-1518066000714-58c45f1a2c0a?q=80&w=1920&auto=format&fit=crop" (保持这个URL不变，或随机选一个氛围感的)
        
        不要使用 Markdown 标记，直接返回 JSON 字符串。
        """
        
        response = model.generate_content(prompt)
        # 清洗数据，防止 AI 加了 ```json 包裹
        text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(text)
        # 确保 url 存在
        if "image_url" not in data: 
            data["image_url"] = fallback_data["image_url"]
        return data

    except Exception as e:
        print(f"AI Generation Error: {e}")
        return fallback_data

# --- 3. 深夜私语 (Chat) ---
def chat_with_ai(user_message, history=[]):
    """
    流式对话。失败则返回 Mock。
    """
    # === 静态兜底 ===
    mock_responses = [
        "我在听。今晚的夜色很深，你不必急着做那个无坚不摧的大人。",
        "有些事如果不说出来，就会变成石头压在心口。这里只有风声和你。",
        "信号似乎不太好，但我依然在听。",
        "此刻，言语也许是多余的，但陪伴不是。"
    ]

    if not configure_ai():
        time.sleep(1)
        return random.choice(mock_responses)

    try:
        # 构建历史上下文 (Streamlit history -> Gemini history)
        # 这里简化处理，直接单轮对话或取最近几轮，避免 token 溢出
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        system_prompt = """
        Role: 深夜守夜人 (The Night Watchman).
        Tone: 王家卫风格，疏离、温柔、隐喻、非说教。
        Task: 回复用户的深夜倾诉。不要给具体建议，要给共情和意象。
        Context: 用户正独自一人面对屏幕。
        """
        
        chat = model.start_chat(history=[])
        response = chat.send_message(f"{system_prompt}\nUser says: {user_message}")
        return response.text

    except Exception as e:
        print(f"Chat Error: {e}")
        return random.choice(mock_responses)

# --- Compatibility Shims ---
get_ai_response = chat_with_ai

def generate_sleep_story(topic):
    if not configure_ai():
        time.sleep(1)
        return f"这是一段关于“{topic}”的梦境... (AI 离线模式)"
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Write a short, calming sleep story about {topic}. Keep it slow and descriptive.")
        return response.text
    except:
        return f"这是一段关于“{topic}”的梦境... (生成失败)"

def analyze_sleep_mood(history_text):
    if not configure_ai():
        time.sleep(1)
        return json.dumps({
            "category": "无剧情放映室",
            "reason": "系统处于离线模式，推荐您听听白噪音。",
            "nutrition": "平静感 +3"
        }, ensure_ascii=False)
        
    try:
        model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})
        response = model.generate_content(f"Analyze this chat history and prescribe a sleep category (Books/Movies/Music/Noise) in JSON: {history_text}")
        return response.text
    except:
        return json.dumps({"category": "琥珀色的慢板", "reason": "分析服务暂时不可用", "nutrition": "未知"}, ensure_ascii=False)

def generate_book_script(book_title, book_whisper):
    return f"这是关于《{book_title}》的解读... (模拟)"
