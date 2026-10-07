import random


# ==========================================
# FUNCTION TO DISPLAY SCORE
# ==========================================

def display_score(name, score, wickets, balls, max_balls):
    overs = balls // 6
    remaining_balls = balls % 6

    print("\n--------------------------------")
    print(name, ":", score, "/", wickets)
    print("Overs:", overs, ".", remaining_balls,"/", max_balls // 6, "overs")
    print("--------------------------------")


# ==========================================
# FUNCTION TO GET A NUMBER FROM USER
# ==========================================

def get_number(message, minimum, maximum):

    while True:
        try:
            number = int(input(message))

            if minimum <= number <= maximum:
                return number
            else:
                print("Please enter a number between",minimum, "and", maximum)

        except ValueError:
            print("Please enter a valid number.")


# ==========================================
# MAIN GAME
# ==========================================

def play_game():

    print("\n========================================")
    print(" WELCOME TO HAND CRICKET")
    print("========================================")

    name = input("Enter your name: ")

    # --------------------------------------
    # MATCH SETTINGS
    # --------------------------------------

    print("\n========== MATCH SETTINGS ==========")

    wickets_limit = get_number(
        "Enter number of wickets (1-10): ", 1, 10)

    overs_limit = get_number(
        "Enter number of overs (1-10): ", 1, 10)

    max_balls = overs_limit * 6

    print("\nMatch Settings:")
    print("Wickets :", wickets_limit)
    print("Overs :", overs_limit)

    print("\nRULES")
    print("• Choose a number from 1 to 6.")
    print("• Computer also chooses a number.")
    print("• Same number = WICKET.")
    print("• Different numbers = runs are scored.")
    print("• Innings ends when all wickets are lost")
    print(" or the selected number of overs is completed.")

    # --------------------------------------
    # TOSS
    # --------------------------------------

    print("\n========== TOSS ==========")

    while True:
        toss_choice = input("Choose Odd or Even: ").lower()

        if toss_choice == "odd" or toss_choice == "even":
            break

        print("Please enter Odd or Even.")

    toss_number = get_number("Choose a number for toss (1-6): ", 1, 6)

    computer_toss = random.randint(1, 6)

    print("\nYou chose:", toss_number)
    print("Computer chose:", computer_toss)

    toss_sum = toss_number + computer_toss

    if toss_sum % 2 == 0:
        toss_result = "even"
    else:
        toss_result = "odd"

    print("Toss result:", toss_result.upper())

    # --------------------------------------
    # DECIDE WHO BATS FIRST
    # --------------------------------------

    if toss_result == toss_choice:

        print("\n🎉 You won the toss!")

        while True:
            decision = input(
                "Do you want to Bat or Bowl? ").lower()

            if decision == "bat" or decision == "bowl":
                break

            print("Please enter Bat or Bowl.")

        if decision == "bat":
            player_bats_first = True
        else:
            player_bats_first = False

    else:

        print("\nComputer won the toss!")

        computer_decision = random.choice(["bat", "bowl"])

        print("Computer chooses to",computer_decision.upper())
        
        if computer_decision == "bat":
            player_bats_first = False
        else:
            player_bats_first = True

    # --------------------------------------
    # INITIAL SCORES
    # --------------------------------------

    player_score = 0
    computer_score = 0

    player_wickets = 0
    computer_wickets = 0

    player_balls = 0
    computer_balls = 0

    # ======================================
    # PLAYER BATS FIRST
    # ======================================

    if player_bats_first:

        # ----------------------------------
        # PLAYER'S INNINGS
        # ----------------------------------

        print("\n========================================")
        print(" YOUR INNINGS")
        print("========================================")

        while (player_wickets < wickets_limit and player_balls < max_balls):

            display_score(
                name,
                player_score,
                player_wickets,
                player_balls,
                max_balls
            )

            player_run = get_number("Choose your run (1-6): ", 1, 6)

            computer_run = random.randint(1, 6)

            print("Computer played:", computer_run)

            player_balls += 1

            if player_run == computer_run:

                player_wickets += 1

                print("\n⚡ WICKET!")
                print("You lost a wicket!")

            else:

                player_score += player_run

                print("You scored",player_run,"run(s).")

        print("\n========================================")
        print(" YOUR INNINGS IS OVER")
        print("========================================")

        display_score(
            name,
            player_score,
            player_wickets,
            player_balls,
            max_balls
        )

        target = player_score + 1

        # ----------------------------------
        # COMPUTER'S INNINGS
        # ----------------------------------

        print("\n========================================")
        print(" COMPUTER'S INNINGS")
        print(" TARGET:", target)
        print("========================================")

        while (computer_wickets < wickets_limit and computer_balls < max_balls):

            display_score(
                "Computer",
                computer_score,
                computer_wickets,
                computer_balls,
                max_balls
            )

            computer_run = random.randint(1, 6)

            player_run = get_number("Choose your bowl (1-6): ", 1, 6)

            print("Computer played:", computer_run)

            computer_balls += 1

            if player_run == computer_run:

                computer_wickets += 1

                print("\n⚡ WICKET!")
                print("Computer lost a wicket!")

            else:

                computer_score += computer_run

                print(
                    "Computer scored",
                    computer_run,
                    "run(s)."
                )

                # Target reached
                if computer_score >= target:
                    break

        print("\n========================================")
        print(" COMPUTER'S INNINGS IS OVER")
        print("========================================")

        display_score(
            "Computer",
            computer_score,
            computer_wickets,
            computer_balls,
            max_balls
        )

    # ======================================
    # COMPUTER BATS FIRST
    # ======================================

    else:

        # ----------------------------------
        # COMPUTER'S INNINGS
        # ----------------------------------

        print("\n========================================")
        print(" COMPUTER'S INNINGS")
        print("========================================")

        while (computer_wickets < wickets_limit and computer_balls < max_balls):

            display_score(
                "Computer",
                computer_score,
                computer_wickets,
                computer_balls,
                max_balls
            )

            computer_run = random.randint(1, 6)

            player_run = get_number("Choose your bowl (1-6): ", 1, 6)

            print("Computer played:", computer_run)

            computer_balls += 1

            if player_run == computer_run:

                computer_wickets += 1

                print("\n⚡ WICKET!")
                print("Computer lost a wicket!")

            else:

                computer_score += computer_run

                print(
                    "Computer scored",
                    computer_run,
                    "run(s)."
                )

        print("\n========================================")
        print(" COMPUTER'S INNINGS IS OVER")
        print("========================================")

        display_score(
            "Computer",
            computer_score,
            computer_wickets,
            computer_balls,
            max_balls
        )

        target = computer_score + 1

        # ----------------------------------
        # PLAYER'S INNINGS
        # ----------------------------------

        print("\n========================================")
        print(" YOUR INNINGS")
        print(" TARGET:", target)
        print("========================================")

        while (player_wickets < wickets_limit and player_balls < max_balls):

            display_score(
                name,
                player_score,
                player_wickets,
                player_balls,
                max_balls
            )

            player_run = get_number(
                "Choose your run (1-6): ", 1, 6
            )

            computer_run = random.randint(1, 6)

            print("Computer played:", computer_run)

            player_balls += 1

            if player_run == computer_run:

                player_wickets += 1

                print("\n⚡ WICKET!")
                print("You lost a wicket!")

            else:

                player_score += player_run

                print("You scored",player_run,"run(s).")

                # Target reached
                if player_score >= target:
                    break

        print("\n========================================")
        print(" YOUR INNINGS IS OVER")
        print("========================================")

        display_score(
            name,
            player_score,
            player_wickets,
            player_balls,
            max_balls
        )

    # ======================================
    # FINAL RESULT
    # ======================================

    print("\n========================================")
    print(" FINAL SCORE")
    print("========================================")

    print(name, ":", player_score, "/", player_wickets)
    print("Computer :", computer_score, "/", computer_wickets)

    print("\nOvers played by", name + ":",
          player_balls // 6,
          ".",
          player_balls % 6)

    print("Overs played by Computer:",
          computer_balls // 6,
          ".",
          computer_balls % 6)

    # --------------------------------------
    # WINNER
    # --------------------------------------

    if player_score > computer_score:

        print("\n🏆 CONGRATULATIONS", name + "!")
        print("YOU WON THE MATCH!😎")

        print("You won by",player_score - computer_score, "run(s)." )

    elif computer_score > player_score:

        print("\n🏆 COMPUTER WON THE MATCH!")

        print("Computer won by", computer_score - player_score, "run(s).")

    else:

        print("\n🤝 THE MATCH IS A DRAW!")


# ==========================================
# PLAY AGAIN
# ==========================================

while True:

    play_game()

    print("\n========================================")

    while True:
        again = input("Do you want to play again? (yes/no): ").lower()
        if again == "yes" or again == "no":
            break

        print("Please enter yes or no.")

    if again == "no":

        print("\n========================================")
        print(" THANK YOU FOR PLAYING!")
        print("========================================")

        break

    print("\nStarting a new match...")