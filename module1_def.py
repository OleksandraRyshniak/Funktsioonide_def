#1


def arithmetic(arv1:float, arv2:float, tehe:str)->any:
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: Sisend kasutajalt, mingi ujukomaarv
    :param float arv2: Sisend kasutajalt, mingi ujukomaarv
    :param str tehe: aritmeetilibe tehe, mis valib kasutaja
    :rtype: var Määrata tüüp(float või str)
    """
    if tehe in ["+", "-", "*", "/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else: 
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus
#2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False Kui on tavaline aasta.
    :param int aasta : aasta number
    :rtype:bool tagastab tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(külg: float) -> any:
    """Square
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    :param float külg: Sisend kasutajalt, mingi ujukomaarv
    :rtype: var märgib tüüpi str
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    return S,P,d

def square_list(külg: float) -> list:
    """Square
    s_list=[S,P,d] where 
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    :param float külg: Sisend kasutajalt, mingi ujukomaarv
    :rtype: var märgib tüüpi str
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    s_list=[S,P,d]
    return S,P,d

#4 
def season(kuu_number:int) -> str:
    """Aastaajad
    Hooaja tagastamine (talv, kevad, suvi või sügis).
    :param int kuu_number : Sisend kasutajalt
    :rtype: var märgib tüüpi str
    """
    if kuu_number==1 or 2 or 12:
       kuu="talv"
    elif kuu_number==3 or 4 or 5:
       kuu="kevad"
    elif kuu_number==6 or 7 or 8:
       kuu2="suvi"
    else:
       kuu3="sügis"
    return kuu


def seasonInput()->str:
    """Aastaaja leidmine
    Tagastab aastaaja nine
    :rtype str tagastab aastaja nine
    """
    k=int(input("Sisesta kuu number: "))
    while True:
        if k in range(1,13):
            break
        else:
            k=int(input("Sisesta kuu number: "))
    return season(k)

#5
def bank(aeur:float, years:int)->float:
    """ Panga Deposiit
    Tagastab summa, mis on kasutaja kontol.
    :param float aeur, Sisend kasutajalt
    :param int years, Sisend kasutajalt
    :rtype float 
    """
    for i in range(years):
        aeur=aeur*1,10
    return aeur

#6
def is_prime(arv:int)->bool:
    """ Primaarvud 
    Tagastab True, kui see on lihtne, ja False, kui see ei ole.
    :param int arv, Sisend kasutajalt
    :rtype bool tagastab tõeväärsuses formaadis tulemus
    """
    if 0<=arv<1001:
        if arv in [0,1]:
            pass
        else:
            for i in range (2, arv):
                    if arv%i==0:
                        return False
                    else:
                        return True

#7
def date(päev:int, kuu:int, aasta:int) -> bool:
    """
    """


