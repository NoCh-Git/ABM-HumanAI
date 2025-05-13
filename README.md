# Workflow ABM – Simulating Control and Participation in Algorithmic Management

This project is a prototype agent-based model (ABM) designed to simulate the dynamics described in:

**Krzywdzinski, M., Schneiß, J., & Sperling, L. (2024).**  
*Between Control and Participation: The Politics of Algorithmic Management*.  
_New Technology, Work and Employment_.

The model explores how managers, engineers, workers, and algorithmic systems interact across three key phases of algorithmic management:

- **Goal formation**  
- **Data production**  
- **Data analysis**  

It investigates how knowledge centralization, worker resistance, and agency evolve over time under different conditions.

## Features

- Agent classes:
  - Workers (participation, resistance, agency)
  - Engineers (system setup, knowledge mediation)
  - DataScientists (fairness focus, expertise)
  - Managers (control orientation, feedback acceptance)
  - Algorithmic systems (transparency, decision influence)
- Simulation of a recurring management cycle
- Data collection on key fairness and power metrics
- Built using the [Mesa ABM framework](https://mesa.readthedocs.io/en/stable/)

## Requirements

- Python 3.7+
- [Mesa](https://github.com/projectmesa/mesa)

Install dependencies:

```bash
pip install mesa
