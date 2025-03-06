correct_ans=0
wrong_ans=0
negative_mark=0
def history():
    global correct_ans,wrong_ans,negative_mark#to ensure we are using global variable
    que=['What is the capital of india?:',
         'What is the capital of karnataka?:',
         'What is the capital of kerala?:',
         'What is the capital of Tamil Nadu?:',
         'What is the capital of Telangana',
         'What is the capital of Madhya Pradesh',
         'What is the capital of Maharashtra',
         'What is the capital of Assam',
         'What is the capital of Bihar',
         'What is the capital of Goa',
         ]
    ans=['delhi',
         'bengaluru',
         'thiruvananthapuram',
         'chennai',
         'hyderabad',
         'bhopal',
         'mumbai',
         'dispur',
         'patna',
         'panaji',
         ]
    for x in range(len(que)):
        print(que[x])
        user_inp=input('Enter your answer:').lower()
        if user_inp==ans[x]:
            print('correct')
            correct_ans=correct_ans+1
        else:
            print('wrong')
            wrong_ans=wrong_ans+1
            negative_mark+=1
            if negative_mark==4:
                print('1 Negative Mark Deducted')
                correct_ans-=1
                negative_mark=0
            else:
                continue
    calculate()
def python():
    global correct_ans,wrong_ans,negative_mark #to ensure we are using global variable
    que=['What is the correct way to declare a variable in Python?:',
         'What is the output of print(3 + 2 * 2) in Python?:',
         'What is used for comments in Python?:',
         'What is not a data type in Python?:',
         'What is the output of print(type("Hello"))?',
         'What is used to concatenate two strings in Python?',
         'What is the result of 3 == 3 in Python?',
         'What is used to check the data type of a variable in Python?',
         'How do you make a string lowercase in Python?',
         'How do you convert a string to an integer in Python?',
         ]
    ans=['x=10',
         '7',
         '#',
         'char',
         '<class str>',
         '+',
         'true',
         'type()',
         'string.lower()',
         'int(string)',
        ]
    for x in range(len(que)):
        print(que[x])
        user_inp=input('Enter your answer:').lower()
        if user_inp==ans[x]:
            print('correct')
            correct_ans=correct_ans+1
        else:
            print('wrong')
            wrong_ans=wrong_ans+1
            negative_mark+=1
            if negative_mark==4:
                print('1 Negative Mark Deducted')
                correct_ans-=1
                negative_mark=0
            else:
                continue
    calculate()
def sql():
    global correct_ans,wrong_ans,negative_mark #to ensure we are using global variable
    que=['What command is used to create a new table in SQL?:',
         'What does BLOB in SQL stand for?:',
         'What is most appropriate for storing a string of up to 255 characters?:',
         'What happens when no value is inserted in an ENUM list?:',
         'When is the wildcard in WHERE clause used?',
         'Which of the following is the full form of DDL?',
         'Which SQL constraint do we use to set some value to a field whose value has not been added explicitly?',
         'What are rows of a relation known as?',
         'Group of operations that form a single logical unit of work called?',
         'How can we view all the triggers currently in the database?',
         ]
    ans=['create table',
         'binary large objects',
         'tiny text',
         'a blank value is inserted in the list',
         'an exact match is not possible in a select statement.',
         'data defenition language',
         'default',
         'tuple',
         'transaction',
         'show',
         ]
    for x in range(len(que)):
        print(que[x])
        user_inp=input('Enter your answer:').lower()
        if user_inp==ans[x]:
            print('correct')
            correct_ans=correct_ans+1
        else:
            print('wrong')
            wrong_ans=wrong_ans+1
            negative_mark+=1
            if negative_mark==4:
                print('1 Negative Mark Deducted')
                correct_ans-=1
                negative_mark=0
            else:
                continue
    calculate()
def ext():
    pass
def calculate():
    print(f'Correct Anwsers:{correct_ans}')
    print(f'Wrong Anwsers:{wrong_ans}')
    if correct_ans+wrong_ans>0:
        print(f'Percentage{(correct_ans/(correct_ans+wrong_ans))*100}%')
    else:
        print('No anwsers attempted')

class QuizApp:
    def category(self):
        print('Select the category on which you want to take the quiz')
        while True:
            print('1.History')
            print('2.Python')
            print('3.SQL')
            user_in=int(input('Enter Your Choice:'))
            if user_in==1:
                history()
                break
            elif user_in==2:
                python()
                break
            elif user_in==3:
                sql()
                break
            else:
                ext()
                break
q = QuizApp()
q.category()






