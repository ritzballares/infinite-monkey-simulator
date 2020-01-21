import random


def generate(length):
    # This function generates characters based on the length parameter

    sentence = ""

    for x in range(length):
        sentence += random.choice("abcdefghijklmnopqrstuvwxyz ")

    return sentence


def calculate_score(monkey_str, goal_str):
    #  This function keeps track and returns the score based on the number of correct matches

    score = 0

    for x in range(1, len(goal_str)+1):
        if monkey_str[:x] == goal_str[:x]:
            score += 1

    return (score)


def main():

    goal_str = input("Enter a phrase: ")
    run_count = best_score = score = 0
    best_sentence = ""

    while(best_score < len(goal_str)):
        # monkey_str keeps track of the remaining length of the string that
        # does not match to goal_str.

        monkey_str = generate(len(goal_str)-best_score)
        score = calculate_score(monkey_str, goal_str[best_score:])

        # Update best score and best guess
        if score > 0:
            best_score += score
            best_sentence += monkey_str[:score]

        run_count += 1
        print(best_sentence)

    print("Total loops: ", run_count)


if __name__ == "__main__":
    main()
