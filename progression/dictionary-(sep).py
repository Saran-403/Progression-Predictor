# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:  IIT :20210883,  westminster :- w1953877
# Date: 12/12/2022






#Initialize Variable
credit = [0, 20, 40, 60, 80, 100, 120]
progress = []
trailer = []
retriever = []
exclude = []

progress_list =[]
trailer_list = []
retriever_list = []
exclude_list = []

pass_credits = 0
defer_credits = 0
fail_credits = 0
stu_id_no = 0

credit_list = []
diction={}
id_1 = []

#Checking & display progress outcome 
def progress_outcome(pass_credits,defer_credits,fail_credits):
    if pass_credits == 120 :
        print("Progress")
        progress_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 100:
        print("Progress (module trailer)")
        trailer_list.extend([[pass_credits,defer_credits,fail_credits]]) 
    elif pass_credits == 80:
        print("Do not Progress - module retriever")
        retriever_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 60:
        print("Do not Progress - module retriever")
        retriever_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 40 and defer_credits != 0:
        print("Do not Progress - module retriever")
        retriever_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 20 and defer_credits >= 40:
        print("Do not Progress - module retriever")
        retriever_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 0 and defer_credits >= 60:
        print("Do not Progress - module retriever")
        retriever_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 40 and defer_credits == 0:
        print("Exclude")
        exclude_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 20 and defer_credits <= 20:
        print("Exclude")
        exclude_list.extend([[pass_credits,defer_credits,fail_credits]])
    elif pass_credits == 0 and defer_credits <= 40:
        print("Exclude")
        exclude_list.extend([[pass_credits,defer_credits,fail_credits]])

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
    
#Credits input Validation
def validation():
    
    while True:
        try:
            pass_credits = int(input("Please enter student credits at pass: "))
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
            defer_credits = int(input("Please enter student credits at defer: "))
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
            fail_credits = int(input("Please enter student credits at fail: "))
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
            progress_outcome(pass_credits, defer_credits,fail_credits)
            break
        
#Entering New Dataset     
def run_again():
    while True:
        print("\n")
        try:
            close = input("Would you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ")
        except ValueError:
            print("Please Enter 'y' or 'q'")
        else:
            if close == "q" or close == "Q":
                print()
                dicts ()
                break

            elif close == "y" or close == "Y":
                print()
                index_id()
                validation()             
            else:
                print("Please Enter 'y' or 'q'")
    return close


#Create dictionary to save and display the dataset       
def dicts ():
    for i in progress_list:
        id_1
        credit_list.append("progress - "+",".join(str(x) for x in i))
        diction=dict(zip(id_1,credit_list))
    
    for i in trailer_list:
        id_1
        credit_list.append("Progress (module trailer) - "+",".join(str(x) for x in i))
        diction=dict(zip(id_1,credit_list))
        
    for i in retriever_list:
        id_1
        credit_list.append("Module retriever - "+",".join(str(x) for x in i))
        diction=dict(zip(id_1,credit_list))
                   
    for i in exclude_list:
        id_1
        credit_list.append("Exclude - "+",".join(str(x) for x in i))
        diction=dict(zip(id_1,credit_list))
   
    print('\n'.join("{} : {}".format(id_1,credit_list) for id_1,credit_list in diction.items()))


#dictionary acessing menu
while True:
    try:
        print()
        menu= input("Enter '1' to Enter Students credit: \n"
                    "Enter '2' quit the program :")
            
    except ValueError:
        print("***PLEASE SELECT THE CORRECT NUMBER '1' or '2''***")
    else:
        if menu == "1" :
            while True:
                print()
                index_id()
                validation()
                run_again()
                break
                    
        elif menu == "2":
            print("\n")
            print("THANK YOU \nprogram is Quiting")
            quit()
             
        else:
            print("***PLEASE SELECT THE CORRECT OPTION '1' or '2'***")
                




#References
#https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50
#https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
#https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python
#https://appdividend.com/2022/09/24/python-zip-dictionary/

