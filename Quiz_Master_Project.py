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
rid1 = int(input("I am a odd number, Take away a letter and I become even. What number am I?(Answer In Number Form)"))
answer_count += 1
if rid1 == 7:
    correct_answer += 1
    print("This Is Correct! Your Score Is Now: ", correct_answer, "/", answer_count)
else:
    print("Wrong :( The Answer Was 7, Seven - S = even, Get it?. Your Score Is Now", correct_answer, "/", answer_count)
print()

print("Question 2")
answer_count += 1
print("What has to be broken before you can use it?")
print("A. s")
print("B. An Egg")
print("C.")
print("D. ")
rid2 = input("What is the answer?")
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
answer_count += 1
print()


print("Question 5")
answer_count += 1
print("It belongs to you, but other people use it more than you do. What is it?")
print("A.")
print("B.")
print("C.")
print("D. Your Name ")

rid5 = input()
print()

print("Question 6")
answer_count += 1
print()

print("Question 7")
answer_count += 1

print(answer_count)
