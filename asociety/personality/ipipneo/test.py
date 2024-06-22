import json
from asociety.personality.ipipneo import IpipNeo
with open('data/IPIP-NEO/120/answers.json') as fp:
    data = json.load(fp)

answers = data['answers']
result = IpipNeo(120).compute(
        sex='F', age=65, answers={"answers": answers}, compare=True
    )
print(result)