import random
import json

sets = {
    "1": ("Maths", "cards_maths.json"),
    "2": ("Physics", "cards_physics.json"),
}

def run_quiz(card_list):
    random.shuffle(card_list)
    score = 0
    missed = []
    
    for question, answer in card_list:
        print("\nQ:", question)
        input("Press Enter to reveal the answer...")
        print("A:", answer)
      
        result = input("Were you correct? (y/n): ")
        if result.lower() == "y":
          score = score + 1
        else:
          missed.append((question, answer))

    print("\nYou got", score, "out of", len(card_list))
    return missed

print("Which set do you want to study?")
for number, (name, filename) in sets.items():
    print(number + ". " + name)

choice = input("Enter a number: ")
while choice not in sets:
    choice = input("Invalid choice. Enter a number: ")

name, filename = sets[choice]

with open(filename, encoding="utf-8") as f:
    cards = json.load(f)

print("\nStudying:", name)


questions = list(cards.items())
missed = run_quiz(questions)

while len(missed) > 0:
    again = input("\nReview missed cards? (y/n): ")
    if again.lower() != "y":
        break
    missed = run_quiz(missed)

if len(missed) == 0:
    print("\nPerfect! You know all the cards.")
