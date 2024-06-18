class Question:
    def __init__(self, text, answer):
        self.text = text
        self.score = 0
        self.answer = answer

question_data = [
    {"text": "A slugs blood is gren", "answer": "true"},
    {"text": "Loudest animal is the african elephant", "answer": "false"}
]
questions=[]
for question in question_data:
    q_text=question["text"]
    q_answer=question["answer"]
    questionstemp=Question(q_text, q_answer)
    questions.append(questionstemp)


class QuizBrain():
    def __init__(self, question_list):
        self.question_number=0
        self.question_list = question_list
    
    def morequestions(self):
        if self.question_number+1 < len(questions):
            return True
    
    def askquestion(self):
        q=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {q.text} (True/false): ")
        self.check_answer(user_answer, q.answer)
    
    def check_answer(self, user_answer, correctanswer):
        if user_answer == correctanswer:
            self.score+=1
            print("you got it right")
            print(f"your score is {self.score}/{self.question_number}")
        else:
            print(f"Thats wrong, the correct answer is {correctanswer}")       

quiz = QuizBrain(questions)

while quiz.morequestions:
    quiz.askquestion()