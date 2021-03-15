from GoodPlayer import GoodPlayer
from params import *
import random


class Simulator():
    def __init__(self, num_of_good, num_of_bad):
        self.good_players = {}
        for i in range(num_of_good):
            pid = i
            self.good_players[pid] = GoodPlayer(pid)

        self.bad_players = {}
        for i in range(num_of_good):
            pid = num_of_good + i
            self.good_players[pid] = GoodPlayer(pid)

        self.players = self.good_players.update(self.bad_players)

        for player in self.players:
            player.set_players(self.players)

        self.round_num = 0

    def round(self):
        """
        1. Everyone votes
        2. The leader chooses a policy
        3. Discussion between the people
        :return:
        """
        for player in self.players:
            player.update_round_num(self.round_num)

        # Get votes for leader from everyone
        votes = {}
        for player in self.players:
            vote = player.vote_leader()
            if vote not in votes:
                votes[vote] = 0
            votes[vote] += 1

        # Choose new leader
        new_leader_pid = max(self.players, key=self.players.get)

        # The leader picks a new policy. He has a chance to automatically choose a good/bad policy,
        #   and otherwise he has free will.
        if random.random() < probability_to_choose_bad_policy:
            policy = False
        elif random.random() < probability_to_choose_good_policy:
            policy = True
        else:
            policy = self.players[new_leader_pid].leader_choose_policy()

        self.players[new_leader_pid].update_policy(new_leader_pid, policy)

        # Update some precent of the players what policy was chosen and by whom
        for player in self.players:
            if random.random() < probability_to_know_the_policy:
                player.update_policy(new_leader_pid, policy)

        # Let the players share information
        for player in self.players:
            player.communicate()

        self.round += 1
