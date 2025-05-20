# Python quiz game

questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the smallest prime number?",
    "What is the chemical symbol for gold?",
    "What is the longest river in the world?",
)

options = (("A. Paris","B. London","C. Berlin","D. Madrid"),
           ("A. Jupiter","B. Saturn","C. Earth","D. Mars"),
           ("A. 1","B. 2","C. 3","D. 4"),
           ("A. Au","B. Ag","C. Fe","D. Pb"),
           ("A. Nile","B. Amazon","C. Yangtze","E. Mississippi"))



answers = ("A", "B", "C", "D", )
quesses = []
score = 0 
questionsNum = 0


for question in questions :
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[questionsNum]:
        print(option)
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    quess = input("Enter your answer: ")
    quesses.append(quess)
    questionsNum += 1
    if quess == answers[questionsNum - 1]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is", answers[questionsNum - 1])
print("~~~~~~~~~~~~~~~~~~~~~~~")

print("You got", score, "out of", len(questions), "correct.")
