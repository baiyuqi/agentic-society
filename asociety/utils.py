from asociety.repository.database import engine
def question_set_by_experiment_name(ename):
    sql = 'select qg.question_set from experiment as e, question_group as qg where e.question_group = qg.name and e.name = \''+ ename + '\''
    from asociety.repository.database import engine
    from sqlalchemy.orm import Session
    from sqlalchemy import text
    
    from sqlalchemy import select
    with engine.connect() as con:
            qa =  con.execute(text(sql)).scalar_one()
            return qa