Distributed algorithms final project by Yoav Flato and Alon Kagan

In order to run a simulation, run the main.py file - a grph will show up when the run ends.

In order to change number of turns, change the parameter i in main(?) call, in main.py file

In order to change strategies of bad/good players you need to go to the init function
in BadPlayer.py/GoodPlayer.py, and change in each relevant variable the number of strategy:

self.vote_strategy = self.vote_strategy_(wanted number strategy)
self.choose_policy_strategy = self.choose_policy_strategy_(wanted number strategy)
self.communicate_strategy = self.communicate_strategy_(wanted number strategy)
self.flush_strategy = self.flush_(wanted number strategy)

NUMBER OF STRATEGY EXPLAINING

IN BADPLAYER:
1 - bad players do nothing other from vote to bad leader
2 - bad players share false information to other players

IN GOODPLAYERS:
1 + 2 - strategies we tried implement, but they didn't work
3 - good players only listen to themselves and don't communicate
4 - good players also send to other players about good/bad policies they see
5 - good players are catching false information from bad players, detect them as bad and
share this information with other players
