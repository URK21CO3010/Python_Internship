class Question:

    def __init__(self, prompt: str, options: list[str], answer_index: int) -> None:
        self.prompt = prompt
        self.options = options
        self.answer_index = answer_index
    
    def change_prompt(self, new_prompt: str) -> None:
        self.prompt = new_prompt
    
    def change_options(self, new_options: list[str]) -> None:
        self.options = new_options
    
    def change_answer_index(self, new_answer_index: int) -> None:
        self.answer_index = new_answer_index


class Quiz:
    
    def __init__(self, questions: list[Question]) -> None:
        self.questions = questions
        self.score = 0
        self.number_of_questions = len(questions)
    
    def start_quiz(self) -> None:

        for question in self.questions:
            
            print(question.prompt)

            for index, option in enumerate(question.options):
                print(str(index + 1) + ".", option)

            user_input = input("Select the correct option : ")

            while user_input <= "1" or user_input >= str(len(question.options) + 1):
                print("Invalid option")
                user_input = input("Select the correct option : ")
            
            user_answer = int(user_input) - 1

            if question.answer_index == user_answer:
                self.score += 1
                print("Correct")

            else:
                print("Wrong answer. The correct answer is :", str(index + 1) + ".", question.options[question.answer_index])
    
    def get_score(self):
        print("Your Score :", self.score, "out of", self.number_of_questions)

    

question_1 = Question(prompt = "What year is it?", options = ["2022", "2023", "2024", "2025"], answer_index = 2)

question_2 = Question(prompt = "What is the color of a tennis ball?", options = ["red", "blue", "green", "yellow"], answer_index = 3)

question_3 = Question(prompt = "How does sugar taste?", options = ["sweet", "bitter", "sour", "spicy"], answer_index = 0)


quiz = Quiz(questions = [question_1, question_2, question_3])
quiz.start_quiz()
