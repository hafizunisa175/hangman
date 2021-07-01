def start():
    print("Lets play hangman")
    word_finished= "_"*len(word)
    tries=6
    g=False
    print(display_hangman(tries))
    print(word_finished)
    letters_done=[] #letters already guessed
    words_done=[]   #words already guessed
    while not g and tries>0:
        print(word_finished)
        your_guess=input(">").upper()
        if len(your_guess)==1 and your_guess.isalpha():
            if your_guess in letters_done:
                print("You already guessed the letter try another one")
            elif your_guess not in word:
                print("Nops not the correct letter")
                print("Try another one")
                letters_done.append(your_guess)
                tries-=1
                print(display_hangman(tries))
            else:
                print("Great guess "+your_guess+" is in the word")
                letters_done.append(your_guess)
                word_list=list(word_finished)
                indices = [i for i, letter in enumerate(word) if letter == your_guess]
                for i in indices:
                    word_list[i]=your_guess
                word_finished="".join(word_list)
                if '_' not in word_finished:
                    g=True
        elif(len(your_guess)==len(word) and your_guess.isalpha()):
            if(your_guess in words_done):
                print("You already guessed the word try another one")
            elif(your_guess not in word):
                print("Nops not the correct word")
                print("Try another one")
                words_done.append(your_guess)
                tries-=1
                print(display_hangman(tries))    
            else:
                g=True
                word_finished=word
        else:
            print("Not a valid guess")
    print(word_finished)
    print("\n")  
    if g:
        print("Congrats, you guessed the word! You win!")
        print(display_hangman(tries))
    else:

        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
                

          
          
def main():
    getWord()
    start()
    ch=input("DO you wanna play furtur Y/N? ").upper()
    if(ch=='Y'):
        getWord()
        start()
    else: exit()    


if __name__ == "__main__":
    main()                  
          
