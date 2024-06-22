from asociety.generator.persona_generator import PersonaGeneratorFactory, PersonaGenerator
from asociety.repository.persina_rep import PersonaRepository

if __name__ == "__main__":
    generator:PersonaGenerator = PersonaGeneratorFactory.create()
    samples = generator.sampling(1)
    rep: PersonaRepository = PersonaRepository()
    rep.savePersonas(samples)