# spelling guessing game using while loop

print('what is the correct english spelling of the numer \'11\' is?')
answer = 'eleven'
guess = ""
limit = 3
trial = 0

while guess.lower() != answer.lower():
    guess = input('please enter your answer: ')
    if guess.lower() != answer.lower():
        trial += 1
        if trial >= limit:
            print('sorry bro, you reached the limit :(, btw the correct answer was', answer)
            exit()
        else:
            print('try again!!')
    else:
        print('well done bruv :)')
