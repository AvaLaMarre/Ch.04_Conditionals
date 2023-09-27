# 4.0 Jedi Training (40pts)  Name:________________
#Below each program list the mistakes found in comments.

#1. Make the following program work. (3 mistakes)  (3pts)
     
midichlorians = float(input("Enter midichlorian count: "))
if midichlorians > 10000:
    print("You have serious Jedi potential")
else:
    print("Jedi, you will never be.")
#missing a ) first line
#there is no : at the end of the if statement
#line nine should be else not elif

# 2. Make the following program work. (3 mistakes)  (3pts)
     
x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")
#Line nine should have a int()
#2Line 18 should have a : at the end
#3Line 18 should have == not a =

  # 3. Make the following program work. (4 mistakes)  (4pts)
     
answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")
#1 used diffent varibles, a is not defined
#2Line 29 should have a : after else
#3 Line 29 should be a == not a =
#4

  # 4. Make the following program work. (4 mistakes) (4pts)
     
x = input("Name one of the top 3 greatest Jedi.")
if x == "Yoda" or x == "Luke Skywalker" or x == "Obi-Wan Kenobi":
    print ("That is correct!")

#1diffrent varibles used x is defined not jedi
#2 the equation needs to be printed out every if
#3Missing () on line 39
#4 Input anwers are not in ""

 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)

print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")

if user_input == "A" or user_input == "a" or user_input == "Jedi Master" or user_input == "jedi master":
    sensitivity = 1000
elif user_input == "B" or user_input == "b" or user_input == "Sith Lord" or user_input == "sith lord":
    sensitivity = 900
elif user_input == "C" or user_input == "c" or user_input == "Droid" or user_input == "droid":
    sensitivity = 0
else:
    senstivity = "Not a choice"
print("Sensitivity: ",sensitivity)




'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

number = int(input("Input any number"))
%=2
if number == 0



'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

if grade >= 90:
    print("A")
elif grade>= 80:
    print("B")
elif grade >=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F, Transfer to Johnston")

