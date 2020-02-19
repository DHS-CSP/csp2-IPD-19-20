####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Collusion' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
import random

    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history) == 0:
        return 'c'
    
    elif random.randint(1,100) <= 4:
      return 'c'

    else:
      return their_history[-1]
  

   
