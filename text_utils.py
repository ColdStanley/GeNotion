import re

def clean_markdown(text):
    # 替换 **加粗**
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    # 替换 *斜体* 和 _斜体_
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)
    # 替换标题符号（#）
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    # 替换列表项
    text = re.sub(r"^\s*[-*+]\s+", "• ", text, flags=re.MULTILINE)
    # 删除连续多空行
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
