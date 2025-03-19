from module1_def import *
print("Ül 1")
#arithmetic funktsiooni kasutamine
while True:
    try:
        a=float(input("Sisesta arv 1:"))
        break
    except:
        print("Arv peab olema kümnendnumber!")
while True:
    try:
        b=float(input("Sisesta arv 2:"))
        break
    except:
        print("Arv peab olema kümnendnumber!")
while True:
    t=input("Tehe: ")
    if t=="+" or t=="-" or t=="*+" or t=="/":
        break
    else:
        print("Sisesta ainult '+' või '-' või '*' või '/'!")
v=arithmetic(a,b,t)
print(v)
 
print("Ül 2")
# is_year_leap funktsiooni kasutamine
while 1:
    try:
        aasta=int(input("Mis aasta tahad kontrollida? "))
        break
    except:
        print("Arv peab olema täisarv!")
if aasta>0: 
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigiaasta")
    else:
        print(f"{aasta} ei ole liigiaasta")

print("Ül 3")
#square funktsiooni kasutamine
while 1:
    try:
        S,P,d=square(float(input("Sisesta külg: ")))
        break
    except:
        print("Arv peab olema kümnendnumber!")
print(f"{S},\n{P},\n{d}\n")

# #square_list funktsiooni kasutamine
# S,P,d=square_list(float(input("Sisesta külg: ")))
# print(f"{S},\n{P},\n{d}\n")

print("Ül 4")
# season funktsiooni kasutamine
while 1:
    try:
        k=int(input("Sisesta kuu number: "))
        break
    except:
        print("Arv peab olema täisarv!")
v=season(k)
print(v)

print("Ül 5")
# bank funktsiooni kasutamine
while 1:
    try:
        years=int(input("Sisesta aasta: "))
        break
    except:
        print("Arv peab olema täisarv!")
while 1:
    try:
        a= int(input('Sisesta raha: '))
        break
    except:
        print("Arv peab olema täisarv!")
while True:
    if years < 0 or a < 0:
        print("Arved positivne! ")
    else:
        vastus = bank(a, years)
        break
 
print("Ül 6")
# is_prime funktsiooni kasutamine
while 1:
    try:
       arv=int(input("Sisesta arv: "))
       break
    except:
        print("Arv peab olema täisarv!")
v=is_prime(arv)
print(v)

print("Ül 7")
# date funktsiooni kasutamine
while 1:
    try:
      päev=int(input("Sisesta päev: "))
      break
    except:
        print("Arv peab olema täisarv!")
while 1:
    try:
       kuu=int(input("Sisesta kuu: "))
       break
    except:
        print("Arv peab olema täisarv!")
while 1:
    try:
       aasta=int(input("Sisesta aasta: "))
       break
    except:
        print("Arv peab olema täisarv!")
v=date(päev, kuu, aasta)
print(v)