import matplotlib.pyplot as plt

def plot_phases(ax, df):
    """Add colored background spans for each phase block."""
    phase_colors = {
        "goal_formation": "#D0E1F9",
        "data_production": "#F9E0D9",
        "data_use": "#E0F9D9"
    }

    start_idx = 0
    current_phase = df["phase"].iloc[0]

    for i in range(1, len(df)):
        if df["phase"].iloc[i] != current_phase:
            start_time = df["time"].iloc[start_idx]
            end_time = df["time"].iloc[i - 1] + 1
            ax.axvspan(start_time, end_time, color=phase_colors.get(current_phase, "#eeeeee"), alpha=0.5)
            current_phase = df["phase"].iloc[i]
            start_idx = i

    # draw final span
    start_time = df["time"].iloc[start_idx]
    end_time = df["time"].iloc[len(df) - 1] + 1
    ax.axvspan(start_time, end_time, color=phase_colors.get(current_phase, "#eeeeee"), alpha=0.5)

def plot_simulation_results(df):
    """
    Plot the simulation results from a DataFrame.
    Produces a two-panel plot: worker metrics and system metrics.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    plot_phases(ax1, df)
    ax1.plot(df["time"], df["average_agency"], label="Average Agency", color="blue")
    ax1.plot(df["time"], df["average_resistance"], label="Average Resistance", color="orange")
    ax1.set_ylabel("Agency / Resistance")
    ax1.legend()
    ax1.set_title("Worker Metrics Over Time")

    plot_phases(ax2, df)
    ax2.plot(df["time"], df["system_influence"], label="System Influence", color="purple")
    ax2.plot(df["time"], df["knowledge_centralization"], label="Knowledge Centralization", color="green")
    ax2.set_ylabel("System Metrics")
    ax2.set_xlabel("Time")
    ax2.legend()
    ax2.set_title("System & Managerial Control Over Time")

    plt.tight_layout()
    plt.show()
