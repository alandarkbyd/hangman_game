import random
swd = ['snake', 'mango', 'carry', 'pocket', 'watch', 'random', 'floor', 'flash', 'field', 'walk', 'rule', 'drive', 'match', 'blur', 'black', 'brain']
swe = [x.upper() for x in swd]
word = random.choice(swe) #'anime'
guess = []
chances = 6
phase = 0
state = False
hint = [
	"an animal",
	"a fruit",
	"which is used when we move something from one place to another",
	"it's a characteristic of your dress",
	"a machine in your hand",
	"not sure",
	"where you walk inside your home",
	"light from clouds",
	"let's go to play",
	"use your two legs",
	"you have to follow to be gentle",
	"what do you do when you want to go somewhere through a car?",
	"it's vs",
	"i can't see it",
	"your hairs",
	"topper most important part"	
]

satisfyHint = ""

def wordChose():
	global satisfyHint, word
	satisfyHint = hint[swe.index(word)]

wordChose()

def choice_section():
    global state
    while not state:
        choice = input("""How do you want to visualize your lives?
		1. Chances refered by numbers
		2. Hang the man
		3. Quit
		Your Choice: """)
        if choice == '1':
            number_chances()
            state = True
        elif choice == '2':
            
            hangThe_man()
            state = True
        elif choice == '3':
            state = True
        else:
            print('Invalid Choice')



def checkall(x):
        global word
        for ch in word:
            if ch not in x:
                return False
        return True

	
def hangThe_man():
    global chances, phase, word
    print('''
    ____________
    |          |
    |          |
    |          
    |         
    |         
    |
    |
    |
    |
    |
    ----''')
    p1 = '''
	____________
	|          |
	|		   |
	|		   O
	|         
	|		  
	|
	|
	|
	|
	|
	----'''
    p2 = '''
	____________
	|          |
	|		   |
	|		   O
	|          |
	|		  
	|
	|
	|
	|
	|
	----'''
    p3 = '''
	____________
	|          |
	|		   |
	|		   O
	|         /|
	|		  
	|
	|
	|
	|
	|
	----'''

    p4 = '''
	____________
	|          |
	|		   |
	|		   O
	|         /|\\
	|		  
	|
	|
	|
	|
	|
	----'''
    p5 = '''
	____________
	|          |
	|		   |
	|		   O
	|         /|\\
	|		  / 
	|
	|
	|
	|
	|
	----'''
    p6 = '''
	____________
	|          |
	|		   |
	|		   O
	|         /|\\
	|		  / \\
	|
	|
	|
	|
	|
	----'''

    

    print('The word structure is like this: \t', end='')
    for k in word:
        print('_', end=' ')
    print(f"""\n:Guess the word correctly to win the game!\n You have to guess the word before the man got hang!\nHint: {satisfyHint}""")
    while True:
        user_input = input('Enter your character: ').upper()
        guess.append(user_input)
        b = guess.count(user_input)
        if user_input in word:
            if b > 1:
                chances += 1

        if user_input not in word:
            phase += 1

        for char in word:
            if char in guess:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        ans = checkall(guess)
        if ans == True:
            print('All guessed words are correct')
            print("You have won the game🎉")
            break


        if user_input not in word:
            if phase == 1:
                print(p1)
            if phase == 2:
                print(p2)
            if phase == 3:
                print(p3)
            if phase == 4:
                print(p4)
            if phase == 5:
                print(p5)
            if phase == 6:
                print(p6)

        if phase == 6:  # chances == 0:
            print("You are failed to rescue the man from being hanged !")
            print("The secret word was: ", word)
            break


def number_chances():
    global chances, phase

    print('The word structure is like this: \t', end='')
    for k in word:
        print('_', end=' ')
    print(f"""\n:Guess the word correctly to win the game!\n You will have {chances} chances to guess each word!\nHint: {satisfyHint}""")
    while True:
        user_input = input('Enter your character: ').upper()
        guess.append(user_input)
        b = guess.count(user_input)
        if user_input in word:
            if b > 1:
                chances += 1

        if user_input not in word:
            chances = chances - 1
        for char in word:
            if char in guess:
                print(char, end=' ')
            else:
                print('_', end=' ')
        print()

        ans = checkall(guess)
        if ans == True:
            print('All guessed words are correct')
            print("You have won the game🎉")
            break

        # chances = chances - 1

        if chances > 1:
            print(f'Now you have {chances} chances')
        elif chances == 1:
            print(f'You just have {chances} more chance left')

        if chances == 0:  # phase == 6:
            print("Your chances are over to guess the secret word and you have lost the game!")
            print("The secret word was: ", word)
            break


choice_section()
