import pandas as pd
import matplotlib.pyplot as plt

def plot_phases(ax, df):
    """Add colored vertical spans to indicate phases."""
    phase_colors = {
        "goal_formation": "#D0E1F9",
        "data_production": "#F9E0D9",
        "data_use": "#E0F9D9"
    }
    for i in range(len(df)):
        phase = df["phase"].iloc[i]
        ax.axvspan(i - 0.5, i + 0.5, color=phase_colors.get(phase, "#eeeeee"), alpha=0.2)

def main():
    # Load the results
    df = pd.read_csv("data/simulation_results.csv")

    # Plot: Agency and Resistance
    fig, ax = plt.subplots(figsize=(12, 5))
    plot_phases(ax, df)

    ax.plot(df["time"], df["average_agency"], label="Average Agency", color="blue", marker="o")
    ax.plot(df["time"], df["average_resistance"], label="Average Resistance", color="orange", marker="x")
    
    ax.set_xlabel("Phase Step")
    ax.set_ylabel("Score (normalized per agent)")
    ax.set_title("Worker Agency and Resistance Over Time (with Phases)")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

    # Plot: System Influence and Knowledge Centralization
    fig, ax2 = plt.subplots(figsize=(12, 5))
    plot_phases(ax2, df)

    ax2.plot(df["time"], df["system_influence"], label="System Influence", color="purple", marker="o")
    ax2.plot(df["time"], df["knowledge_centralization"], label="Knowledge Centralization", color="green", marker="s")

    ax2.set_xlabel("Phase Step")
    ax2.set_ylabel("Control Metrics")
    ax2.set_title("System and Managerial Control Over Time (with Phases)")
    ax2.legend()
    ax2.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
