import random
import sys 
import subprocess
import timeit

# subprocess.check_call([sys.executable, "-m", "pip", "install", "colored"])
# subprocess.check_call([sys.executable, "-m", "pip", "install", "cprint"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])

from termcolor import colored, cprint


question_type = (int)(input("What type of questions: \n 1. Addition \n 2. Subtraction \n 3. Multiplications ") or "1")
num_question = (int)(input("How many questions? (default 10)") or "10")
min_num = (int)(input("What is the smallest number? (default 1)") or "1")
max_num = (int)(input("What is the largest number? (default 10)") or "10")


cprint(f"Question type: {question_type}", "green")
cprint(f"Number of question: {num_question}", "green")
cprint(f"Range: {min_num} - {max_num}", "green")


ready = input("Read to start? (Y/N)")

if (ready != "y"): exit()

def do_addition():
    num_correct=0
    while(num_correct < num_question):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        answer = input(f"{num1} + {num2} = ")

        while(not answer.isnumeric() or float(answer) != num1+num2):
            cprint("\u2717 Try again.", "red")
            answer=input()

        cprint("\u2713 Correct!","green")
        
        num_correct = num_correct + 1

        cprint(f"Progress: {num_correct}/{num_question}","green")
    end = timeit.default_timer()
    elaspe = format(end - start, '.2f')
    cprint(f"Total time: {elaspe}s")
    print("Good Bye")



def do_substration():
    num_correct=0
    answer=""
    while(num_correct < num_question):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        
        while (num1 < num2):
            num1 = random.randint(min_num, max_num)
        answer = input(f"{num1} - {num2} = ")

        while(not answer.isnumeric() or float(answer) != num1 - num2):
            cprint("\u2717 Try again.", "red")
            answer=input()

        cprint("\u2713 Correct!","green")
        
        num_correct = num_correct + 1

        cprint(f"Progress: {num_correct}/{num_question}","green")
    end = timeit.default_timer()
    elaspe = format(end - start, '.2f')
    cprint(f"Total time: {elaspe}s")
    print("Good Bye")


def do_multiple():
    num_correct=0
    while(num_correct < num_question):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)
        answer = input(f"{num1} x {num2} = ")

        while(not answer.isnumeric() or float(answer) != num1 * num2):
            cprint("\u2717 Try again.", "red")
            answer=input()

        cprint("\u2713 Correct!","green")
        
        num_correct = num_correct + 1

        cprint(f"Progress: {num_correct}/{num_question}","green")
    end = timeit.default_timer()
    elaspe = format(end - start, '.2f')
    cprint(f"Total time: {elaspe}s")
    print("Good Bye")

start = timeit.default_timer()
num_correct=0
if (question_type == 1): do_addition()
elif (question_type == 2): do_substration()
elif (question_type == 3): do_multiple()
else: cprint("Invalid type selection", "red")






# while(num_correct < num_question):
#     num1 = random.randint(min_num, max_num)
#     num2 = random.randint(min_num, max_num)
#     answer = input(f"{num1} + {num2} = ")

#     while(not answer.isnumeric() or float(answer) != num1+num2):
#         cprint("\u2717 Try again.", "red")
#         answer=input()

#     cprint("\u2713 Correct!","green")
    
#     num_correct = num_correct + 1

#     cprint(f"Progress: {num_correct}/{num_question}","green")
# end = timeit.default_timer()
# elaspe = format(end - start, '.2f')
# cprint(f"Total time: {elaspe}s")
# print("Good Bye")
