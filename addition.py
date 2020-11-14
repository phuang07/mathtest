import random
import sys 
import subprocess
import timeit

# subprocess.check_call([sys.executable, "-m", "pip", "install", "colored"])
# subprocess.check_call([sys.executable, "-m", "pip", "install", "cprint"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])

from termcolor import colored, cprint

num_question = 100 
min_num = 1
max_num = 10
num_correct=0

start = timeit.default_timer()

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
