####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Los Gatos' # Only 10 chars displayed.
strategy_name = '1/3 Betray, Then Betray'
strategy_description = 'Collud but 1/3 chance betray, then betray forever'
import random 

def move(my_history, their_history, my_score, their_score):
    '''Collude but 1/3 chance that they betray, then betray for the rest of the games
    '''
    if 'b' in my_history: 
      return 'b'
    else: 
      dice = random.randint(1,3)
      if dice == 1 or dice == 2:
        return 'b'
      else: 
        return 'c'

    