#문제1
name=input("이름을 입력하세요")
age=input("나이를 입력하세요")
email=input("이메일 주소를 입력하세요")

dic={name:[age,email]}

print(dic)

#문제2
exchage={'달러':1320,'엔화':950,'위안':182}
chul=[13,200,13]
total = exchage['달러']*chul[0]+exchage['엔화']*chul[1]
print('가지고 계신 돈은  ',total,  '원 입니다')
