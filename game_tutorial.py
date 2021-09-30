#
# Python
#
# Author:   Beatrice Owens
#
#Purpose:   The Tech Academy Python Course; Creating my first Python course.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Function_name (variable) means to pass in a variable.
#           return variable means returning the variable back to the calling function.




def start(nice=0,mean=0,name=""):
    #^defining initial values for 3 variables
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    #^three var passed into nice_mean function, which will return those values back to the variables



def describe_game(name):
    """
        check if this is a new game or not.
        if new, get user's name.
        if not new, thank the player for playing
        and continue the game
    """
    #meaning, if we don't have the user's name,
    #then they're a new player and we need to get the name
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name) #creating a new variable yet to be defined
        pick = input("\nA stranger approaches you for an \nannoying conversation. Will you be nice \nor assertive? (N/A) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "a":
            print("\nThe strangers glares at you \nmenacingly and storms off... \nbut at least you followed your heart.")
            mean = (mean +1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Assertive)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored w/in the 3 var
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function w/var
        lose(nice,mean,name)
    else:   #else, call nice_mean function passing in variables
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    #substitute the {} wildcards with our var values
    print("\nNice job {}! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    #substitute the {} wildcards with our var values
    print("\nCongratulations, {}! \nYou are alone, but you lived \nyour life your way \nand stood up for yourself.".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nIt's cool. Have a good day.")
            stop = False
            quit()
        else:
            print("\nEnter ( y ) for 'YES,' ( n ) for 'NO':\n>>> ")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    #name var not reset since the user decided to play again
    start(nice,mean,name)







if __name__ == "__main__":
    start()
