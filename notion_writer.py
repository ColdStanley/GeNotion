import requests
from config import NOTION_API_KEY, DATABASE_ID

def write_to_notion(title, content):
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Title": {
                "title": [{"text": {"content": title}}]
            },
            "Content": {
                "rich_text": [{"text": {"content": content}}]
            },
            "Tag": {
                "select": {"name": "Gemini"}
            }
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        print("✅ Notion 写入成功")
    else:
        print("❌ 写入失败:", response.text)
