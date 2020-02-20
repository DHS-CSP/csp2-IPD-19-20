####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
 
team_name = 'Alcatraz'
strategy_name = 'Probability'
strategy_description = 'Based on their history, betray or collude. If they have colluded more than 75% of the time, then collude as well. Otherwise, betray.'
  
def move(my_history, their_history, my_score, their_score):
 num_collude = 0
 num_betray = 0
 if len(my_history) == 0:
   return 'c'
 else:
   for char in their_history:
    if char == 'c':
      num_collude += 1
    if char == 'b':
       num_betray += 1
    percent_collude = float(num_collude / len(their_history))
   if percent_collude >= 0.75:
     return 'c'
   else:
     return 'b'


