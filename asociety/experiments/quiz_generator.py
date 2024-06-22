
class QuizGenerator:
    def __init__(self,question_group) -> None:
        self.question_group = question_group
    def generateQuiz(self):
        from asociety.repository.database import engine
        from asociety.repository.experiment_rep import QuestionGroup,Question

        from sqlalchemy.orm import Session
        with Session(engine) as session:
            qg = session.query(QuestionGroup).filter(QuestionGroup.name == self.question_group).one()
            qids = qg.questions.split(",")
            length = len(qids)
            n = length/20
            r = length%20
            if(r != 0):
                n = n+ 1
            import numpy as np
            subs = np.array_split(qids, n)
            result = []
            for sub in subs:
                subs = self.generateSubQuiz(sub)
                result.append(subs)
            return result


    def generateSubQuiz(self, sub):
        from asociety.repository.database import engine
        from asociety.repository.experiment_rep import QuestionGroup,Question

        from sqlalchemy.orm import Session
        sheet = ''
        with Session(engine) as session:
            
            count = 1
            for qid in sub:
                q = session.get_one(Question, qid)
                sheet += '\n\n' + str(count) + ': ' +  q.question
                sheet += '\nFollwing are options = choose from:\n'
                sheet += q.options
                count = count + 1
        return sheet
        
sheet = QuizGenerator('ipip').generateQuiz()
print(sheet)
