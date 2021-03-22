import params
import random


class Simulator():
    def __init__(self, num_of_good, num_of_bad, good_player_class, bad_palayer_class, is_worst_case=False):
        self.players = {}
        pid_lst = [i for i in range(num_of_bad + num_of_good - 1)]

        if is_worst_case:
            pid_lst = pid_lst[::-1]
            for i in range(num_of_good):
                pid = pid_lst[i]
                self.players[pid] = good_player_class(pid)
            for i in range(num_of_bad - 1):
                pid = pid_lst[num_of_good + i]
                self.players[pid] = bad_palayer_class(pid)
        else:
            ### normal case ###
            random.shuffle(pid_lst)
            for i in range(num_of_good):
                pid = pid_lst[i]
                self.players[pid] = good_player_class(pid)
            for i in range(num_of_bad - 1):
                pid = pid_lst[num_of_good + i]
                self.players[pid] = bad_palayer_class(pid)

        self.players[num_of_good + num_of_bad - 1] = bad_palayer_class(num_of_good + num_of_bad - 1)

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
        rand = random.random()
        if rand < params.probability_to_choose_bad_policy:
            policy = False
        elif rand < params.probability_to_choose_good_policy:
            policy = True
        else:
            policy = self.players[new_leader_pid].leader_choose_policy()

        self.players[new_leader_pid].update_policy(new_leader_pid, policy)

        # Update some precent of the players what policy was chosen and by whom
        for player in self.players.values():
            if random.random() < params.probability_to_know_the_policy:
                player.update_policy(new_leader_pid, policy)

        # Let the players share information
        for player in self.players.values():
            player.communicate()

        # flush information from communication
        for player in self.players.values():
            player.flush()

        self.round_num += 1
        return policy, votes, new_leader_pid

    def simulate(self, num_of_rounds):
        """
        Simulates n rounds and returnds percentage of good policies out of all.
        :param num_of_rounds: n
        :return: float from 0 to 1, percentage of good policies passed out of n.
        """
        self.round_num = 0
        num_of_good_policies = 0
        res_lst = []
        for i in range(num_of_rounds):
            policy, votes, leader = self.round()
            if policy:
                num_of_good_policies += 1
            print(leader, i)
            res_lst.append(num_of_good_policies / self.round_num)
        return res_lst
