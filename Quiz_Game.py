print("=================================")
print("      WELCOME TO QUIZ GAME")
print("=================================")

questions = {
    "1. Capital of India? ": "Delhi",
    "2. 2 + 2 = ? ": "4",
    "3. Which language is used for AI and ML? ": "Python",
    "4. Who is known as the Father of Computers? ": "Charles Babbage",
    "5. What does CPU stand for? ": "Central Processing Unit"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)

    if user_answer.lower() == answer.lower():
        print("Correct Answer!\n")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer is:", answer)
        print()

print("=================================")
print("QUIZ COMPLETED")
print("=================================")

print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: D")

print("Thank You For Playing!")