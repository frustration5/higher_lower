from data import data
import logo
import random
import time


# Global variable list of len of data for selecting from for random
data_c = []
data_c.extend(range(0, len(data)))
# Create a starting number to grab from the data dictionary
def grab():
    """
    Takes a random entry in the data list of
    dictionaries and returns it as a dictionary.
    At the same time, this function removes whatever random number was generated
    from the data_c global variable.
    """
    global data_c
    rand = random.choice(data_c)
    data_c.remove(rand)
    #print(data_c)
    to_compare = data[rand]
    return to_compare # Return a dictionary entry from data

def game_start():
    """
    Starts the game by printing the logo and using grab()
    to generate 2 items to compare with compare_1 & compare_2
    :return:
    """
    compare = []
    compare.append(grab())
    #compare.append(grab())
    #print(compare)
    return compare

def comparing():
    """
    Compares the return from game_start()
    :return:
    """
    comp_dict = []
    comp_dict.append(grab())
    i = 1 # Determines which index to use to compare to the correct answer of the previous question.
    i2 = 0 # The index of which i is compared to.
    while True: # Loop to continue to compare until you are wrong.
        end = False
        if end == True: # Break the while loop if there was a wrong answer.
            break
        comp_dict.append(grab())
        print("Alright, who has a larger follower count?")
        print("")
        print("Name: " + comp_dict[i2]['name'])
        print("Follower Count: " + str(comp_dict[i2]['follower_count']) + ",000")
        print("Description: " + comp_dict[i2]['description'])
        print("Country: " + comp_dict[i2]['country'])
        time.sleep(0.5)
        print(logo.vs)
        time.sleep(0.5)
        print("")
        print("Name: " + comp_dict[i]['name'])
        print("Follower Count: " + str(comp_dict[i]['follower_count']) + ",000")
        print("Description: " + comp_dict[i]['description'])
        print("Country: " + comp_dict[i]['country'])
        print("")

        player_guess = input("Does " + comp_dict[i2]['name'] +
                             " have more followers than " + comp_dict[i]['name'] + "? (y/n) ").lower()

        while player_guess != 'y' or player_guess != 'n':
            player_guess = input("Does " + comp_dict[i2]['name'] +
                                 " have more followers than " + comp_dict[i]['name'] + "? (y/n) ").lower()


            if player_guess == 'y': # If you guessed that the first item has greater followers than the second
                if comp_dict[i2]['follower_count'] > comp_dict[i]['follower_count']: # If you are correct or not
                    print("Correct! Next comparison.")
                    i += 1
                    i2 += 1
                else:
                    print("Wrong! You Lose!")
                    end = True
                    break
            elif player_guess == 'n':
                if comp_dict[i]['follower_count'] > comp_dict[i2]['follower_count']: # If you are correct or not
                    print("Correct! Next comparison.")
                    i += 1
                    i2 += 1
                else:
                    print("Wrong! You Lose!")
                    end = True
                    break

def to_begin():
    """
    question to begin the game and play again
    :return:
    """
    print(logo.logo)

    begin_game = input("Ready to begin comparing nonsense people/companies? (y/n) ").lower()
    if begin_game == 'y':
        comparing()
    else:
        print("Cya!")

to_begin()
# You can minus a set from a set to remove ints
# n = [9,2]
# s = set(range(1,8))
# a = list(s - set(n))
# print(s)
# print(a)
