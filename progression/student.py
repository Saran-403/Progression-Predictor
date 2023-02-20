# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:  IIT :20210883,  westminster :- w1953877
# Date: 12/12/2022




#Initialize Variable
credit = [0, 20, 40, 60, 80, 100, 120]


pass_credits = 0
defer_credits = 0
fail_credits = 0
stu_id_no = 0
id_1 =[]

#Part-A
#Checking & display progress outcome 
def progress_outcome(pass_credits,defer_credits):
    if pass_credits == 120:
        print("Progress")
    elif pass_credits == 100:
        print("Progress (module trailer)")
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")

#Part - 4
#Create student id & validate
def index_id():
    """ The student id is validated using the Westminster 8-character format, with an index[0]= "w" """
    
    global stu_id_no,id_1
    while True:
        stu_id_no = input("Please enter student id number: ").lower()
        if len(stu_id_no)!= 8 and (stu_id_no[0])!= ["w","W"]:
            print("Invalid student id")
            continue
        else:
            if stu_id_no in id_1 :
                print("student id number is already there")
                continue
        id_1.append(stu_id_no)
        break
    
#Part -B
#Credits input Validation
def validation():
    
    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if pass_credits not in credit:
                print("Out of range")
            elif pass_credits in credit:
                break
        

    while True:
        try:
            defer_credits = int(input("Please enter your credits at defer: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if defer_credits not in credit:
                print("Out of range")
            elif defer_credits in credit:
                break
       

    while True:
        try:
            fail_credits = int(input("Please enter your credits at fail: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if fail_credits not in credit:
                print("Out of range")
            elif fail_credits in credit:
                break
        
            
                
    while True:
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            validation()
            break
        else:
            progress_outcome(pass_credits, defer_credits)
            break



#References
#https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50
#https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
#https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python
#https://appdividend.com/2022/09/24/python-zip-dictionary/

