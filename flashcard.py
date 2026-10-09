import random

cards = {
    "Defintion of a photon": "A quantum of electromagnetic energy",
    "2 Equations of photon energy": "E = hf and E = hc/λ",
    "How to photons and electrons interact": "one to one interaction",
}

questions = list(cards.items())
random.shuffle(questions)

def run_quiz(card_list):
    random.shuffle(card_list)
    score = 0
    missed = []
    for question, answer in questions:
      print("\nQ:", question)
      input("Press Enter to reveal the answer...")
      
      result = input("Were you correct? (y/n): ")
      if result.lower() == "y":
         score = score + 1
      else:
         missed.append((question, answer))

    print("\nYou got", score, "out of", len(questions))
    return missed

questions = list(cards.items())
missed = run_quiz(questions)

while len(missed) > 0:
    again = input("\nReview missed cards? (y/n): ")
    if again.lower() != "y":
        break
    missed = run_quiz(missed)

if len(missed) == 0:
    print("\nPerfect! You know all the cards.")
