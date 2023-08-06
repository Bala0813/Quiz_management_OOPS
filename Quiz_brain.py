class Quiz_brain:
    def __init__(self, question_list):
        self.question_no = 0
        self.questions = question_list
        self.current_score = 0

    def process_question_list(self):
        return self.question_no < len(self.questions)

    def check_solution(self, correct_answer, user_answer):
        return correct_answer == user_answer


    def next_question(self):
        current_question = self.questions[self.question_no]
        self.question_no += 1
        user_response = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        sys_check = self.check_solution(current_question.answer, user_response)
        if sys_check:
            self.current_score += 1
            print("Hurray, you got it.")
        else:
            print("You missed it.")
        print(f"The correct answer is {current_question.answer}")
        print(f"Your current score is {self.current_score}/{self.question_no}")
        print("\n")

