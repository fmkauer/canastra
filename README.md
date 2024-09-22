# Canastra rules - TODO

General ruling of the game, _~~or at least, the way I learned with my grandparents.~~_

The game is played in doubles, so it goes P1 (Team 1), P2 (Team 2), P3 (Team 1), P4 (Team 2) and then the cycle repeats. The game is played with 2 decks of cards with all cards that come with the deck.

The game starts with the dealer shuffling the cards and the player to the right cutting the deck. The dealer then gives 13 cards to each player, and the game starts.

The first player has to draw a card, as there are no cards on the waste stack. But that player has the option to redraw, if they discard the card that they drew.
Each player receives 13 cards. The game goes to 3000 points.

You try to make sequences of 7 cards of the same suit, which is called Canastra, which gives you 200 points (if it's a clean one, the 'dirty' one gives you only half (100 points))

You can also 'burn' Aces, 3s ans Kings (which means put them on the table, but using only that card and not, and they are eligible to the Canastra (7 of the same kind together makes it a Canastra))

Aces are worth 15 points, 2, 7-K are worth 10, 3-6 are worth 5 and jokers are worth 20. 

Jokers can be used as any card, and still makes the canastra be 'clean', meanwhile 2s can be used as jokers, but they make the canastra be 'dirty', they can be used as 2s, and if so, the Canastra is clean.

There a waste stack, which is visible for everyone and all cards in it are visible as well

Every turn each player has a decision, to either draw a card from the deck or to get the whole waste stack. And then they decide if they put some card on the table, either a new sequence, starting with 3 cards at minimum, or to add to a sequence from their team already on the table.

The game ends when a team reaches 3000 points, and the team with the most points wins.

# TODO:

- [x] Implement card deck creation and shuffling.
- [x] Implement player hands and drawing cards.
- [ ] Implement game logic for playing cards and forming canastas.
    - [x] Implement player turns.
        1. Create a method in `table.py` to cycle through players.
        2. The method should take the current player and return the next player.
    - [x] Implement drawing cards from the deck or waste pile.
        1. Add a method to `player.py` to draw from the waste pile.
        2. Modify the existing `draw` method to take an optional argument indicating whether to draw from the deck or waste pile.
    - [x] Implement playing cards from hand to the table.
        1. Add a method to `player.py` to play a card from their hand to the table.
        2. The method should take the card and the target sequence on the table as arguments.
    - [ ] Implement validating played sequences.
        1. Add a method to `table.py` to validate if a played sequence is valid.
        2. The method should check if the sequence meets the Canastra rules (at least three cards of the same suit, using wildcards appropriately).
    - [ ] Implement forming Canastras.
        1. Add a method to `table.py` to check if a Canastra is formed.
        2. The method should check if a sequence has at least seven cards and apply the appropriate scoring rules.
- [ ] Implement scoring system.
    1. Create a method in `table.py` to calculate the score for a given team.
    2. The method should consider the cards on the table, canastas formed, and any special cards used.
- [ ] Create a command-line interface or graphical user interface for playing the game.
    1. Choose a suitable framework for the interface (e.g., `curses` for CLI, `Tkinter` for GUI).
    2. Implement user input to allow players to interact with the game.
    3. Display the game state, including player hands, the table, and the score.
- [ ] Develop a reinforcement learning AI agent that can play Canastra.
    1. Choose a reinforcement learning library (e.g., `TensorFlow`, `PyTorch`).
    2. Define the state space, action space, and reward function for the Canastra environment.
    3. Implement the AI agent using a suitable reinforcement learning algorithm (e.g., Q-learning, Deep Q-learning).
- [ ] Train and evaluate the AI agent's performance.
    1. Create a simulation environment where the AI agent can play against itself or other agents.
    2. Train the AI agent using the chosen reinforcement learning algorithm.
    3. Evaluate the agent's performance by measuring its win rate against different opponents.
