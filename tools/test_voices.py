import asyncio
import os
import edge_tts

OUTPUT_DIR = "assets/audio/demos"

SAMPLES = [
    {
        "name": "sample_1_xiaoxiao_normal.mp3",
        "voice": "zh-CN-XiaoxiaoNeural",
        "rate": "+0%",
        "pitch": "+0Hz",
        "text": "今晚，我们去康科德的林间坐坐。戈壁滩上的风，会吹走所有烦恼。"
    },
    {
        "name": "sample_2_xiaoxiao_sleep.mp3",
        "voice": "zh-CN-XiaoxiaoNeural",
        "rate": "-25%",
        "pitch": "-2Hz",
        "text": "今晚，我们去康科德的林间坐坐。戈壁滩上的风，会吹走所有烦恼。"
    },
    {
        "name": "sample_3_yunxi_sleep.mp3",
        "voice": "zh-CN-YunxiNeural",
        "rate": "-20%",
        "pitch": "+0Hz",
        "text": "今晚，我们去康科德的林间坐坐。戈壁滩上的风，会吹走所有烦恼。"
    }
]

async def generate_voice(sample):
    output_path = os.path.join(OUTPUT_DIR, sample["name"])
    print(f"Generating {output_path}...")
    print(f"  Voice: {sample['voice']}")
    print(f"  Rate: {sample['rate']}")
    print(f"  Pitch: {sample['pitch']}")
    
    communicate = edge_tts.Communicate(
        text=sample["text"],
        voice=sample["voice"],
        rate=sample["rate"],
        pitch=sample["pitch"]
    )
    await communicate.save(output_path)
    print("  Done.")

async def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    for sample in SAMPLES:
        await generate_voice(sample)
    
    print("All samples generated successfully.")

if __name__ == "__main__":
    asyncio.run(main())
