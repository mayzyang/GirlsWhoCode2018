while True:
    word = input("Type a word for someone to guess: ")
    word = word.lower()
    if(word.isalpha() == False):
        print("That's not a word")
    else:
        break

guesses = []
numFails  = 0
maxFails = 7
wordToGuess = []

for letter in word:
    wordToGuess.append("_")

for i in range(0, 20):
    print(" ")

done = False;

while not done:
    print ("------------------------------")
    print("Lives left: ", maxFails - numFails)
    print("Guesses so far: ", guesses)
    print("Current word: ", wordToGuess)

    guess = input("Guess a letter: ")
    guess = guess.lower()

    if(len(guess) > 1):
        print("too long")
    elif(guess.isalpha() == False):
        print("thats not a letter")
    elif(guess in guesses):
        print("you already guessed that!")
    else:
        guesses.append(guess)

        if(guess in word):
            print("you got a letter!")
            for i in range(0, len(word)):
                if word[i] == guess:
                    wordToGuess[i] = guess;
            done = True
            for i in range(0, len(wordToGuess)):
                if wordToGuess[i] == "_":
                    done = False
                    break
            if done:
                print("You won!")
        else:
            print("Wrong Guess!")
            numFails += 1

            if numFails >= maxFails:
                print("you lost!")
                done = True
