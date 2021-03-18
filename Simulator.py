from params import *
import random


class Simulator():
    def __init__(self, num_of_good, num_of_bad, good_player_class, bad_palayer_class):
        self.players = {}
        for i in range(num_of_good):
            pid = i
            self.players[pid] = good_player_class(pid)
        for i in range(num_of_bad):
            pid = num_of_good + i
            self.players[pid] = bad_palayer_class(pid)

        for player in self.players.values():
            player.set_players(self.players)

        self.round_num = 0

    def round(self):
        """
        1. Everyone votes
        2. The leader chooses a policy
        3. Discussion between the people
        :return:
        """
        for player in self.players.values():
            player.update_round_num(self.round_num)

        # Get votes for leader from everyone
        votes = {}
        for player in self.players.values():
            vote = player.vote_leader()
            if vote not in votes:
                votes[vote] = 0
            votes[vote] += 1

        # Choose new leader
        new_leader_pid = max(votes, key=votes.get)

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
        for player in self.players.values():
            if random.random() < probability_to_know_the_policy:
                player.update_policy(new_leader_pid, policy)

        # Let the players share information
        for player in self.players.values():
            player.communicate()

        self.round_num += 1
        return policy

    def simulate(self, num_of_rounds):
        """
        Simulates n rounds and returnds percentage of good policies out of all.
        :param num_of_rounds: n
        :return: float from 0 to 1, percentage of good policies passed out of n.
        """
        self.round_num = 0
        num_of_good_policies = 0
        for i in range(num_of_rounds):
               if self.round():
                   num_of_good_policies += 1
        return num_of_good_policies/num_of_rounds
