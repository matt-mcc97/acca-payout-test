
import random
from math import floor

payoutPercentage = 0.2    # How much is paid back on fourfold
assumedMargin = 1.05      # How much margin is assumed in each selection
minOdds = 1.5             # Minimum odds per selection
maxPayout = 50            # Maximum payout on fourfold


def place_bet(stake, odds1=0, odds2=0, odds3=0, odds4=0, odds5=0):

    # Assigns random odds to each selection
    selection1 = minOdds * random.randint(1, 4)
    selection2 = minOdds * random.randint(1, 4)
    selection3 = minOdds * random.randint(1, 4)
    selection4 = minOdds * random.randint(1, 4)
    selection5 = minOdds * random.randint(1, 4)


    # If specific odds are declared in function call then they will be assigned here
    if odds1 > 0:
        selection1 = odds1
    if odds2 > 0:
        selection2 = odds2
    if odds3 > 0:
        selection3 = odds3
    if odds4 > 0:
        selection4 = odds4
    if odds5 > 0:
        selection5 = odds5


    # This takes the selection odds and applies the assumed margin
    trueOdds1 = selection1 * assumedMargin
    trueOdds2 = selection2 * assumedMargin
    trueOdds3 = selection3 * assumedMargin
    trueOdds4 = selection4 * assumedMargin
    trueOdds5 = selection5 * assumedMargin

    # 'Results' for each outcome are generated
    result1 = random.random()
    result2 = random.random()
    result3 = random.random()
    result4 = random.random()
    result5 = random.random()

    # Declaring variables as a boolean for storing each selection result
    betResult1 = 0
    betResult2 = 0
    betResult3 = 0
    betResult4 = 0
    betResult5 = 0


    # Checks each result against the 'true' odds
    if 1 / trueOdds1 > result1:
        betResult1 = 1
    if 1 / trueOdds2 > result2:
        betResult2 = 1
    if 1 / trueOdds3 > result3:
        betResult3 = 1
    if 1 / trueOdds4 > result4:
        betResult4 = 1
    if 1 / trueOdds5 > result5:
        betResult5 = 1


    # Checking if the bet is a five/fourfold winner and determining the payout
    numberOfWinners = betResult1 + betResult2 + betResult3 + betResult4 + betResult5

    if numberOfWinners < 4:
        payout = 0
    elif numberOfWinners == 5:
        payout = stake * selection1 * selection2 * selection3 * selection4 * selection5
    elif numberOfWinners == 4:
        payout = stake * selection1 * selection2 * selection3 * selection4 * selection5 * payoutPercentage
        if betResult1 == 0:
            payout = payout / selection1
        elif betResult2 == 0:
            payout = payout / selection2
        elif betResult3 == 0:
            payout = payout / selection3
        elif betResult4 == 0:
            payout = payout / selection4
        elif betResult5 == 0:
            payout = payout / selection5

    # Checks if is the payout is above the max payout and lowers it if needed
    if payout > maxPayout and numberOfWinners == 4:
        payout = maxPayout

    return payout, numberOfWinners


def run_bets(min_bet, max_bet, number_of_trails, bets_per_trial, odds1=0, odds2=0, odds3=0, odds4=0, odds5=0):
    for j in range(1, number_of_trails):
        pot_amount = 0
        fourfoldWinners = 0
        fivefoldWinners = 0
        for i in range(1, bets_per_trial):
            bet_amount = random.randint(min_bet, max_bet)
            bet_return, win_status = place_bet(bet_amount, odds1, odds2, odds3, odds4, odds5)
            if bet_return > 0:
                pot_amount = pot_amount + bet_amount - bet_return
            else:
                pot_amount = pot_amount + bet_amount

            if win_status == 4:
                fourfoldWinners += 1
            elif win_status == 5:
                fivefoldWinners += 1

        print(f"Final pot amount is £{round(pot_amount, 2)} (£{round(pot_amount / bets_per_trial, 2)} per bet).",
              end=" ")
        print(f"Fourfold winners: {fourfoldWinners} (1 in every {floor(bets_per_trial / fourfoldWinners)} bets).",
              end=" ")
        print(f"Fivefold winners: {fivefoldWinners} (1 in every {floor(bets_per_trial / fivefoldWinners)} bets).")


run_bets(1, 10, 10, 1000000)
# 1. Min bet
# 2. Max bet
# 3. Number of trials
# 4. Number of bets per trial
# 5. 5 optional parameters to choose the specific selection odds
