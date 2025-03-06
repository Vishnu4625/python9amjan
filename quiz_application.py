correct_ans=0
wrong_ans=0
# ***********************************
# normal code                       *
# ***********************************
# q=input('What is the capital of india?:').lower()
# if q=='delhi':
#     print('Correct Answer')
#     correct_ans=correct_ans+1
# else:
#     print('Wrong Answer')
#     wrong_ans=wrong_ans+1
# q=input('What is the capital of karnataka?:').lower()
# if q=='blr':
#     print('Correct Answer')
#     correct_ans=correct_ans+1
# else:
#     print('Wrong Answer')
#     wrong_ans=wrong_ans+1
# print(f'Correct{correct_ans}marks')
# print(f'Wrong{wrong_ans}marks')
# print('Percentage',(correct_ans/(correct_ans+wrong_ans))*100)
# ***********************************
# decreasing line of codes with bug *
# ***********************************
# q=['What is the capital of india?:','What is the capital of karnataka?:']
# ans=['delhi','blr']
# for x in q:
#     print(x)
#     user_inp=input('Enter your answer:')
#     if user_inp in ans:
#         print('correct')
#         correct_ans+=1
#     else:
#         print('wrong')
#         wrong_ans+=1
# print(f'Correct Anwsers:{correct_ans}')
# print(f'Wrong Anwsers:{wrong_ans}')
# print('Percentage',(correct_ans/(correct_ans+wrong_ans))*100)
# ***********************************
# decreasing line of codes without bug *
# *********************************** 
q=['What is the capital of india?:','What is the capital of karnataka?:']
ans=['delhi','blr']
for x in range(len(q)):#to remove bug changes done here
    print(q[x])#to remove bug changes done here
    user_inp=input('Enter your answer:')
    if user_inp in ans[x]:#to remove bug changes done here
        print('correct')
        correct_ans+=1
    else:
        print('wrong')
        wrong_ans+=1
print(f'Correct Anwsers:{correct_ans}')
print(f'Wrong Anwsers:{wrong_ans}')
print('Percentage',(correct_ans/(correct_ans+wrong_ans))*100)