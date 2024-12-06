import pandas as pd
import json
if __name__ == "__main__":
    with open('data/IPIP-NEO/120/questions.json') as pjson:
            collections_data = json.load(pjson)
    questions = collections_data['questions']
    select = collections_data['select']
    options = ''
    for e in select:
          item = str(e['id']) + ': ' + e['text'] + '\n'
          options+= item
    df = pd.json_normalize(questions)
    df['standard_id'] = df['id']
    df['question'] = df['text']
    df = df.drop(columns=['id','text'])
    df['options'] = options

    df.insert(1, 'question_set', 'ipip_neo_120')
  
    from asociety.repository.database import engine

    df.to_sql(name="question", con=engine,if_exists='append', index=False)