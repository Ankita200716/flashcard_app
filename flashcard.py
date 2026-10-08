import random

cards = {
    "Defintion of a photon": "A quantum of electromagnetic energy",
    "2 Equations of photon energy": "E = hf and E = hc/λ",
    "How to photons and electrons interact": "one to one interaction",
}

questions = list(cards.items())
random.shuffle(questions)

for question, answer in questions:
    print("\nQ:", question)
    input("Press Enter to reveal the answer...")
    print("A:", answer)