from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()
import json

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

def plan_categories():
    prompt = """"
    You are a news planning agent. Select 4 globally important news for today's roundup. 
    Choose from: technology, business, general, health, science, sports, entertainment

    Return ONLY a JSON list.  
    Example: ["technology", "business", "general", "science"] 
    """

    response = model.invoke([HumanMessage(content=prompt)])
    return json.loads(response.content)