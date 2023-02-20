# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID:  IIT :20210883,  westminster :- w1953877
# Date: 12/12/2022


#Import outcome packages
import student
import staff

#Initialize variable
title = ""
title_2 = ""
align = 0
align_2 = 0
menu = 0

#Heading display
print()
title = " ******WESTMINSTER****** "
title_2 = "\\\\\\\\\\\\ <><><>PREDICT PROGRESSION SYSTEM<><><> //////"
align =title.center(92)
align_2 = title_2.center(90)
print(align)
print(align_2)


#Create menu for outputs
def menu():
    while True:
        try:
            print("\n")
            menu= input("Enter '1' to Open Students Version: \n"
                        "Enter '2' to Open Staff Version : \n"
                        "Enter 'q' to Quit: ")
        except ValueError:
            print("***PLEASE SELECT THE CORRECT NUMBER '1' '2' or 'q'***")
        else:
            if menu == "1" :
                print("\n")
                print("=" * 80)
                print("Student Version\n")
                student.index_id()
                student.validation()
                print("=" * 80)
           
            elif menu == "2" :
                print("\n")
                print("=" * 80)
                print("Staff Version\n")
                while True:
                    staff.index_id()
                    staff.validation()
                    close =staff.run_again()
                    staff.list_file()
                    print()
                    staff.file_read()
                    print()
                    staff.dicts ()
                    break                    
            
                
                    print("=" * 80)
            elif menu == "q":
                print("\n")
                print("THANK YOU \nprogram is Quiting")
                quit()
            else:
                print("***PLEASE SELECT THE CORRECT OPTION '1' '2' or 'q'***")
                
menu()

 







#References
#https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50
#https://www.entechin.com/how-to-print-a-list-without-square-brackets-in-python/
#https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python
#https://appdividend.com/2022/09/24/python-zip-dictionary/


                        
