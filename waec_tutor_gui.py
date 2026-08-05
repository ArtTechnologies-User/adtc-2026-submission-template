import tkinter as tk
from tkinter import scrolledtext, filedialog, simpledialog
from llama_cpp import Llama
import threading

# Create window first
root = tk.Tk()
root.title("WAEC Tutor")

# Subject dropdown
subject_var = tk.StringVar(value="Biology")
subjects = [
    "Biology", "Chemistry", "Physics", "Mathematics", "English",
    "Agricultural Science", "Geography", "Economics", "Government",
    "Literature", "Commerce", "Accounting"
]
subject_menu = tk.OptionMenu(root, subject_var, *subjects)
subject_menu.pack(pady=5)

# Question entry
entry = tk.Entry(root, width=80)
entry.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Chat box
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
chat_box.pack(pady=10)
chat_box.insert(tk.END, "👋 Welcome to WAEC Tutor!\n"
                        "Answers will now include Summary, Detailed Explanation, and Example.\n"
                        "Select a subject, type your question, or generate a quiz to begin.\n\n")

# Global model variable
llm = None

# Load model in background thread
def load_model():
    global llm
    llm = Llama(model_path="models/llama-2-7b-chat-hf-q4_k_m.gguf", n_threads=8)

threading.Thread(target=load_model).start()

# --- Functions ---
def ask_question():
    if llm is None:
        chat_box.insert(tk.END, "⏳ Model is still loading, please wait...\n\n")
        return
    subject = subject_var.get()
    question = entry.get()
    if not question.strip():
        return
    prompt = f"""
    Subject: {subject}
    Q: {question}
    A: Please provide the answer in three layers:
    1. Summary: A short, clear answer.
    2. Detailed Explanation: Step-by-step reasoning or deeper context.
    3. Example: A practical illustration or analogy.
    """
    # Removed timeout, kept max_tokens for speed
    output = llm(prompt, max_tokens=250)
    answer = output["choices"][0]["text"].strip()
    chat_box.insert(tk.END, f"[{subject}] Q: {question}\n{answer}\n\n")
    entry.delete(0, tk.END)


def clear_chat():
    chat_box.delete(1.0, tk.END)

def save_chat():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(chat_box.get(1.0, tk.END))

score = {"correct": 0, "total": 0}

def generate_quiz():
    if llm is None:
        chat_box.insert(tk.END, "⏳ Model is still loading, please wait...\n\n")
        return
    subject = subject_var.get()
    prompt = f"Generate one WAEC-style multiple choice question in {subject}. Provide 4 options (A-D) and indicate the correct answer clearly."
    output = llm(prompt, max_tokens=150, timeout=60)
    quiz_text = output["choices"][0]["text"].strip()
    chat_box.insert(tk.END, f"[{subject} Quiz]\n{quiz_text}\n\n")

    user_answer = simpledialog.askstring("Your Answer", "Enter your choice (A/B/C/D):")
    if user_answer:
        score["total"] += 1
        if f"Answer: {user_answer.strip().upper()}" in quiz_text:
            score["correct"] += 1
            chat_box.insert(tk.END, f"✅ Correct! Your score: {score['correct']}/{score['total']}\n\n")
        else:
            chat_box.insert(tk.END, f"❌ Incorrect. Your score: {score['correct']}/{score['total']}\n\n")

# Buttons
ask_button = tk.Button(button_frame, text="Ask", command=ask_question)
ask_button.pack(side=tk.LEFT, padx=5)

quiz_button = tk.Button(button_frame, text="Generate Quiz", command=generate_quiz)
quiz_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear Chat", command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save Chat", command=save_chat)
save_button.pack(side=tk.LEFT, padx=5)

# Run app
if __name__ == "__main__":
    root.mainloop()
