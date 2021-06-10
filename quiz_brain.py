


class QuizBrain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def stillHasQuestions(self):
        return self.question_num < len(self.question_list)

    def checkAnswer(self, user_answer, correcrt_answer):
        if user_answer.lower() == correcrt_answer.lower():
            self.score += 1
            print("You got it Right")
        else:
            print("You got it wrong")
        print(f"Current Score: {self.score}/{self.question_num+1}")

    def nextQuestion(self):
        new_qestion = self.question_list[self.question_num]
        q_num = self.question_num +1
        new_q = new_qestion.text
        new_a = new_qestion.answer
        user_answer = input(f"Q{q_num}. {new_q} True/False: ").lower()
        self.checkAnswer(user_answer,new_a)
        self.question_num+= 1
        print("\n")
        if self.question_num == len(self.question_list):
            print("You completed the quiz!")
            print(f"Your final score: {self.score}/{len(self.question_list)}")


