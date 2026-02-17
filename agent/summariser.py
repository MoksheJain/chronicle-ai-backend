from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)

from tools.sheet_manager import get_all_subscribers

def summarise_english(category, articles):
    article_text = "\n\n".join([f"{a['title']} - {a['description']}" for a in articles])
    prompt = f"""
    You are a professional news editor. 
    Category: {category}
    Articles: {article_text}
    Language: English
    Generate:
    - A short engaging paragraph.
    - 3 bullet highlights.
    - One line: why this matters.

    Format this in clean HTML in provided language.
    """

    response = model.invoke([HumanMessage(content=prompt)])

    return response.content

def summarise_hindi(category, articles):
    article_text = "\n\n".join([f"{a['title']} - {a['description']}" for a in articles])
    prompt = f"""
    You are a professional news editor. 
    Category: {category}
    Articles: {article_text}
    Language: Hindi
    Generate:
    - A short engaging paragraph.
    - 3 bullet highlights.
    - One line: why this matters.

    Format this in clean HTML in provided language.
    """

    response = model.invoke([HumanMessage(content=prompt)])

    return response.content
