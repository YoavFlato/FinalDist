import params
import random


class Player:
    def __init__(self, id):
        self.id = id
        self.good_players_rank = [0 for i in range(params.n)]
        # dict policy_information_from_others[i] = [(id_info_from, leader, is_policy_good) for each info in turn i]
        self.policy_information_from_others = {}
        # dict policy_information[i] = (leader, is_policy_good)
        self.policy_information = {}
        self.round = 0
        self.players = []
        self.vote_strategy = None  # strategy for vote leader

    def strategies_decide(self):
        # decide the functions for strategies, will be edited in inheritence
        pass

    def set_players(self, lst_of_players):
        self.players = lst_of_players

    def update_policy(self, leader, is_policy_good):
        self.policy_information[self.round] = {"leader": leader, "is_policy_good": is_policy_good}

    def update_round_num(self, round):
        self.round = round

    def vote_leader(self):
        self.strategy()

    def leader_choose_policy(self):
        return True  # True is good policy, False is bad policy

    def communicate(self):
        # communicate with other players and transfer information
        pass
