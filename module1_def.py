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