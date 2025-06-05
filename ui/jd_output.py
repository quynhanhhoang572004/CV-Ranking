import tkinter as tk
from tkinter import messagebox, scrolledtext

def config_output(data):

    config_str = f"""
REQUIREMENTS {{
    position: {data['role']}
    level: {data['level']}
    stack {{
        tools: {data['tools']}
        programming languages: {data['languages']}
        framework libraries: {data['frameworks']}
        databases cloud services: {data['cloud']}
    }}
    education {{
        major: {data['field']}
        degree: {data['degree']}
        gpa: {data['gpa']}
    }}
    experience: {data['experience']} years
    language: {data['languages_required']}
    activities: {data['activities']}
    references: {data['references']}
}}""".strip()


    root = tk.Tk()
    root.title("📋 Structured JD Requirements")
    root.geometry("700x600")
    root.configure(bg="#FFF8DC")

    tk.Label(root, text="📋 Structured JD Requirements", font=("Comic Sans MS", 16, "bold"),
             bg="#FFF8DC", fg="#B8860B").pack(pady=10)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25,
                                          font=("Courier New", 10), bg="#FFFAF0")
    text_area.pack(padx=20, pady=10, fill="both", expand=True)
    text_area.insert(tk.END, config_str)
    text_area.config(state=tk.DISABLED)

    def on_submit():
        messagebox.showinfo("✅ Success", "JD submitted successfully!")

    submit_btn = tk.Button(root, text="✅ Submit JD", font=("Comic Sans MS", 12, "bold"),
                           bg="#FFD700", fg="white", padx=20, pady=10, command=on_submit)
    submit_btn.pack(pady=20)

    root.mainloop()

    return config_str


if __name__ == "__main__":
    sample_data = {
        "role": "AI Engineer",
        "level": "senior",
        "tools": "docker, git",
        "languages": "python, react",
        "frameworks": "react, django",
        "cloud": "mysql, aws",
        "field": "computer science",
        "degree": "bachelor",
        "gpa": ">= 3.2",
        "languages_required": "english",
        "experience": "2",
        "activities": "open-source, hackathon",
        "references": "dr. smith"
    }

    config_output(sample_data)