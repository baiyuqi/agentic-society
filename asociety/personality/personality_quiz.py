
import json
import random
import sys
import urllib.request
from itertools import chain, repeat
from asociety.personality.ipipneo import IpipNeo

class PersonalityResult:
    def __init__(self, result) -> None:
        self.data = result


        big5 =self.data.get("person").get("result").get("personalities")


        E = [
            "EXTRAVERSION",
            "Friendliness",
            "Gregariousness",
            "Assertiveness",
            "Activity Level",
            "Excitement-Seeking",
            "Cheerfulness",
        ]

        ed =    [
                int(big5[2].get("extraversion").get("E")),
                int(big5[2].get("extraversion").get("traits")[0].get("friendliness")),
                int(big5[2].get("extraversion").get("traits")[1].get("gregariousness")),
                int(big5[2].get("extraversion").get("traits")[2].get("assertiveness")),
                int(big5[2].get("extraversion").get("traits")[3].get("activity_level")),
                int(
                    big5[2]
                    .get("extraversion")
                    .get("traits")[4]
                    .get("excitement_seeking")
                ),
                int(big5[2].get("extraversion").get("traits")[5].get("cheerfulness")),
            ]
        self.E = {E[i]:ed[i] for i in range(0, 7)}
        
        A = [
            "AGREEABLENESS",
            "Trust",
            "Morality",
            "Altruism",
            "Cooperation",
            "Modesty",
            "Sympathy",
        ]

        ad =    [
                int(big5[3].get("agreeableness").get("A")),
                int(big5[3].get("agreeableness").get("traits")[0].get("trust")),
                int(big5[3].get("agreeableness").get("traits")[1].get("morality")),
                int(big5[3].get("agreeableness").get("traits")[2].get("altruism")),
                int(big5[3].get("agreeableness").get("traits")[3].get("cooperation")),
                int(big5[3].get("agreeableness").get("traits")[4].get("modesty")),
                int(big5[3].get("agreeableness").get("traits")[5].get("sympathy")),
            ]
        self.A = {A[i]:ad[i] for i in range(0, 7)}
        C = [
            "CONSCIENTIOUSNESS",
            "Self-Efficacy",
            "Orderliness",
            "Dutifulness",
            "Achievement-Striving",
            "Self-Discipline",
            "Cautiousness",
        ]

        cd =    [
                int(big5[1].get("conscientiousness").get("C")),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[0]
                    .get("self_efficacy")
                ),
                int(
                    big5[1].get("conscientiousness").get("traits")[1].get("orderliness")
                ),
                int(
                    big5[1].get("conscientiousness").get("traits")[2].get("dutifulness")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[3]
                    .get("achievement_striving")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[4]
                    .get("self_discipline")
                ),
                int(
                    big5[1]
                    .get("conscientiousness")
                    .get("traits")[5]
                    .get("cautiousness")
                ),
            ]
        self.C = {C[i]:cd[i] for i in range(0, 7)}
        N = [
            "NEUROTICISM",
            "Anxiety",
            "Anger",
            "Depression",
            "Self-Consciousness",
            "Immoderation",
            "Vulnerability",
        ]

        nd =    [
                int(big5[4].get("neuroticism").get("N")),
                int(big5[4].get("neuroticism").get("traits")[0].get("anxiety")),
                int(big5[4].get("neuroticism").get("traits")[1].get("anger")),
                int(big5[4].get("neuroticism").get("traits")[2].get("depression")),
                int(
                    big5[4]
                    .get("neuroticism")
                    .get("traits")[3]
                    .get("self_consciousness")
                ),
                int(big5[4].get("neuroticism").get("traits")[4].get("immoderation")),
                int(big5[4].get("neuroticism").get("traits")[5].get("vulnerability")),
            ]
        
        self.N = {N[i]:nd[i] for i in range(0, 7)}
        O = [
            "OPENNESS",
            "Imagination",
            "Artistic Interests",
            "Emotionality",
            "Adventurousness",
            "Intellect",
            "Liberalism",
        ]

        od = [
                int(big5[0].get("openness").get("O")),
                int(big5[0].get("openness").get("traits")[0].get("imagination")),
                int(big5[0].get("openness").get("traits")[1].get("artistic_interests")),
                int(big5[0].get("openness").get("traits")[2].get("emotionality")),
                int(big5[0].get("openness").get("traits")[3].get("adventurousness")),
                int(big5[0].get("openness").get("traits")[4].get("intellect")),
                int(big5[0].get("openness").get("traits")[5].get("liberalism")),
            ]
        self.O = {O[i]:od[i] for i in range(0, 7)}