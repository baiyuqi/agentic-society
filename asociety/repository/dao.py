
def extract_personas_of_experiment(experiment_name):
    from asociety.repository.database import engine

    from sqlalchemy.orm import Session
    from asociety.repository.experiment_rep import QuizAnswer
    from asociety.repository.persina_rep import Persona
    with Session(engine) as session:
        ps = session.query(QuizAnswer.persona_id).filter(QuizAnswer.experiment_name==experiment_name).distinct()
        rst = []
        for p in ps:
            persona = session.query(Persona).get(p)
            rst.append(persona)
        return rst