import random
from mesa import Agent

class Worker(Agent):
    def __init__(self, unique_id, model):
        # Avoid broken Mesa super() call
        self.unique_id = unique_id
        self.model = model

        self.participation = random.uniform(0, 1)
        self.agency_score = 0
        self.resistance = 0
        self.data_quality = 0

    def step(self):
        if self.model.phase == "goal_formation":
            if self.participation > 0.7:
                self.agency_score += 1
        elif self.model.phase == "data_production":
            if self.participation > 0.5:
                self.data_quality = random.uniform(0.7, 1.0)
                self.agency_score += 0.5
            else:
                self.data_quality = random.uniform(0.1, 0.6)
                self.resistance += 1
        elif self.model.phase == "data_use":
            if self.model.system.transparency > 0.5:
                self.agency_score += 0.2
            else:
                self.resistance += 0.5

class Engineer(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model

        self.knowledge_level = random.uniform(0.5, 1.0)
        self.data_sensitivity = random.uniform(0.3, 0.8)

    def step(self):
        if self.model.phase == "goal_formation":
            self.knowledge_level += 0.05
        elif self.model.phase == "data_production":
            self.model.data_quality_modifier += self.data_sensitivity * 0.05
        elif self.model.phase == "data_use":
            self.model.knowledge_centralization += self.knowledge_level * 0.05

class Manager(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model

        self.control_preference = random.uniform(0.5, 1.0)
        self.feedback_acceptance = random.uniform(0.2, 0.8)

    def step(self):
        if self.model.phase == "goal_formation":
            self.model.knowledge_centralization += self.control_preference * 0.1
        elif self.model.phase == "data_use":
            if self.model.system.transparency < 0.5:
                self.model.knowledge_centralization += 0.1
            else:
                self.model.knowledge_centralization += 0.05 * (1 - self.feedback_acceptance)

class AlgorithmicSystem(Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        self.model = model

        self.transparency = random.uniform(0.2, 0.8)

    def step(self):
        if self.model.phase == "data_use":
            self.model.system_influence += (1 - self.transparency) * 0.1
            for w in self.model.workers:
                if self.transparency < 0.5:
                    w.agency_score -= 0.2
