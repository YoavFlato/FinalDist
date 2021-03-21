import params
import random
import Player


class GoodPlayer(Player.Player):
    # need to have strategies for vote, leader choose and communicate
    def __init__(self, id):
        super().__init__(id)
        self.players_rank = [{"P": 0.0, "N": 0.0} for i in
                                  range(params.n + params.f)]  # (P_good-P_bad, number of selection to leadership)
        # decide the functions for strategies, will be edited in inheritence
        self.vote_strategy = self.vote_strategy_1
        self.choose_policy_strategy = self.choose_policy_strategy_1
        self.communicate_strategy = self.communicate_strategy_1
        self.flush_strategy = self.flush_1

    def highest_rank_vote(self):
        if not self.policy_information:
            # first turn - choose randomly
            return random.randint(0, params.n - 1)
        # vote to highest P_good - P_bad
        if self.round - 1 in self.policy_information.keys():
            leader = self.players_rank[self.policy_information[self.round - 1]["leader"]]
            add_P = 1 if self.policy_information[self.round - 1]["is_policy_good"] else -1
            leader["P"] = leader["P"] * (leader["N"] / (leader["N"] + 1)) + (
                        add_P / (leader["N"] + 1))  # update P_good - P_bad
            leader["N"] = leader["N"] + 1

        players_rank_P = [d["P"] for d in self.players_rank]
        best_P_ratio = max(players_rank_P)
        players_with_best_P_ratio = [i for i in range(params.n + params.f) if players_rank_P[i] == best_P_ratio]
        return random.choice(players_with_best_P_ratio)

    def vote_strategy_1(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        return self.highest_rank_vote()

    def choose_policy_strategy_1(self):
        return True

    def communicate_strategy_1(self, isSend=True, msg=None):
        pass

    def flush_1(self):
        pass

    def vote_strategy_2(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        return self.highest_rank_vote()

    def choose_policy_strategy_2(self):
        return True

    def communicate_strategy_2(self, isSend=True, msg=None):
        if isSend:
            # send the information
            # if have information
            if self.round in self.policy_information.keys():
                ids = random.sample(range(0, params.n), params.communication_bound)
                for id in ids:
                    self.players[id].communicate(isSend=False,
                                                 msg={"from": self.id} + self.policy_information[self.round])
        else:
            # recieve information and put it in
            if self.round in self.policy_information_from_others.keys:
                self.policy_information_from_others[self.round] = [msg]
            self.policy_information_from_others[self.round].append(msg)

    def flush_2(self):
        # flush the information from the communication part
        if self.round in self.policy_information_from_others.keys:
            # if exists
            key0 = self.policy_information_from_others.keys[0]
            self.policy_information[self.round] = {"leader": self.policy_information_from_others[key0]["leader"],
                                                   "is_policy_good": self.policy_information_from_others[key0][
                                                       "is_policy_good"]}
