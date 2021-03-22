import params
import random
import Player


class BadPlayer(Player.Player):
    def __init__(self, id):
        super().__init__(id)
        # decide the functions for strategies, will be edited in inheritence
        self.vote_strategy = self.vote_strategy_2
        self.choose_policy_strategy = self.choose_policy_strategy_2
        self.communicate_strategy = self.communicate_strategy_2
        self.flush_strategy = self.flush_2

    def vote_strategy_1(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        return params.n + params.f - 1

    def choose_policy_strategy_1(self):
        return False

    def communicate_strategy_1(self, isSend=True, msg=None):
        pass

    def flush_1(self):
        pass

    def vote_strategy_2(self):
        # strategy for turn
        # already got the information of the turn, update the leader selection
        return params.n + params.f - 1

    def choose_policy_strategy_2(self):
        return False

    def communicate_strategy_2(self, isSend=True, msg=None):
        if isSend:
            # send the information
            # if have information
            if self.round in self.policy_information.keys():
                ids = random.sample(range(0, params.n), params.communication_bound + 500)
                fake_msg = self.policy_information[self.round]
                fake_msg["is_policy_good"] = not fake_msg["is_policy_good"]
                for id in ids:
                    d_msg = {"from": self.id}
                    d_msg.update(fake_msg)
                    self.players[id].communicate(isSend=False,
                                                 msg=d_msg)

    def flush_2(self):
        pass
