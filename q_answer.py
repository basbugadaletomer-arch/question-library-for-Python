#This code defines the question function
def question(query=None, answer=None, a=None,b=None, c=None,d=None,e=None, aname="a",bname="b",cname="c",dname="d",ename="e"):
    #This if loop checks if there is an error in the code.
    if query == None:
        print("TypeError: question() takes exactly minimum 3 arguments (0 given, query=None, answer=None, a=None) \nPlease write code screen: q_answer.help('0 given') \nDon't panic, your code has started successfully.")
        Error = True
    elif answer == None:
        print("TypeError: squestion() takes exactly minimum 3 arguments (1 given, query=", query, ", answer=None, a=None) \nPlease write code screen: q_answer.help('1 given') \nDon't panic, your code has started successfully.")
        Error = True
    elif a == None:
        print("TypeError: question() takes exactly minimum 3 arguments (2 given, query=", query, ", answer=",answer, ", a=None) \nPlease write code screen: q_answer.help('2 given') \nDon't panic, your code has started successfully.")
        Error = True
    elif (answer == "a" or answer == "b" or answer == "c" or answer == "d" or answer == "e") == False:
        print("RestrictionError: The only possible answer value for q_answer.question() is 'a', 'b', 'c', 'd', 'e'. \nPlease write code screen: q_answer.help('answer') \nDon't panic, your code has started successfully.")
        Error = True
    else:
        #Your code doesn't have a problem
        Error = False
    #If Error is True, code'll break (return pass).
    if Error:
        pass
    #If Your code isn't have a problem, the code will run.
    else:
        notanswer = True
        while notanswer:
            print(query)
            print(aname, " ", a)
            if b != None:
                print(bname, " ", b)
                if c != None:
                    print(cname, " ", c)
                    if d != None:
                        print(dname, " ", d)
                        if e != None:
                            print(ename, " ", e)
            user_answer = input("Choose one. \n>")
            notanswer = False
            if user_answer == str(aname):
                return answer == "a"
            elif b != None and (user_answer == bname or user_answer == cname or user_answer == dname or user_answer == ename):
                if user_answer == str(bname):
                    return answer == "b"
                elif c != None:
                    if user_answer == str(cname):
                        return answer == "c"
                    elif d != None:
                        if user_answer == str(dname):
                            return answer == "d"
                        if e != None:
                            if user_answer == str(ename):
                                return answer == "e"
                            else:
                                notanswer = True
                        else:
                            notanswer = True
                    else:
                        notanswer = True
                else:
                    notanswer = True
            else:
                notanswer = True
            if notanswer:
                print("Sorry, there is no such answer.\nPlease, try again")
def help(x = "About"):
    if x == "About":
        print("Welcome to q-answer. This is a Python library.\
\nThis library makes asking questions easier.\
\nWhat does it do?\
\nYou ask a question using the q_answer.question() function;\
\nParameters:\
\nquery = Write your question (e.g., 'How are you'),\
\nanswer = Write the answer (e.g., 'a'),\
\na,b,c,d,e = Write the option (e.g., 'Very Happy')\
\naname,bname,cname,dname,ename = Write the option names here (e.g., 'Apple -->', 'Banana -->')\
\nExample usage:\
\nprint(q_answer.question('Do you like Minecraft?', 'a', 'Yes', 'No'))\
\nTerminal output:\
\nNOTE:\
\np- : print output,\
\ni- : input output.\
\nm- : my answer\
\n\\n : line break\
\n:::\
\np-Do you like Minecraft?\
\np-a Yes\
\np-b No\
\ni-Choose one. \\n>\
\nm-a\
\np-True\
\n\nThank you used this library.\nBY Adalet Ö** B** - Python Programer - Türkiye\
              ")

    if x == "0 given":
        print("It's a error massage. \nSolution to the problem:\
\n1- You are NEVER writing q_answer.question() because you aren't giving any parameter.")
    if x == "1 given":
        print("It's a error massage. \nSolution to the problem:\
\n1- You are NEVER writing q_answer.question('Something') because you are giving only 1 parameter.")
    if x == "2 given":
        print("It's a error massage. \nSolution to the problem:\
\n1- You are NEVER writing q_answer.question('Something', 'Something') because you are giving only 2 parameter.")
    if x == "Answer":
        print("It's a error massage. \nSolution to the problem:\
\n1- You sellect 1 true answer. (Only a, b, c, d, e)")
