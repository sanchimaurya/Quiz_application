def load_questions(file):
    questions = []
    try:
        with open(file, 'r') as file:
            for line in file:
                parts = line.strip().split("Answer:")
                if len(parts) == 2:
                    question = parts[0].strip()
                    answer = parts[1].strip()
                    questions.append((question, answer))

                    
    except FileNotFoundError:
        print("Error: The file", file," does not exist.")
        return []
    return questions

def save_score(score):
    with open('E:\\scores.txt', 'a') as file:
        file.write(f'Score: {score}\n')

def main():
    print("Welcome to the Quiz Application! by Adiba & Sanchi")

    while True:
        choice = input("Choose the type of questions (gk / heritage/ reasoning): ").strip().lower()
        
        if choice == "gk":
            questions = load_questions('gk.txt')
            break 
        elif choice == "heritage":
            questions = load_questions('heritage.txt')
            break
        elif choice == "reasoning":
            questions = load_questions('reasoning.txt')
            break  
        else:
            print("Invalid choice! Please select 'gk' or 'heritage'.")

    if not questions:
        print("No questions loaded. Exiting.")
        return

    score = 0
    for i, (question, answer) in enumerate(questions):
        print(f'{question}')
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == answer.lower():
            score += 10
            print("Correct!")
        else:
            print("Wrong! The correct answer is: ",answer)

    print("Your final score is: ",score)
    save_score(score)
    print("Your score has been saved.")

main()

