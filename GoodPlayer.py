import params
import random
import Player


class GoodPlayer(Player.Player):
    # need to have strategies for vote, leader choose and communicate
    def strategies_decide(self):
        # decide the functions for strategies, will be edited in inheritence
        pass

    def strategy1(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        if self.round == 0:
            return random.randint(0, params.n - 1)
        self.good_players_rank[self.policy_information[self.round - 1]["leader"]] = \
            self.policy_information[self.round - 1][
                "is_policy_good"]
        return self.good_players_rank.index(max(self.good_players_rank))
