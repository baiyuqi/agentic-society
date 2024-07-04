import pandas as pd
import json
if __name__ == "__main__":
    collections=(f'data/test/test.jsonl')
    collections_data = [json.loads(line) for line in open(collections, 'r')]
    df = pd.json_normalize(collections_data)

    df.insert(1, 'question_set', 'multi-choice')
    df["options"] = 'A: ' + df["A"] + ' \nB: ' + df["B"] + ' \nC: ' + df["C"] + ' \nD: ' + df["D"]
    df = df.drop(columns=['A', 'B','C','D'])
    from sqlalchemy import create_engine
    engine =create_engine(r'sqlite:///data/db/agentic_society.db')
    df.to_sql(name="question", con=engine,if_exists='append', index=False)