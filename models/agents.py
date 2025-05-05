import random
from mesa import Agent

class Worker(Agent):
    """
    Represents a worker agent in the simulation.

    Workers have varying levels of participation, and their behavior affects and is affected by
    algorithmic management dynamics such as transparency, data collection, and decision-making.

    Attributes:
        unique_id (int): Unique identifier for the agent.
        model (Model): Reference to the model instance.
        participation (float): A random value [0, 1] representing how active the worker is.
        agency_score (float): Accumulated indicator of perceived influence or participation.
        resistance (float): Accumulated indicator of disengagement or pushback.
        data_quality (float): Quality of data generated during data production phase.
    """
    def __init__(self, unique_id, model):
        """
        Initialize a worker with random participation and zeroed scores.
        """
        self.unique_id = unique_id
        self.model = model

        self.participation = random.uniform(0, 1)
        self.agency_score = 0
        self.resistance = 0
        self.data_quality = 0

    def step(self):
        """
        Define behavior for each simulation step, based on the current model phase:
        - In 'goal_formation': high participation boosts agency.
        - In 'data_production': participation affects data quality and resistance.
        - In 'data_use': transparency influences perceived fairness and resistance.
        """
        # Update agency and resistance based on participation and model phase
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
    """
    Represents a technical engineer in the simulation.

    Engineers influence the quality of system setup and mediate knowledge flow between
    workers, management, and the algorithmic system.

    Attributes:
        unique_id (int): Unique identifier for the agent.
        model (Model): Reference to the model instance.
        knowledge_level (float): Represents system literacy or expertise.
        data_sensitivity (float): Determines how much they improve data quality.
    """
    def __init__(self, unique_id, model):
        """
        Initialize an engineer with moderate to high knowledge and data sensitivity.
        """
        self.unique_id = unique_id
        self.model = model

        self.knowledge_level = random.uniform(0.5, 1.0)
        self.data_sensitivity = random.uniform(0.3, 0.8)

    def step(self):
        """
        Engineer behavior across phases:
        - In 'goal_formation': gain more system knowledge.
        - In 'data_production': improve data quality based on sensitivity.
        - In 'data_use': increase centralization by interpreting results for others.
        """
        if self.model.phase == "goal_formation":
            self.knowledge_level += 0.05
        elif self.model.phase == "data_production":
            self.model.data_quality_modifier += self.data_sensitivity * 0.05
        elif self.model.phase == "data_use":
            self.model.knowledge_centralization += self.knowledge_level * 0.05

class Manager(Agent):
    """
    Represents a managerial agent responsible for decision-making and oversight.

    Managers shape how centralized decisions are and how feedback is incorporated
    based on their preferences and attitudes toward transparency.

    Attributes:
        unique_id (int): Unique identifier for the agent.
        model (Model): Reference to the model instance.
        control_preference (float): Tendency to centralize decision-making (0–1).
        feedback_acceptance (float): Willingness to incorporate worker feedback (0–1).
    """

    def __init__(self, unique_id, model):
        """
        Initialize a manager with preferences for control and feedback.
        """
        self.unique_id = unique_id
        self.model = model

        self.control_preference = random.uniform(0.5, 1.0)
        self.feedback_acceptance = random.uniform(0.2, 0.8)

    def step(self):
        """
        Manager behavior by phase:
        - In 'goal_formation': exert control in framing objectives.
        - In 'data_use': influence how decisions are interpreted based on transparency and feedback tolerance.
        """
        if self.model.phase == "goal_formation":
            self.model.knowledge_centralization += self.control_preference * 0.1
        elif self.model.phase == "data_use":
            if self.model.system.transparency < 0.5:
                self.model.knowledge_centralization += 0.1
            else:
                self.model.knowledge_centralization += 0.05 * (1 - self.feedback_acceptance)

class AlgorithmicSystem(Agent):
    """
    Represents the algorithmic decision-making system.

    The system's transparency determines how much influence it has over outcomes and
    how much it reduces or supports worker agency.

    Attributes:
        unique_id (int): Unique identifier for the agent.
        model (Model): Reference to the model instance.
        transparency (float): Degree of explainability and openness (0 = opaque, 1 = fully transparent).
    """
    def __init__(self, unique_id, model):
        """
        Initialize the system with a random level of transparency.
        """
        self.unique_id = unique_id
        self.model = model

        self.transparency = random.uniform(0.2, 0.8)

    def step(self):
        """
        In 'data_use' phase:
        - The system exerts more influence if it is opaque.
        - Reduces worker agency when transparency is low.
        """
        if self.model.phase == "data_use":
            self.model.system_influence += (1 - self.transparency) * 0.1
            for w in self.model.workers:
                if self.transparency < 0.5:
                    w.agency_score -= 0.2
