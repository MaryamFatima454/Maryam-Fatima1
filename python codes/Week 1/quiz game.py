questions = [
    {"question": "What is the capital of Pakistan?", "answer": "islamabad"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "Who wrote 'Hamlet'?", "answer": "shakespeare"},
    {"question": "What is the chemical symbol for water?", "answer": "h2o"},
]
def run_quiz():
    score = 0
    for q in questions:
        user_answer = input(q["question"] + " ").lower()
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    print(f"You got {score} out of {len(questions)} correct.")
print("Welcome to the Quiz Game!\n")
run_quiz()
