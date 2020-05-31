import random
import time


def generate(length):
    # This function generates a set of characters based on length
    # length = amount of characters to be generated

    sentence = ""

    for x in range(length):
        sentence += random.choice(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")

    return sentence


def calculate_score(monkey_str, goal_str):
    # This function keeps track and returns the score based on the number of correct matches
    # monkey_str = generated set of characters
    # goal_str = set of characters to be matched

    score = 0

    for x in range(1, len(goal_str)+1):
        if monkey_str[:x] == goal_str[:x]:
            score += 1

    return score


def main():

    goal_str = input("Enter a phrase: ")
    run_count = best_score = score = 0
    best_sentence = ""

    # Start tracking time when program starts generating characters
    start_time = time.time()

    # If best_score doesn't equal goal_str (set of characters to be matched), continue generated characters
    while(best_score < len(goal_str)):
        # monkey_str holds the length of charaters to be generated
        # This is calculated by subtracting the length of goal_str from best_score
        monkey_str = generate(len(goal_str)-best_score)
        score = calculate_score(monkey_str, goal_str[best_score:])

        # Update best score and best guess if there's a match (score is greater than 0)
        if score > 0:
            best_score += score
            best_sentence += monkey_str[:score]

        run_count += 1
        print(best_sentence)

    end_time = time.time()  # Program finished generating characters
    total_time = end_time - start_time  # Time it took to match goal_str

    print(f"Total loops: {run_count} ({total_time:.3f}s)")


if __name__ == "__main__":
    main()
