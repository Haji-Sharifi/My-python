# Quiz game with multiple-choice questions
# This is a simple quiz game where the user is presented with multiple-choice questions.
# The user can input their answers, and at the end, the game will display the correct answers and the user's score.
# Quiz Game

# questions = (
#     "What is the capital of France?",
#     "What is the largest planet in our solar system?",
#     "What is the smallest prime number?",
#     "What is the chemical symbol for gold?",
#     "What is the longest river in the world?",
# )

# options = (
#     ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
#     ("A. Jupiter", "B. Saturn", "C. Earth", "D. Mars"),
#     ("A. 1", "B. 2", "C. 3", "D. 4"),
#     ("A. Au", "B. Ag", "C. Fe", "D. Pb"),
#     ("A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi")
# )

# answers = ("A", "A", "B", "A", "A")  # Correct answers

# guesses = []
# score = 0

# for i in range(len(questions)):
#     print("~~~~~~~~~~~~~~~~~~~~~~~")
#     print(questions[i])
#     for option in options[i]:
#         print(option)
#     print("~~~~~~~~~~~~~~~~~~~~~~~")
#     guess = input("Enter your answer (A/B/C/D): ").upper()
#     guesses.append(guess)

#     if guess == answers[i]:
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Incorrect! The correct answer is {answers[i]}")

# print("~~~~~~~~~~~~~~~~~~~~~~~")
# print("Answers: ", " ".join(answers))
# print("Guesses: ", " ".join(guesses))
# print("~~~~~~~~~~~~~~~~~~~~~~~")


# score = int(score / len(questions) * 100)
# print(f"Your score is {score}%")
