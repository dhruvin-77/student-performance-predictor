import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model
model = joblib.load("model.pkl")

# ---------- DROPDOWN HELPER ----------

def create_dropdown(root, text, options, row):
    tk.Label(root, text=text, anchor="w", justify="left").grid(row=row, column=0, sticky="w")
    
    var = tk.StringVar()
    var.set(list(options.keys())[0])
    
    menu = tk.OptionMenu(root, var, *options.keys())
    menu.grid(row=row, column=1)
    
    return var, options

# ---------- INPUT VALIDATION ----------

def safe_int(value, name):
    try:
        return int(value)
    except:
        raise ValueError(f"{name} must be a number")

# ---------- PREDICT FUNCTION ----------

def predict():
    try:
        # Convert dropdowns to numbers
        studytime = studytime_map[studytime_var.get()]
        health = health_map[health_var.get()]
        freetime = freetime_map[freetime_var.get()]
        goout = goout_map[goout_var.get()]
        Medu = Medu_map[Medu_var.get()]
        Fedu = Fedu_map[Fedu_var.get()]

        # Numeric inputs
        failures = safe_int(failures_entry.get(), "Failures")
        absences = safe_int(absences_entry.get(), "Absences")
        G1 = safe_int(g1_entry.get(), "G1")
        G2 = safe_int(g2_entry.get(), "G2")

        # ---------- VALIDATION ----------

        if failures < 0 or failures > 3:
            raise ValueError("Failures must be between 0 and 3")

        if absences < 0 or absences > 50:
            raise ValueError("Absences must be between 0 and 50")

        if G1 < 0 or G1 > 20 or G2 < 0 or G2 > 20:
            raise ValueError("G1 and G2 must be between 0 and 20")

        # ---------- PREDICTION ----------

        values = [[studytime, failures, absences, G1, G2,
                   health, freetime, goout, Medu, Fedu]]

        result = model.predict(values)[0]

        # Clamp result
        result = max(0, min(20, result))

        # ---------- INTERPRETATION ----------

        if result >= 16:
            level = "Excellent"
        elif result >= 12:
            level = "Good"
        elif result >= 8:
            level = "Average"
        elif result >= 4:
            level = "Poor"
        else:
            level = "Very Poor"

        # ---------- REASONING ----------

        reasons = []

        if G1 > 12 and G2 > 12:
            reasons.append("Strong previous academic performance")

        if absences > 10:
            reasons.append("High absences may reduce performance")

        if studytime >= 3:
            reasons.append("Good study time improves results")

        if failures > 0:
            reasons.append("Past failures negatively affect score")

        reason_text = "\n".join(reasons) if reasons else "No major factors detected"

        # ---------- OUTPUT ----------

        output_label.config(
            text=f"Predicted G3: {round(result,2)} / 20\n"
                 f"Performance: {level}\n\n"
                 f"Reason:\n{reason_text}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------- GUI SETUP ----------

root = tk.Tk()
root.title("Student Performance Predictor")

# ---------- DROPDOWNS WITH REAL MEANING ----------

studytime_var, studytime_map = create_dropdown(
    root,
    "Study Time:\n(<2 hrs, 2–5 hrs, 5–10 hrs, >10 hrs per week)",
    {
        "< 2 hrs/week": 1,
        "2–5 hrs/week": 2,
        "5–10 hrs/week": 3,
        "> 10 hrs/week": 4
    },
    0
)

health_var, health_map = create_dropdown(
    root,
    "Health:\n(1=very bad → 5=excellent)",
    {
        "Very Bad": 1,
        "Bad": 2,
        "Average": 3,
        "Good": 4,
        "Excellent": 5
    },
    5
)

freetime_var, freetime_map = create_dropdown(
    root,
    "Free Time:\n(1=very low → 5=very high)",
    {
        "Very Low": 1,
        "Low": 2,
        "Medium": 3,
        "High": 4,
        "Very High": 5
    },
    6
)

goout_var, goout_map = create_dropdown(
    root,
    "Going Out:\n(1=rarely → 5=very often)",
    {
        "Rarely": 1,
        "Less": 2,
        "Sometimes": 3,
        "Often": 4,
        "Very Often": 5
    },
    7
)

Medu_var, Medu_map = create_dropdown(
    root,
    "Mother Education:",
    {
        "None": 0,
        "Primary School": 1,
        "Middle School": 2,
        "Secondary School": 3,
        "Higher Education": 4
    },
    8
)

Fedu_var, Fedu_map = create_dropdown(
    root,
    "Father Education:",
    {
        "None": 0,
        "Primary School": 1,
        "Middle School": 2,
        "Secondary School": 3,
        "Higher Education": 4
    },
    9
)

# ---------- INPUT FIELDS ----------

def create_entry(root, text, row):
    tk.Label(root, text=text).grid(row=row, column=0, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=row, column=1)
    return entry

failures_entry = create_entry(root, "Failures (0–3)", 1)
absences_entry = create_entry(root, "Absences (0–30 typical, max 50)", 2)
g1_entry = create_entry(root, "G1 Marks (0–20)", 3)
g2_entry = create_entry(root, "G2 Marks (0–20)", 4)

# ---------- BUTTON ----------

tk.Button(root, text="Predict", command=predict).grid(row=10, column=0, columnspan=2)

# ---------- OUTPUT ----------

output_label = tk.Label(root, text="", justify="left")
output_label.grid(row=11, column=0, columnspan=2)

root.mainloop()