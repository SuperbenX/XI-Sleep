import asyncio
import os
import sys

# Ensure project root is in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

import edge_tts
from utils.literature_data import LITERATURE_VAULT
from utils.ai_helper import generate_book_script

OUTPUT_BASE_DIR = "assets/audio/literature"

async def generate_audio_for_book(book, index, total):
    category_dir = os.path.join(OUTPUT_BASE_DIR, book["category"])
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    
    filename = f"{book['title']}.mp3"
    filepath = os.path.join(category_dir, filename)
    
    if os.path.exists(filepath):
        print(f"⏭️  [{index}/{total}] Skipped {book['title']} (Already exists)")
        return

    print(f"⏳ [{index}/{total}] Generating script for {book['title']}...")
    script = generate_book_script(book["title"], book["whisper"])
    
    if script.startswith("Error"):
        print(f"❌ Error generating script for {book['title']}: {script}")
        return

    print(f"🎙️  [{index}/{total}] Synthesizing audio for {book['title']}...")
    communicate = edge_tts.Communicate(script, voice="zh-CN-XiaoxiaoNeural", rate="+0%")
    await communicate.save(filepath)
    
    print(f"✅ [{index}/{total}] {book['title']} Done")

async def main():
    # SAMPLE MODE: First book of each category
    processed_categories = set()
    sample_books = []
    
    for book in LITERATURE_VAULT:
        if book["category"] not in processed_categories:
            sample_books.append(book)
            processed_categories.add(book["category"])
            
    total = len(sample_books)
    print(f"Starting sampling generation for {total} books (1 per category)...")
    
    for i, book in enumerate(sample_books, 1):
        await generate_audio_for_book(book, i, total)

if __name__ == "__main__":
    asyncio.run(main())
