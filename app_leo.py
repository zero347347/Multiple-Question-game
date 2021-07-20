
# 1st we already define a new data type[Question] in the other python file
# 2nd we create the question_prompt array
from question import Question

question_prompts = [
    "What is the name of Harry Potter's owl?\n(a) Scabbers\n(b) Hedwig\n(c) Queenie\n(d) Nagini\n\n",
    "Which house is Cedric.D belongs to?\n(a) Gryffindor\n(b) Slytherin\n(c) Hufflepuff\n(d) Ravenclaw\n\n",
    "What creature is Aragog?\n(a) Acromantula\n(b) Unicorn\n(c) Basilisk\n(d) Hippogriffs\n\n",
]

# 3rd we create the another array that includes prompt and related correct answer
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

# the next step is to write a function that will run the function[questions]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct")

# last step is to run the function questions
run_test(questions)
