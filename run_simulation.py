from models.workflow_model import WorkflowModel
import pandas as pd
import os

def main():
    model = WorkflowModel(N_workers=20)

    num_steps = 30
    for _ in range(num_steps):
        model.step()

    # Convert collected data to DataFrame
    df = pd.DataFrame(model.data)

    # Save results to CSV
    os.makedirs("data", exist_ok=True)
    output_path = "data/simulation_results.csv"
    df.to_csv(output_path, index=False)

    print(f"Simulation complete. Results saved to: {output_path}")
    print(df.tail())  # Show last few rows

if __name__ == "__main__":
    main()
