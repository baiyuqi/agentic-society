from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph
from langchain_community.chat_models import ChatZhipuAI

model = ChatZhipuAI(
    model="glm-4",
    api_key="a075eb3edebc5741d238284820988035.6k1unECbt6xLUxfG",
)

graph = MessageGraph()

# This will not work with MessageGraph!
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

@tool
def multiply(first_number: int, second_number: int):
    """Multiplies two numbers together."""
    return first_number * second_number


model_with_tools = model.bind_tools([multiply])

builder = MessageGraph()

builder.add_node("oracle", model_with_tools)

tool_node = ToolNode([multiply])
builder.add_node("multiply", tool_node)

builder.add_edge("multiply", END)

builder.set_entry_point("oracle")
