"""Check bank loan approval
Hint:
Ask the user to enter:
salary
credit score
experience
Use:
AND operator
IF
ELIF
ELSE
Compare:
salary > 50000
creditscore > 750
experience > 3
If all conditions satisfy:
Print "Loan Approved"""

sal=int(input("enter your salary : "))
sco=int(input("enter your score : "))
exp=int(input("enter your experince : "))
if(sal>50000 and sco>750 and exp >3):
    print("Loan Approval")
elif(sal>25000 and sco>350 and exp >2):
    print("LOan under review")
else:
    print("Loan Rejected")