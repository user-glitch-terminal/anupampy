import friendlywords as fw

s_word = fw.generate(1).lower()
g_words = []
tries = 5
d_words = ["_" for _ in s_word]

print("Welcome to word guessing game")
print(f"You have {tries} tries left")

while tries > 0 and "_" in d_words:
    print("Word: " + "".join(d_words))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet\n")
        continue

    if guess in g_words:
        print("You already guessed that\n")
        continue

    g_words.append(guess)

    if guess in s_word:
        print("Correct\n")
        for i, ch in enumerate(s_word):
            if ch == guess:
                d_words[i] = guess
    else:
        tries -= 1
        print(f"Wrong! YOU HAVE {tries} tries")

    if "_" not in d_words:
        print("You won")
        break
else:
    print(f"You lost! The word was {s_word}")
