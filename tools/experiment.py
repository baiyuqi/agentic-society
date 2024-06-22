from asociety.experiments.experiment_generator import ExperimentGenerator
from asociety.experiments.question_anserer import QuestionAnwserer

if __name__ == "__main__":
    expGenerator:ExperimentGenerator = ExperimentGenerator("math")
    exp = expGenerator.generateExperiment("xxx", 1,1,3)
    for i, p in exp.personas.iterrows():
        for j, q in exp.questions.iterrows():

            exe: QuestionAnwserer = QuestionAnwserer(p, q)
            anwser = exe.getAnwser()
