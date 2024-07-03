import pandas as pd
import json
if __name__ == "__main__":
    collections=(f'data/test/math.jsonl')
    collections_data = [json.loads(line) for line in open(collections, 'r')]
    collections_df = pd.json_normalize(collections_data)

    def flatten_pandas(df_):
        #The same as flatten but for pandas

        have_list = df_.columns[df_.applymap(lambda x: isinstance(x, list)).any()].tolist()
        have_dict = df_.columns[df_.applymap(lambda x: isinstance(x, dict)).any()].tolist()
        have_nested = len(have_list) + len(have_dict)
        
        while have_nested!=0:
            if len(have_list)!=0:
                for _ in have_list:
                    df_ = df_.explode(_)
                    
            elif have_dict !=0:
                df_ = pd.json_normalize(json.loads(df_.to_json(force_ascii=False, orient="records")), sep=".")
            
            have_list = df_.columns[df_.applymap(lambda x: isinstance(x, list)).any()].tolist()
            have_dict = df_.columns[df_.applymap(lambda x: isinstance(x, dict)).any()].tolist()
            have_nested = len(have_list) + len(have_dict)
            
        return df_


    flattend = flatten_pandas(collections_df)
    flattend.insert(1, 'question_set', 'math')
    from sqlalchemy import create_engine
    engine =create_engine(r'sqlite:///data/db/agentic_society.db')
    flattend.to_sql(name="questions", con=engine,if_exists='append', index=True)