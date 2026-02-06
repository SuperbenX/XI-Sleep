# Mock Data migrated from components.ts

SOUNDSCAPES = [
  { "id": 'rain', "name": 'Rain', "icon": '🌧️', "description": 'Soft pitter-patter on a tin roof.', "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" },
  { "id": 'forest', "name": 'Forest', "icon": '🌲', "description": 'Rustling leaves and distant birds.', "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" },
  { "id": 'ocean', "name": 'Ocean', "icon": '🌊', "description": 'Gentle waves on a sandy shore.', "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3" },
  { "id": 'fire', "name": 'Fireplace', "icon": '🔥', "description": 'Crackling wood and warm embers.', "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3" },
]

# 光影的余烬 (Movies)
MOVIE_LIST = [
    {
        "id": "ember-1",
        "title": "《肖申克的救赎》- 场景素描",
        "category": "光影的余烬",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "coverImage": "https://images.unsplash.com/photo-1485846234645-aae511591952?auto=format&fit=crop&q=80&w=600",
        "duration": "45:00",
        "description": "[光影素描] 极慢速度描述《肖申克的救赎》中一个寂静的长镜头。",
        "introText": "瑞德，那个关于希望的午后，阳光洒在房顶，这不仅是自由的味道，更是入睡前的宁静。",
        "tags": ["低剧情起伏", "氛围电影"],
        "isAiGenerated": True
    },
    {
        "id": "ember-2",
        "title": "《教父》- 场景素描",
        "category": "光影的余烬",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "coverImage": "https://images.unsplash.com/photo-1485846234646-aae511591952?auto=format&fit=crop&q=80&w=600", # Mocked image increment
        "duration": "45:00",
        "description": "[光影素描] 极慢速度描述《教父》中一个寂静的长镜头。",
        "introText": "那些关于家族的低语，在阴影中盘旋。让权力和纷争在这一刻熄灭，只剩下壁炉的余烬。",
        "tags": ["低剧情起伏", "氛围电影"],
        "isAiGenerated": True
    },
    {
        "id": "ember-3",
        "title": "《星际穿越》- 场景素描",
        "category": "光影的余烬",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "coverImage": "https://images.unsplash.com/photo-1485846234647-aae511591952?auto=format&fit=crop&q=80&w=600",
        "duration": "45:00",
        "description": "[光影素描] 极慢速度描述《星际穿越》中一个寂静的长镜头。",
        "introText": "跨越亿万光年的孤独，最终落在那排书架后。在库珀的视线里，我们缓缓闭眼。",
        "tags": ["低剧情起伏", "氛围电影"],
        "isAiGenerated": True
    }
]

# 琥珀色的慢板 (Music)
MUSIC_LIST = [
    {
        "id": "adagio-1",
        "title": "巴赫：G弦上的咏叹调",
        "category": "琥珀色的慢板",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "coverImage": "https://images.unsplash.com/photo-1514119412350-e174d90d280e?auto=format&fit=crop&q=80&w=600",
        "duration": "30:00",
        "description": "[琥珀色慢板] 缓慢舒展的弦乐，如静谧河流。",
        "tags": ["纯音乐", "低频无损"]
    },
    {
        "id": "adagio-2",
        "title": "德彪西：月光",
        "category": "琥珀色的慢板",
        "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
        "coverImage": "https://images.unsplash.com/photo-1514119412351-e174d90d280e?auto=format&fit=crop&q=80&w=600",
        "duration": "30:00",
        "description": "[琥珀色慢板] 柔和的钢琴波纹，映照意识的湖面。",
        "tags": ["纯音乐", "低频无损"]
    }
]

# Dream Weaver Stories
MOCK_STORIES = [
  {
    "id": 's1',
    "title": 'The Starry Night',
    "imageUrl": 'https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&q=80&w=600',
    "duration": '20m',
    "description": 'A journey through a swirling sky.'
  },
  {
    "id": 's2',
    "title": 'Autumn Leaves',
    "imageUrl": 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=600',
    "duration": '15m',
    "description": 'The golden hour in a silent wood.'
  }
]

# Night Wake Patch (Specific item)
NIGHT_WAKE_ITEM = {
    "id": 'w1',
    "title": '深夜火车站远处轰鸣',
    "category": '无剧情放映室',
    "url": 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3',
    "coverImage": 'https://images.unsplash.com/photo-1542332213-31f87348057f?auto=format&fit=crop&q=80&w=600',
    "duration": '10:00',
    "description": '极低频，适合夜醒后快速拉回睡眠状态。',
    "tags": ["非人声", "白噪声"]
}

# Aggregate List (excluding Books which are in literature_data)
# Note: In the React app, MOCK_AUDIO_ITEMS included Classics. 
# Here we separate them to avoid duplication with LITERATURE_VAULT
EXTRA_AUDIO_ITEMS = [
    *MOVIE_LIST,
    *MUSIC_LIST,
    NIGHT_WAKE_ITEM
]
