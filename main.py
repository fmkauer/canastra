from player import Player
from table import Table
from deck import Deck

def main():
    team1_score = 0
    team2_score = 0

    while team1_score < 3000 and team2_score < 3000:
        # Create players
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        player3 = Player("Player 3")
        player4 = Player("Player 4")

        # Initialize game
        table = Table([player1, player2, player3, player4], 2)
        current_player = player1

        # Round loop
        round_over = False
        while not round_over:
            # Player turn
            print(f"{current_player.name}'s turn")
            table.play_turn(current_player)

            # Check if the round is over
            if len(current_player.hand) == 0:
                round_over = True

            # Move to the next player
            current_player = table.next_player()

        # Update scores (placeholder)
        team1_score += 100
        team2_score += 150

        print(f"Round over! Team 1: {team1_score}, Team 2: {team2_score}")

    # Determine the winner
    if team1_score >= 3000:
        print("Team 1 wins!")
    else:
        print("Team 2 wins!")

if __name__ == "__main__":
    main()
