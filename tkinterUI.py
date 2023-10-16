import tkinter as tk
from tkinter import ttk

def get_auth_info():
    def submit():
        global input1, input2, input3
        input1 = entry1.get()
        input2 = entry2.get()
        input3 = entry3.get()
        entry1.config(state='readonly')
        entry2.config(state='readonly')
        entry3.config(state='readonly')
        root.quit()

    root = tk.Tk()
    root.title("Bard Authentication UI")

    # Set window dimensions and position
    window_width = 800
    window_height = 250
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set a custom background color
    root.configure(bg='#f0f0f0')

    label1 = tk.Label(root, text="PSID:", bg='#f0f0f0')
    label1.pack(pady=(10, 0))

    entry1 = tk.Entry(root)
    entry1.pack(pady=(0, 10), padx=10, fill=tk.X)

    label2 = tk.Label(root, text="PSIDCC:", bg='#f0f0f0')
    label2.pack(pady=(10, 0))

    entry2 = tk.Entry(root)
    entry2.pack(pady=(0, 10), padx=10, fill=tk.X)

    label3 = tk.Label(root, text="PSIDTS:", bg='#f0f0f0')
    label3.pack(pady=(10, 0))

    entry3 = tk.Entry(root)
    entry3.pack(pady=(0, 10), padx=10, fill=tk.X)

    submit_button = tk.Button(root, text="Submit", command=submit, bg='#4caf50', fg='white', font=('Arial', 12))
    submit_button.pack(pady=(10, 10), padx=10, fill=tk.X)

    root.mainloop()

    return input1, input2, input3

def bard_ui(PSID, PSIDCC, PSIDTS):
    import requests
    from bardapi import Bard, SESSION_HEADERS
    session = requests.Session()
    token = PSID
    session.cookies.set("__Secure-1PSID", PSID)
    session.cookies.set( "__Secure-1PSIDCC", PSIDCC)
    session.cookies.set("__Secure-1PSIDTS", PSIDTS)
    session.headers = SESSION_HEADERS
    def get_answer():
        question = question_entry.get()
        bard = Bard(token=token, session=session)
        answer = bard.get_answer(question)
        answer_label.config(text=answer)

    root = tk.Tk()
    root.title("Bard UI")
    root.geometry("400x200")

    frame = ttk.Frame(root, padding=(10, 10))
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    frame.columnconfigure(0, weight=1)

    question_label = ttk.Label(frame, text="Ask a question:")
    question_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))

    question_entry = ttk.Entry(frame, width=40)
    question_entry.grid(row=1, column=0, padx=(0, 5))

    get_answer_button = ttk.Button(frame, text="Get Answer", command=get_answer)
    get_answer_button.grid(row=1, column=1)

    answer_label = ttk.Label(frame, text="", font=("Helvetica", 12, "bold"), wraplength=350)
    answer_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()