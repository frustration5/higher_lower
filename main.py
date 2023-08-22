from data import data
import logo
import random
import time


# TODO
# 1. When progressing through the game the next comparison always uses the last compared to index

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
    first_item = 1  # Determines which index to use to compare to the correct answer of the previous question.
    second_item = 0  # The index of which first_item is compared to.
    end = False
    while True:  # Loop to continue to compare until you are wrong.
        lg_fol_cnt = []  # List of dictionaries of comp_dict with the largest follower count.
        if end == True:  # Break the while loop if there was a wrong answer.
            break
        comp_dict.append(grab())
        print("Alright, who has a larger follower count?")
        print("")
        print("Name: " + comp_dict[second_item]['name'])
        print("Follower Count: " + str(comp_dict[second_item]['follower_count']) + ",000")
        print("Description: " + comp_dict[second_item]['description'])
        print("Country: " + comp_dict[second_item]['country'])
        time.sleep(0.5)
        print(logo.vs)
        time.sleep(0.5)
        print("")
        print("Name: " + comp_dict[first_item]['name'])
        print("Follower Count: " + str(comp_dict[first_item]['follower_count']) + ",000")
        print("Description: " + comp_dict[first_item]['description'])
        print("Country: " + comp_dict[first_item]['country'])
        print("")

        while len(lg_fol_cnt) < 1:  # Compares the dictionaries when the list lg_fol_count is larger than 1.
            player_guess = input("Does " + comp_dict[second_item]['name'] +
                                 " have more followers than " + comp_dict[first_item]['name'] + "? (y/n) ").lower()

            if player_guess == 'y':  # If you guessed that the first item has greater followers than the second
                if comp_dict[second_item]['follower_count'] > comp_dict[first_item]['follower_count']:  # If you are correct or not
                    print("Correct! Next comparison.")
                    lg_fol_cnt.append(comp_dict[second_item])
                    first_item += 1
                    second_item += 1
                    break
                else:
                    print("Wrong! You Lose!")
                    end = True
                    break
            elif player_guess == 'n':
                if comp_dict[first_item]['follower_count'] > comp_dict[second_item]['follower_count']:  # If you are correct or not
                    print("Correct! Next comparison.")
                    lg_fol_cnt.append(comp_dict[first_item])
                    first_item += 1
                    second_item += 1
                    break
                else:
                    print("Wrong! You Lose!")
                    end = True
                    break

        while len(lg_fol_cnt) > 1:
            player_guess = input("Does " + comp_dict[second_item]['name'] +
                                 " have more followers than " + comp_dict[first_item]['name'] + "? (y/n) ").lower()

            if player_guess == 'y':  # If you guessed that the first item has greater followers than the second
                if comp_dict[second_item]['follower_count'] > comp_dict[first_item]['follower_count']:  # If you are correct or not
                    print("Correct! Next comparison.")
                    lg_fol_cnt.append(comp_dict[second_item])
                    first_item += 1
                    second_item += 1
                    break
                else:
                    print("Wrong! You Lose!")
                    end = True
                    break
            elif player_guess == 'n':
                if comp_dict[first_item]['follower_count'] > comp_dict[second_item]['follower_count']:  # If you are correct or not
                    print("Correct! Next comparison.")
                    lg_fol_cnt.append(comp_dict[first_item])
                    first_item += 1
                    second_item += 1
                    break
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
