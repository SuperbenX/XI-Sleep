import asyncio
import edge_tts
import os

# 1. 强制定义内容 (跳过 AI 生成，排除 API 错误)
TEXT = "今晚，我们去康科德的林间坐坐。我是梭罗。我独自生活在森林里，距离任何邻居都有一英里之遥..."
VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_FILE = "瓦尔登湖_test.mp3"

async def main():
    print(f"🚀 开始生成: {OUTPUT_FILE} ...")
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"✅ 生成成功！文件应该在: {os.getcwd()}/{OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())
