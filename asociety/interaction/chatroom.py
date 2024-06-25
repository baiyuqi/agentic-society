

from langchain_core.messages import (
    BaseMessage,
    ToolMessage,
    HumanMessage,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph


def create_agent(llm, name, persona: str):
    """Create an agent."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                
               
                "{persona}Now you inside a chatroom. Prefix your message with #yournickname. You can use @ somebody or just publish a message without specifying a person.For example, if you are chatter1 and want to address chatter2, start with \'#chatter1:\n@chatter2\'.\n"
                "Your nickname is {name}\n"
                ,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )
    prompt = prompt.partial(persona=persona, name=name)
    return prompt | llm



from typing import Annotated



import operator
from typing import Annotated, Sequence, TypedDict


from typing_extensions import TypedDict


# This defines the object that is passed between each node
# in the graph. We will create different nodes for each agent and tool
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str



import functools
from langchain_core.messages import AIMessage


# Helper function to create a node for a given agent
def agent_node(state, agent, name):
    result = agent.invoke(state)
    result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
    return {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "sender": name,
    }

from langchain_community.chat_models import ChatZhipuAI
from asociety.generator.llm_engine import llm


# Either agent can decide to end
from typing import Literal


def router(state, personas) :
    # This is the router
    import random
    return random.choice(list(personas.keys()))
    

def create_graph(personas):
    chatters = {}
    routerd = {}

    global router
    for i, (k,v) in enumerate(personas.items()):
        name = "chatter" + k
        agent = create_agent(
            llm,
            name,
            persona=v,
        )
       
        chatter = functools.partial(agent_node, agent=agent, name=name)
        routerd[name] = name
      
        chatters[name] = chatter


    workflow = StateGraph(AgentState)
    mrouter = functools.partial(router, personas=routerd)
    for k, c in chatters.items():
        workflow.add_node(k, c)
        workflow.add_conditional_edges(
            k,
            mrouter,
            routerd,
        )
    

    workflow.set_entry_point("chatter9")
    
    graph = workflow.compile()
    return graph


if __name__ == "__main__": 
    personas = {'9':'''You are a 43-year-old professional, employed in the federal government sector. With a solid educational background that includes professional school, you have accumulated 15 years of education. As a married man, you are the proud husband in a civilian marriage, and you hold the title of a professional specialist in your occupation. Your Asian-Pacific Islander heritage contributes to your unique perspective in your work and personal life. Despite having no capital gains to speak of, you have experienced a capital loss of 2415, which has not deterred you from working diligently, clocking in 55 hours a week. Your income comfortably surpasses the 50K mark, reflecting your hard work and dedication. Your native country remains a mystery, perhaps a topic you choose to explore with others rather than revealing directly. Overall, you present as a committed, well-educated professional with a strong sense of responsibility and a varied life experience.''',
                '10':'''You are a 25-year-old married man, originally from Guatemala, now living and working in the private sector. With a 10th-grade education under your belt, which translates to about 6 years of formal schooling, you've embarked on a career as a machine operator and inspector. Your workweek is standard, clocking in at 40 hours, and you've yet to see significant capital gains or losses. Your income level is currently less than 50K per year. As a husband and a provider, you likely carry a sense of responsibility for your family, striving to make the best of your circumstances and work your way up in life. Your journey from Guatemala to your current life has shaped you into a resilient and hardworking individual.''',
                '11':'''You are a 31-year-old, highly educated black woman, working in a private sector with a specialized professional occupation. You have never been married and currently have no family ties, which may explain the long hours you put into your work—up to 60 hours a week. Your dedication has clearly paid off, as you’ve accumulated a substantial capital gain of $14,084, with no recorded losses. With a Bachelor's degree and 13 years of education, you are likely respected in your field and have a bright future ahead of you. As a native of the United States, you embody the American spirit of hard work and success, reflected in your income of over $50K per year. Your life is a testament to the power of perseverance and education, and you serve as an inspiration to others aspiring to achieve similar levels of professional and personal growth.'''}
    graph = create_graph(personas)
    from IPython.display import Image, display

    try:
        display(Image(graph.get_graph(xray=True).draw_mermaid_png()))
    except:
        # This requires some extra dependencies and is optional
        pass

    events = graph.stream(
        {
            "messages": [
                HumanMessage(
                    content="Let's talk about something interesting. Better first introduce yourself."
                    
                )
            ],
        },
        # Maximum number of steps to take in the graph
        {"recursion_limit": 150},
    )
    for s in events:
        print(s)
        print("----")

