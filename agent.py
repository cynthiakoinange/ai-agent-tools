from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from tools.web_search import search_web
from tools.calculator import calculate
from tools.file_reader import read_file

tools = [
    Tool(name="Web Search", func=search_web, description="Search the web"),
    Tool(name="Calculator", func=calculate, description="Do calculations"),
    Tool(name="File Reader", func=read_file, description="Read file content")
]

llm = ChatOpenAI(temperature=0, model_name="gpt-4")

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
