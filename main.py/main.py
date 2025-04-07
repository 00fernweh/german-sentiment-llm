from transformers import pipeline

# Fertiges Modell zur Analyse von Emotionen auf Deutsch
classifier = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert")

# Holen Sie die Sätze des Benutzers ein und analysieren Sie sie
while True:
    user_input = input("Gib einen Satz auf Deutsch ein (oder 'exit'): ")
    if user_input.lower() == "exit":
        break
    result = classifier(user_input)
    print("Analyse:", result)
