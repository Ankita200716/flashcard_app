import random

cards = {
    "Defintion of a photon": "A quantum of electromagnetic energy",
    "2 Equations of photon energy": "E = hf and E = hc/λ",
    "How to photons and electrons interact": "one to one interaction",
}

questions = list(cards.items())
random.shuffle(questions)

score = 0
missed = []

for question, answer in questions:
    print("\nQ:", question)
    input("Press Enter to reveal the answer...")
    print("A:", answer)
    
    result = input("Were you correct? (y/n): ")
    if result == "y":
        score = score + 1
    else:
        missed.append(question)

print("\nYou got", score, "out of", len(questions))

if len(missed) > 0:
    print("Cards to review:")
    for card in missed:
        print("-", card)
else:
    print("Perfect score!")
