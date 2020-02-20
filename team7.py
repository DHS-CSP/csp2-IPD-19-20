####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The Escapees' # Only 10 chars displayed.
strategy_name = 'Copy'
strategy_description = 'Always copy the previous output of the opponent.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif their_history[-1]=='b':#checks if the opponent betrayed in the previous round
        return 'b' #copies the opponent and puts a betrayal for the next round 
    else:
        return 'c' # otherwise collude.
    

