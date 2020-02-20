####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'GitScrub' # Only 10 chars displayed.
strategy_name = 'Smartest'
strategy_description = 'We used a lot of conditionals so our decision is based off the previous opponets decision and the score.'
    
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
    # Decide whether to return 'c' or 'b'
    
#betrays first round
    if len(my_history)==0:
      output = 'b'
#rounds after first round
    if len(my_history) > 0:
      value = 0
      #checks if opponent score is higher than mine
      if their_score > my_score:
        value += abs(their_score-my_score)
      else:
        value += abs(my_score - their_score)
      #counts the number of betrays and colludes
      countb = their_history.count('b')
      countc = their_history.count('c')
      countvalue = 0
      #compares the number of betrays and colludes
      if countb > countc:
        countvalue += abs(countb-countc)
      else: 
        countvalue += abs(countc-countb)
      retaliate = False
      #checks if I was betrayed in last round
      if my_history[-1]=='c' and their_history[-1]=='b':
        retaliate = True
      #if opponent's score is higher and I was betrayed, return b
      if their_score > my_score and retaliate == True:
        output = 'b'
      #if no betray in opponent history and more than 3 rounds
      elif 'b' not in their_history[-3:] and len(my_history)>=3:
        output = 'b'
      #if my score is equal to theirs
      elif my_score == their_score:
        output = 'b'
      else:
        factor = 0.86
        #if opponent has betray in history, increase betray factor
        if 'b' in their_history:
          factor += 0.4
        #if difference between b and c is greater than difference of scores
        if countvalue > value:
          upperlim = int((countvalue - value) * factor)
          #generated random integer with limits of the different of scores (values) and difference in number of b and c
          if random.randint(value, countvalue) < upperlim:
            output = 'b'
          else:
            output = 'c'
        else:
          upperlim2 = int((value - countvalue) * factor)
          if random.randint(countvalue, value) < upperlim2:
            output = 'b'
          else:
            output = 'c'
    return output

