import tkinter as tk
from tkinter import ttk

def submit_form():
    data = {
        "role": role_var.get().strip(),
        "level": level_var.get(),
        "tools": tools_var.get(),
        "languages": languages_var.get(),
        "frameworks": frameworks_var.get(),
        "cloud": cloud_var.get(),
        "field": field_var.get(),
        "degree": degree_var.get(),
        "gpa": gpa_var.get(),
        "languages_required": languages_required_var.get(),
        "experience": experience_var.get(),
        "activities": activities_var.get(),
        "references": "dr. smith"
    }
    print("🌟 Collected JD Data:")
    for k, v in data.items():
        print(f"{k}: {v}")

# Yellow theme
bg_color = "#FFFACD"       # Lemon Chiffon
frame_color = "#FFF8DC"    # Cornsilk
button_color = "#FFD700"   # Gold
highlight_color = "#FFEC8B"  # Light Goldenrod

root = tk.Tk()
root.title("🌞 JD Prompt Input")
root.geometry("820x780")
root.configure(bg=bg_color)

# Header
header = tk.Label(root, text="💛 JD Prompt Input", font=("Comic Sans MS", 22, "bold"),
                  bg=bg_color, fg="#DAA520")
header.pack(pady=25)

# Center container
container = tk.Frame(root, bg=bg_color)
container.pack(expand=True)

# Main rounded-like frame
main_frame = tk.Frame(container, bg=frame_color, bd=2, relief="ridge")
main_frame.pack(padx=20, pady=10)

def cute_frame(title):
    return tk.LabelFrame(main_frame, text=title, font=("Comic Sans MS", 12, "bold"),
                         bg=frame_color, fg="#DAA520", padx=10, pady=10, bd=2, relief="groove")

# Variables
role_var = tk.StringVar()
level_var = tk.StringVar(value="senior")
tools_var = tk.StringVar(value="docker, git")
frameworks_var = tk.StringVar(value="react, django")
languages_var = tk.StringVar(value="python, react")
cloud_var = tk.StringVar(value="mysql, aws")
field_var = tk.StringVar(value="computer science")
degree_var = tk.StringVar(value="bachelor")
gpa_var = tk.StringVar(value=">= 3.2")
languages_required_var = tk.StringVar(value="english")
experience_var = tk.IntVar(value=2)
activities_var = tk.StringVar(value="open-source, hackathon")

def add_label_entry(frame, text, var, row, column):
    tk.Label(frame, text=text, font=("Comic Sans MS", 10), bg=frame_color).grid(row=row, column=column, sticky="w", pady=5)
    entry = tk.Entry(frame, textvariable=var, font=("Comic Sans MS", 10), width=25)
    entry.grid(row=row, column=column + 1, padx=5, pady=5)
    return entry


role_frame = cute_frame("🧑‍💼 Role Info")
role_frame.grid(row=0, column=0, padx=10, pady=10)
add_label_entry(role_frame, "Role:", role_var, 0, 0)
tk.Label(role_frame, text="Level:", font=("Comic Sans MS", 10), bg=frame_color).grid(row=0, column=2, sticky="w")
tk.OptionMenu(role_frame, level_var, "junior", "mid", "senior", "lead").grid(row=0, column=3, padx=5)


stack_frame = cute_frame("🛠️ Tech Stack")
stack_frame.grid(row=1, column=0, padx=10, pady=10)
add_label_entry(stack_frame, "Tools:", tools_var, 0, 0)
add_label_entry(stack_frame, "Frameworks:", frameworks_var, 1, 0)
add_label_entry(stack_frame, "Languages:", languages_var, 0, 2)
add_label_entry(stack_frame, "Cloud/DB:", cloud_var, 1, 2)

edu_frame = cute_frame("🎓 Education")
edu_frame.grid(row=2, column=0, padx=10, pady=10)
add_label_entry(edu_frame, "Field of Study:", field_var, 0, 0)
add_label_entry(edu_frame, "Degree:", degree_var, 0, 2)
add_label_entry(edu_frame, "GPA:", gpa_var, 1, 0)

lang_frame = cute_frame("🌍 Languages & Hobbies")
lang_frame.grid(row=3, column=0, padx=10, pady=10)
add_label_entry(lang_frame, "Required Language(s):", languages_required_var, 0, 0)
tk.Label(lang_frame, text="Years of Experience:", font=("Comic Sans MS", 10), bg=frame_color).grid(row=0, column=2)
tk.Spinbox(lang_frame, from_=0, to=50, textvariable=experience_var, width=5).grid(row=0, column=3, padx=5)
add_label_entry(lang_frame, "Activities:", activities_var, 1, 0)


submit_btn = tk.Button(root, text="🌟 Submit 🌟", font=("Comic Sans MS", 12, "bold"),
                       bg=button_color, fg="white", activebackground=highlight_color,
                       padx=25, pady=10, command=submit_form, relief="raised", bd=3)
submit_btn.pack(pady=25)


def on_enter(e): submit_btn.config(bg=highlight_color)
def on_leave(e): submit_btn.config(bg=button_color)

submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

root.mainloop()
