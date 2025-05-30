import streamlit as st
from content_generator import generate_content
from notion_writer import write_to_notion
from text_utils import clean_markdown

st.set_page_config(page_title="Gemini → Notion 写入工具", layout="centered")
st.title("📝 Gemini to Notion Writer")

user_prompt = st.text_input("请输入主题：", placeholder="例如：Solution Consultant 需要哪些能力？")

if st.button("生成并写入 Notion"):
    with st.spinner("🤖 正在调用 Gemini 生成内容..."):
        full_prompt = user_prompt.strip() + "\n\n请用自然语言生成纯文本回答，不要使用 Markdown。"
        response = generate_content(full_prompt)
        clean_text = clean_markdown(response)
        write_to_notion(user_prompt, clean_text)
    st.success("✅ 内容已写入 Notion！")
    st.text_area("💬 AI 生成结果（纯文本）：", value=clean_text, height=300)
