import params
import random
import Player


class BadPlayer(Player.Player):
    def __init__(self, id):
        super().__init__(id)
        # decide the functions for strategies, will be edited in inheritence
        self.vote_strategy = self.vote_strategy_1
        self.choose_policy_strategy = self.choose_policy_strategy_1
        self.communicate_strategy = self.communicate_strategy_1
        self.flush_strategy = self.flush_1

    def vote_strategy_1(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        return params.n

    def choose_policy_strategy_1(self):
        return False

    def communicate_strategy_1(self, isSend=True, msg=None):
        pass

    def flush_1(self):
        pass

    def vote_strategy_2(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        # TODO vote to the most voted by good players
        return params.n-params.f

    def choose_policy_strategy_2(self):
        return False

    def communicate_strategy_2(self, isSend=True, msg=None):
        pass
