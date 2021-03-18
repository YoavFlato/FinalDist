import params
import random


class Player:
    def __init__(self, id):
        self.id = id
        # dict policy_information_from_others[i] = [(id_info_from, leader, is_policy_good) for each info in turn i]
        self.policy_information_from_others = {}
        # dict policy_information[i] = (leader, is_policy_good)
        self.policy_information = {}
        self.round = 0
        self.players = []
        self.vote_strategy = None  # strategy for vote leader  :type: function
        self.choose_policy_strategy = None  # strategy for choose policy  :type: function
        self.communicate_strategy = None  # strategy for communicate  :type: function

    def set_players(self, lst_of_players):
        self.players = lst_of_players

    def update_policy(self, leader, is_policy_good):
        self.policy_information[self.round] = {"leader": leader, "is_policy_good": is_policy_good}

    def update_round_num(self, round):
        self.round = round

    def vote_leader(self):
        return self.vote_strategy()

    def leader_choose_policy(self):
        return self.choose_policy_strategy()

    def communicate(self):
        # communicate with other players and transfer information
        self.communicate_strategy()
