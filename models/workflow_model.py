from mesa import Model
from models.agents import Worker, Engineer, Manager, AlgorithmicSystem, DataScientist

class WorkflowModel(Model):
    def __init__(self, N_workers=1000, N_ds_agents=5, N_engineers=10, N_managers=3, total_steps=300):
        self.total_steps = total_steps
        self.num_w_agents = N_workers
        self.num_ds_agents = N_ds_agents
        self.num_engineers = N_engineers
        self.num_managers = N_managers
        #self.num_agents = N_workers + N_ds_agents + N_engineers #exclude managers
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
        self.data_scientist = DataScientist(self.next_id(), self)
        self.system = AlgorithmicSystem(self.next_id(), self)
        self.all_agents.extend([self.manager, self.engineer, self.data_scientist, self.system])

        # Create workers
        self.workers = []
        for _ in range(self.num_w_agents):
            worker = Worker(self.next_id(), self)
            self.workers.append(worker)
            self.all_agents.append(worker)

        # Create datascientists
        self.data_scientist = []
        for _ in range(self.num_ds_agents):
            ds_agent = DataScientist(self.next_id(), self)
            self.data_scientist.append(ds_agent)
            self.all_agents.append(ds_agent)

        # Create engineers
        self.engineers = []
        for _ in range(self.num_engineers):
            engineer = Engineer(self.next_id(), self)
            self.engineers.append(engineer)
            self.all_agents.append(engineer)

        # Create managers
        self.managers = []  
        for _ in range(self.num_managers):
            manager = Manager(self.next_id(), self)
            self.managers.append(manager)
            self.all_agents.append(manager)

        # Manual data collection
        self.data = []

    def next_id(self):
        self.agent_id += 1
        return self.agent_id

    def step(self):
        # Determine current phase by internal counter
        one_third = self.total_steps // 3

        if self.phase_step < one_third:
            self.phase = "goal_formation"
        elif self.phase_step < 2 * one_third:
            self.phase = "data_production"
        elif self.phase_step < self.total_steps:
            self.phase = "data_usage"
        else:
            self.phase_step = 0
            self.knowledge_centralization = 0
            self.system_influence = 0
            self.data_quality_modifier = 0
            self.phase = "goal_formation"

        # print(f"Phase: {self.phase}")
        # Step all agents
        for agent in self.all_agents:
            agent.step()

        # Collect metrics
        avg_resistance = sum(w.resistance for w in self.workers) / self.num_agents
        avg_agency = sum(w.agency_score for w in self.workers) / self.num_agents
        avg_data_quality = sum(w.data_quality for w in self.workers) / self.num_agents

        # Log data (use global self.time)
        self.data.append({
            "time": self.time,
            "phase": self.phase,
            "knowledge_centralization": self.knowledge_centralization,
            "system_influence": self.system_influence,
            "average_resistance": avg_resistance,
            "average_agency": avg_agency,
            "average_data_quality": avg_data_quality,
            "data_quality_modifier": self.data_quality_modifier
        })

        # Advance counters
        self.phase_step += 1
        self.time += 1
