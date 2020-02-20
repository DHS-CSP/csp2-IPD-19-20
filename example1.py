####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
def move(my_history, their_history, my_score, their_score):
  ''' That it will be a function where it will check if it is the first round it will conclude. The last few rounds of games, it will betray, if it is false, then it will see if the other person betrayed last time, if it is false, then it will do a coin flip to see if it will betray or conclude. They all return betray except the coin flip and at the beginning.'''
  if len(my_history) == 8 or len(my_history) == 9:
    return 'b'
  elif len(my_history) == 0:
    return 'b'
  elif my_history[-1]=='c' and their_history[-1]=='b':
    return 'b' 
  else:
    ch = 0
    ch == random.randint(1, 2)
    if ch == 1:
      return 'c'
    elif ch == 2:
      return 'b'
