
from sqlalchemy import create_engine
from asociety import config
database = config.configuration['database']


dbfile = r'sqlite:///data/db/' + database + '.db'
from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass

engine =create_engine(dbfile)


from asociety.repository.experiment_rep import *
from asociety.repository.personality_rep import *
from asociety.repository.socializing_rep import *
Base.metadata.create_all(engine)
