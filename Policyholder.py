class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name
        self.policy_id = policy_id
        self.active = True

    def register_policyholder(self):
        # Code to register a policyholder
        pass

    def suspend_policyholder(self):
        # Code to suspend a policyholder
        self.active = False

    def reactivate_policyholder(self):
        # Code to reactivate a policyholder
        self.active = True
