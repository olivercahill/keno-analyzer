import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
import os
from KenoPatterns import fetch_keno_results, analyze_combos

# Use relative path to find the logo inside the assets folder
LOGO_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "keno_logo.png")

def run_predictions():
    combo_size = spots_var.get()
    days = days_var.get()
    top_n = results_var.get()

    # Update headers dynamically
    least_header.config(text=f"Top {top_n} LEAST Common ({combo_size}-number combos)")
    most_header.config(text=f"Top {top_n} MOST Common ({combo_size}-number combos)")

    try:
        draws = fetch_keno_results(days)
    except Exception as e:
        most_box.delete("1.0", tk.END)
        least_box.delete("1.0", tk.END)
        most_box.insert(tk.END, "Error fetching results.")
        least_box.insert(tk.END, str(e))
        return

    most_common, least_common = analyze_combos(draws, combo_size, top_n)

    # Fill MOST common column
    most_box.delete("1.0", tk.END)
    for combo, count in most_common:
        if len(combo) == 1:
            most_box.insert(tk.END, f"{combo[0]} → {count} times\n")
        else:
            most_box.insert(tk.END, f"{combo} → {count} times\n")

    # Fill LEAST common column
    least_box.delete("1.0", tk.END)
    for combo, count in least_common:
        if len(combo) == 1:
            least_box.insert(tk.END, f"{combo[0]} → {count} times\n")
        else:
            least_box.insert(tk.END, f"{combo} → {count} times\n")

# ---------------- Tkinter UI Setup ---------------- #
root = tk.Tk()
root.title("Keno Predictions")
root.geometry("800x600")  # Wider window for two columns

# Background logo
try:
    bg_image = Image.open(LOGO_PATH)
    bg_image = bg_image.resize((800, 600), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"⚠ Could not load background image: {e}")

# Title
title_label = tk.Label(root, text="Keno Predictions", font=("Arial", 18, "bold"), bg="white")
title_label.pack(pady=10)

# Number of Spots
spots_label = tk.Label(root, text="Number of Spots:", font=("Arial", 14), bg="white")
spots_label.pack()
spots_var = tk.IntVar(value=1)
ttk.Combobox(root, textvariable=spots_var, values=list(range(1, 13)), font=("Arial", 12), state="readonly").pack(pady=5)

# Number of Days
days_label = tk.Label(root, text="Number of Days:", font=("Arial", 14), bg="white")
days_label.pack()
days_var = tk.IntVar(value=1)
ttk.Combobox(root, textvariable=days_var, values=list(range(1, 31)), font=("Arial", 12), state="readonly").pack(pady=5)

# How Many Results
results_label = tk.Label(root, text="How Many Results:", font=("Arial", 14), bg="white")
results_label.pack()
results_var = tk.IntVar(value=1)
ttk.Combobox(root, textvariable=results_var, values=list(range(1, 11)), font=("Arial", 12), state="readonly").pack(pady=5)

# Run button
run_button = tk.Button(root, text="Run Predictions", font=("Arial", 14), command=run_predictions, bg="white")
run_button.pack(pady=15)

# Results frame
results_frame = tk.Frame(root, bg="white")
results_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Header row (fixed above scroll areas)
header_frame = tk.Frame(results_frame, bg="white")
header_frame.pack(fill="x")

least_header = tk.Label(header_frame, text="Top N LEAST Common", font=("Arial", 14, "bold"), bg="white")
least_header.pack(side="left", fill="x", expand=True, padx=5)

most_header = tk.Label(header_frame, text="Top N MOST Common", font=("Arial", 14, "bold"), bg="white")
most_header.pack(side="right", fill="x", expand=True, padx=5)

# Columns for results
columns_frame = tk.Frame(results_frame, bg="white")
columns_frame.pack(fill="both", expand=True)

least_box = ScrolledText(columns_frame, wrap=tk.WORD, font=("Courier", 12), bg="white", width=40, height=12)
least_box.pack(side="left", fill="both", expand=True, padx=5)

most_box = ScrolledText(columns_frame, wrap=tk.WORD, font=("Courier", 12), bg="white", width=40, height=12)
most_box.pack(side="right", fill="both", expand=True, padx=5)

root.mainloop()
