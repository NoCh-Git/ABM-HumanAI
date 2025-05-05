from mesa import Model
from models.agents import Worker, Engineer, Manager, AlgorithmicSystem

class WorkflowModel(Model):
    def __init__(self, N_workers=10):
        self.num_agents = N_workers
        self.all_agents = []
        self.agent_id = 0  # custom ID counter

        self.phase = "goal_formation"
        self.phase_step = 0
        self.time = 0  # global time step

        self.knowledge_centralization = 0
        self.system_influence = 0
        self.data_quality_modifier = 0

        # Create core agents
        self.manager = Manager(self.next_id(), self)
        self.engineer = Engineer(self.next_id(), self)
        self.system = AlgorithmicSystem(self.next_id(), self)
        self.all_agents.extend([self.manager, self.engineer, self.system])

        # Create workers
        self.workers = []
        for _ in range(self.num_agents):
            worker = Worker(self.next_id(), self)
            self.workers.append(worker)
            self.all_agents.append(worker)

        # Manual data collection
        self.data = []

    def next_id(self):
        self.agent_id += 1
        return self.agent_id

    def step(self):
        # Determine current phase by internal counter
        if self.phase_step < 5:
            self.phase = "goal_formation"
        elif self.phase_step < 10:
            self.phase = "data_production"
        elif self.phase_step < 15:
            self.phase = "data_use"
        else:
            self.phase_step = 0
            self.knowledge_centralization = 0
            self.system_influence = 0
            self.data_quality_modifier = 0
            self.phase = "goal_formation"

        # Step all agents
        for agent in self.all_agents:
            agent.step()

        # Collect metrics
        avg_resistance = sum(w.resistance for w in self.workers) / self.num_agents
        avg_agency = sum(w.agency_score for w in self.workers) / self.num_agents

        # Log data (use global self.time)
        self.data.append({
            "time": self.time,
            "phase": self.phase,
            "knowledge_centralization": self.knowledge_centralization,
            "system_influence": self.system_influence,
            "average_resistance": avg_resistance,
            "average_agency": avg_agency,
            "data_quality_modifier": self.data_quality_modifier
        })

        # Advance counters
        self.phase_step += 1
        self.time += 1
