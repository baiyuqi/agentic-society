from asociety.generator.persona_skeleton_generator import *
from asociety.generator.persona_generator import PersonaGeneratorFactory
class FixedSkeletonGenerator:
    def __init__(self) -> None:
        
        self.skeleton = self.getSkeleton()
        self.generator = PersonaGeneratorFactory.create()

    def getSkeleton(self):
         pass
    def sampling(self, n):
        rst = []
        for i in range(0, n):
            rst.append(self.generator.llm_enrich(self.skeleton))
        return rst
class RandomFixedSkeletonGenerator(FixedSkeletonGenerator):
    def __init__(self) -> None:
        super()
    def getSkeleton(self):
        skeletonGenerator = PersonaSkeletonGeneratorFactory.create()
        skel = skeletonGenerator.sampling(1)
        obj = {}
        keys = skel.keys();

        for key in keys:
                if(key in ["fnlwgt","probability"]):
                    continue
                obj[key] = skel[key]
        return obj
class PresetFixedSkeletonGenerator(FixedSkeletonGenerator):
    def __init__(self, skeleton) -> None:
        super()
        self.skeleton = skeleton
    def getSkeleton(self):
        
        return self.skeleton