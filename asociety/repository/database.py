
from sqlalchemy import create_engine
from asociety import config
model = config.configuration['llm']

if model == 'glm-4':
    dbfile = r'sqlite:///data/db/agentic_society.db'
if model == 'chatgpt4':
    dbfile = r'sqlite:///data/db/agentic_society_chatgpt4.db'
engine =create_engine(dbfile)

