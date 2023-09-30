class Question:
                        def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, correct_answer):
        new_question = Question(question, options, correct_answer)
        self.questions.append(new_question)

    def administer_quiz(self):
        score = 0
        for question in self.questions:
            print(question.question)
            for i, option in enumerate(question.options, 1):
                print(f"{i}. {option}")
            user_answer = int(input("Your answer (enter the option number): "))
            if user_answer == question.correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect. The correct answer was option", question.correct_answer, "\n")
        print("Quiz completed. Your score:", score, "out of", len(self.questions))

def main():
    quiz = Quiz()

    # Administrator adds questions
    quiz.add_question("What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], 1)
    quiz.add_question("What is 2 + 2?", ["1", "3", "4", "5"], 3)
    quiz.add_question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1)

    print("Welcome to the Quiz Application!")
    user_type = input("Are you an (A)dministrator or (U)ser? ").lower()

    if user_type == "a":
        quiz.administer_quiz()
    elif user_type == "u":
        print("\nLet's start the quiz!")
        quiz.administer_quiz()
    else:
        print("Invalid user type. Please enter 'A' for Administrator or 'U' for User.")

if __name__ == "__main__":
    main()

