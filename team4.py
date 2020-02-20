####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Computer'
strategy_name = 'BBCB'
strategy_description = 'Betray, Betray, Collude, Betray '
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    # This player colludes on even numbered rounds (first round is round #0).
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if severely punished last time,
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'c'
    else:
        return 'c'   
    