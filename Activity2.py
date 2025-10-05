class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word}: {self.meaning}"


flash = []
print("Welcome to flashcard application")

while True:
    word = input("Enter the word you want to add to flashcard (or leave empty to stop): ")
    if not word:
        break
    meaning = input("Enter the meaning: ")
    flash.append(Flashcard(word, meaning))

    try:
        option = int(input("Enter 0 to add another flashcard, or 1 to stop: "))
    except ValueError:
        option = 1

    if option:
        break

print("\nYour flashcards are:")
for i in flash:
    print(">", i)