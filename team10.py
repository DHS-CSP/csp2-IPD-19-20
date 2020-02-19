####
# Each team's file must define four tokens:
team_name = 'The Successors!'
strategy_name: 'Success'
strategy_description: ' Making 4 strategies. Betry, Alternate, Collude but retaliate, and collude. '
#     move: A function that returns 'c' or 'b'
####
 
team_name = 'The Successors!' # Only 10 chars displayed.
strategy_name = 'Success'
strategy_description = '  Making 4 strategies. Betry, Alternate, Collude but retaliate, and collude.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'b'

def move(my_history, their_history, my_score, their_score):
  theirB = 0 
  for action in their_history:
    if action == 'b':
      theirB+=1
  if len(their_history)==0:
    return "c"
  else:
    if theirB/len(their_history)>0.5 or their_score > my_score:
      return 'b'
    else:
      return 'c'
  print(theirB)
  
# Example 0.  collude
def move(my_history, their_history, my_score, their_score):
    return 'c'

# Example 1. Always collude
def move(my_history, their_history, my_score, their_score):
    return 'b'

# Example 2. Collude, then alternate
def move(my_history, their_history, my_score, their_score):
    if len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'

# Example 3. Collude but retaliate
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if severely punished last time,# otherwise collude.
    else:
        return 'c' # otherwise collude.


