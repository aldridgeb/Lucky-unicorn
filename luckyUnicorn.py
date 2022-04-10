import random

def yes_no(question_text):
    while True:

        answer = input(question_text).lower()

        if answer == "yes" or answer == "y":
            answer = "yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "no"
            return answer

        else:
            print("please answer 'yes' or 'no'")

            def instructions():
                print()
                print(formatter("*", "how to play"))
                print()
                print("choose a starting ammount to play with 0 must be between $1 and $10")
                print()
                print("then press <enter> to play you will get a rendom token witch might"
                      "be a horse a zebra a donkey or a unicorn ")
                print()
                print()
