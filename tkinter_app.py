# This is a simple Tkinter GUI for running the ABM simulation.
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import pandas as pd
from models.workflow_model import WorkflowModel
from analysis.visualize import plot_simulation_results  # make sure this is importable

def run_simulation():
    # Get values from sliders and fields
    workers = int(worker_slider.get())
    engineers = int(engineer_slider.get())
    managers = int(manager_slider.get())
    data_scientists = int(ds_slider.get())
    try:
        steps = int(step_var.get())
    except ValueError:
        steps = 300  # fallback if input is invalid

    # Run the model
    model = WorkflowModel(
        N_workers=workers,
        N_ds_agents=data_scientists,
        N_engineers=engineers,
        N_managers=managers,
        total_steps=steps
    )

    for _ in range(steps):
        model.step()

    # Create dataframe and plot using your visualize.py logic
    df = pd.DataFrame(model.data)
    plot_simulation_results(df)


# --- GUI layout ---
root = tk.Tk()
root.title("ABM Human-AI Simulation")
root.resizable(True, True)
root.geometry("400x900")
root.configure(bg="#1C39BB")
bold_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
root.option_add("*TButton*highlightThickness", 0)
root.option_add("*TButton*borderWidth", 0)
root.option_add("*TButton*padding", [5, 5])
root.option_add("*TButton*relief", "flat")

tk.Label(root, text="Number of Workers", bg="#1C39BB", fg="white",font=bold_font).pack()
worker_slider = tk.Scale(root, from_=5, to=1000, orient="horizontal", length=300, bg="#1C39BB", fg="white", troughcolor="#0F1E6B", highlightthickness=0)
worker_slider.set(20)
worker_slider.pack()

tk.Label(root, text="Number of Engineers", bg="#1C39BB", fg="white",font=bold_font).pack()
engineer_slider = tk.Scale(root, from_=1, to=10, orient="horizontal", length=300, bg="#1C39BB", fg="white", troughcolor="#0F1E6B", highlightthickness=0)
engineer_slider.set(2)
engineer_slider.pack()

tk.Label(root, text="Number of Managers", bg="#1C39BB", fg="white",font=bold_font).pack()
manager_slider = tk.Scale(root, from_=1, to=10, orient="horizontal", length=300, bg="#1C39BB", fg="white", troughcolor="#0F1E6B", highlightthickness=0)
manager_slider.set(2)
manager_slider.pack()

tk.Label(root, text="Number of Data Scientists", bg="#1C39BB", fg="white",font=bold_font).pack()
ds_slider = tk.Scale(root, from_=0, to=5, orient="horizontal", length=300, bg="#1C39BB", fg="white", troughcolor="#0F1E6B", highlightthickness=0)
ds_slider.set(1)
ds_slider.pack()

tk.Label(root, text="Number of Steps", font=bold_font, bg="#1C39BB", fg="white").pack()
step_var = tk.StringVar()
step_entry = ttk.Entry(root, textvariable=step_var, width=10)
step_var.set("300")  # default value
step_entry.pack()

run_button = tk.Button(
    root,
    text="Run Simulation",
    command=run_simulation,
    highlightbackground="yellow",  # background color
    fg="black",         # text color
    font=bold_font
)
run_button.pack(pady=15)
# Add a quit button
quit_button = tk.Button(
    root,
    text="Quit",
    command=root.quit,
    highlightbackground="yellow",  # background color
    fg="Black",          # text color
    font=bold_font       
)
quit_button.pack(pady=15)

root.mainloop()
