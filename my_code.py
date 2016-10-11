# blanks are associated with their respective games and answers
easy_blanks = ["__1__", "__2__", "__3__", "__4__"]
medium_blanks = ["__1__", "__2__", "__3__", "__4__"]
hard_blanks = ["__1__", "__2__", "__3__", "__4__"]

easy_game ="""Hello __1__! a message that is commonly use when you first begin programming.
Many beginners start with the standard markup language __2__ to create web pages
and web applications. Once HTML is nicely structured, you can apply __3__ to style the
HTML document. Lets not forget __4__, a popular client side scripting language."""

easy_answers = ["world", "html", "css", "javascript"]

medium_game ="""A __1__ is used to store information to be referenced and manipulated
 in a computer program. Sometimes a __2__, a sequence of characters are assigned
 to the variable. In python, a __3__ is created with the def keyword. Functions
provide better modularity for your __4__ and a high degree of code reusing."""

medium_answers = ["variable", "string", "function", "application"]

hard_game ="""A __1__ is the most versatile datatype available in Python. An __2__ statement
contains the block of code that executes if the conditional expression in the
if statement resolve to 0 or a False value. __3__ loops, like the __4__ loop, are
used __4__ repeating sections of code, unlike a __4__ loop, th __3__ loop will not return
n times but until a defined condition is met."""

hard_answers =["list","else","while","for"]

def game_setup(user_select):
    if user_select == "easy" or user_select == "Easy":
        return easy_game, easy_blanks, easy_answers
    elif user_select == "medium" or user_select == "Medium":
        return medium_game, medium_blanks, medium_answers
    elif user_select == "hard" or user_select == "Hard":
        return hard_game, hard_blanks, hard_answers
        print "Error"

# Takes user_select and outputs the selected game with the answer choices.
def start_game():
    user_select = raw_input("Please select a game difficulty by typing it in!"+
    "\n" +"Possible choices include easy, medium and hard"+"\n")
    print "Fantastic!"+"\n" +"\n" + "You will get 5 guesses per problem" +"\n"
    text, blanks, choices = game_setup(user_select)
    print text
    current_idex = 0
    tries = 5
    current_try = 0
    while current_idex < len(blanks):
    	if current_try >= tries:
    		print "Sorry you ran out of guesses"
    		end_game()
        user_choice = raw_input("What should be substitued in for " + blanks[current_idex] + "? ")
        if user_choice.lower() == choices[current_idex].lower():
        	text.replace(blanks[current_idex], user_choice)
        	print "Correct!"
        	current_idex += 1
        else:
            print "Try Again!"
            current_try += 1
    else:
    	end_game()

#After user completes the game,user will can select to play new game or exit.
def end_game():
	user_three = raw_input("New Game (1) or Exit (2)?")
    if user_three == "1"
    	start_game()
    print "Goodbye! Thank you for playing!"
        quit()


start_game()
