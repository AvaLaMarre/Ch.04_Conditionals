'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
print("Welcome To My Quiz, This Quiz Is About Riddles ")
answer_count = 0
correct_answer = 0
print()

print("Question 1")
rid1 = int(input("I am a odd number, Take away a letter and I become even. What number am I?(Answer In Number Form) "))
answer_count += 1
if rid1 == 7:
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was 7, (Seven - S = even) Get it?. Your Score Is Now", correct_answer, "/", answer_count)
print()

print("Question 2")
answer_count += 1
print("What has to be broken before you can use it?")
print("A. Bones")
print("B. Eggs")
print("C. Muscles")
rid2 = input("What Is The Answer: ")
if rid2 == "B" or rid2 == "b":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was B. An Egg. Your Score Is Now", correct_answer, "/", answer_count)
print()


print("Question 3")
rid3 = input(" David’s parents have three sons: Snap, Crackle, and what’s the name of the third son? ")
answer_count += 1
if rid3 == "David" or rid3 == "david":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was David. Your Score Is Now", correct_answer, "/", answer_count)
print()

print("Question 4")
print("What can you catch but not throw?")
print("A. A Baseball")
print("B. Hands")
print("C. A Cold")
rid4 = input("What Is The Answer: ")
answer_count += 1
if rid4 == "C" or rid4 == "c" or rid4 == "A Cold" or rid4 == "a cold":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was C: A Cold, Your Score Is Now", correct_answer, "/", answer_count)
print()


print("Question 5")
answer_count += 1
print("It belongs to you, but other people use it more than you do. What is it?")
print("A. Your Car")
print("B. Your Heart")
print("C. Your Name ")
rid5 = input("What Is The Answer? ")
if rid5 == "C" or rid5 == "c":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was C: Your Name. Your Score Is Now", correct_answer, "/", answer_count)
print()

print("Question 6")
rid6 = input("What can you keep after giving it to someone? Your ")
if rid6 == "word" or rid6 == "Word":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was Your Word. Your Score Is Now", correct_answer, "/", answer_count)
answer_count += 1
print()

print("Question 7")
rid7 = input("If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I? I Am A ")
answer_count += 1
if rid7 == "Secret" or rid7 == "secret":
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was D: Your Name. Your Score Is Now", correct_answer, "/", answer_count)
print()

print("THE END ")
print(correct_answer, "/", answer_count)
end_score = (correct_answer/answer_count) * 100
end_score = round(end_score)
if end_score >= 90:
    print(end_score, "% Letter Grade = A")
elif end_score >= 80:
    print(end_score, "% Letter Grade = B")
elif end_score >= 70:
    print(end_score, "% Letter Grade = C")
elif end_score >= 60:
    print(end_score, "% Letter Grade = D")
else:
    print(end_score, "% Letter Grade = F")
print("Thanks For PLaying!")
