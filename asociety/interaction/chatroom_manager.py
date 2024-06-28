

from langchain_core.messages import (
    BaseMessage,
    ToolMessage,
    HumanMessage,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, StateGraph
latest_state = None
def get_summary(graph: StateGraph):
    if not latest_state:
        return None
    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()
    from asociety.generator.llm_engine import llm, summary, friend
    chain = summary | llm |output_parser
    resp = chain.invoke(latest_state)
    return resp
def get_friends(persona, sum,nickname):
    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()
    from asociety.generator.llm_engine import llm, summary, friend
    chain = friend | llm |output_parser
    resp = chain.invoke({'persona':persona.persona, 'summary':sum,'nickname':nickname})
    return resp
def select_personas(n):
    from asociety.repository.persina_rep import Persona
    from asociety.repository.database import engine
    from sqlalchemy.orm import Session
    with Session(engine) as session:
        ps = session.query(Persona).all()
        data = {p.id: p.persona_desc for p in ps }
        eve = [p.id for p in ps]
        import random
        selected = random.choices(eve, k=n)
        
        rst =    {id:data[id] for id in selected }
        return rst

def create_agent(llm, name, persona: str):
    """Create an agent."""
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                
               
                "{persona}Now you are inside a chatroom. Prefix your message with #yournickname. You can use @ to address somebody or just publish a message without specifying a person.For example, if you are chatter1 and want to address chatter2, start with \'#chatter1:\n@chatter2\'.\n"
                "Your nickname is {name}\n"
                "If you don't want to speak, just respond with \'silence\'\n"
                "If you want to go away, just respond with \'exit\'\n"
                "If you want to add fiend, just respond with \'add-friend: #friend nickname\'\n"
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

data = [1,2,3,4,5,6]
del data[0:3]
# Helper function to create a node for a given agent
def agent_node(state, agent, name,listener):
    import copy
    mcopy: AgentState = copy.deepcopy(state)
    length = len(mcopy["messages"])
    if length > 4:
        del mcopy["messages"][1:length - 3]
    #result = agent.invoke(state)
    #result = AIMessage(**result.dict(exclude={"type", "name"}), name=name)
    result = AIMessage(content="hello world!", name=name)
    if(listener != None):
        listener(result.content)

    if result.content == '':
        return {}
    return {
        "messages": [result],
        # Since we have a strict workflow, we can
        # track the sender so we know who to pass to next.
        "sender": name,
    }

from asociety.generator.llm_engine import llm


# Either agent can decide to end
from typing import Literal

from collections import deque
atqueue = deque()

def extract_at(msg):
    import re
    swords = re.findall(r'@\w+\d+', msg)
    atqueue.extend(swords)

def router(state, personas) :
    global latest_state
    latest_state = state
    msg = state['messages'][-1].content
    extract_at(msg)
    if  atqueue:
        at = atqueue.pop()
        return at[1:]
    # This is the router
    import random
    data = []
    mmm = list(personas.keys())
    for m in mmm:
        if(m != state['sender']):
            data.append(m)
    return random.choice(data)
    

def create_graph(personas, message_listener):
    chatters = {}
    routerd = {}
    for i, (k,v) in enumerate(personas.items()):
        name = "chatter" + str(k)
        agent = create_agent(
            llm,
            name,
            persona=v

        )
       
        chatter = functools.partial(agent_node, agent=agent, name=name,  listener = message_listener)
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
    
    starter = 'chatter' + str(list(personas.keys())[0])
    workflow.set_entry_point(starter)
    graph = workflow.compile()
    return graph


if __name__ == "__main__": 
    personas = select_personas(3)
    graph = create_graph(personas, message_listener=None)
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
                    content="Let's talk about something interesting"
                    
                )
            ],
        },
        # Maximum number of steps to take in the graph
        {"recursion_limit": 5},
    )
    for s in events:
        print(s)
        print("----")

