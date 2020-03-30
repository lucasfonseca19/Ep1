'''Sorteio e soma'''
import random
dado1=[1,2,3,4,5,6]
dado2=[1,2,3,4,5,6]
fichas=100
n=1
'''função apostar ou não(não terminei)'''
def apostar():
    resp=input("\nvocê gostaria de apostar nessa rodada ou sair do jogo?\nDigite'apostar'ou'sair'\n")
    if (resp =='apostar'):
        return True
    else:
        return False
'''função para cada tipo de jogo'''
def sorteio():
    x=random.choice(dado1)
    y=random.choice(dado2)
    resultado=x+y
    return resultado
def plb():
    global fichas
    aposta=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
    z=sorteio()
    print(z)
    if(z== 7 or z== 11):
        fichas=fichas+aposta 
        print(fichas)
    elif(z== 2 or z== 3 or z== 12):
        fichas=fichas-aposta
        print(fichas)
    elif(z== 4 or z== 5 or z== 6 or z== 8 or z== 9 or z== 10):
        def loop_point():
            w=sorteio()
            global n
            global fichas
            print("Agora você se encontra na fase point pela {}° vez\n".format(n))
            print("O valor {} retirado no priemiro sorteio é seu point".format(z))
            print("O novo valor sorteado é",w)
            n=n+1
            if(w==z):
                fichas=fichas+aposta
                print(fichas)
                return True
            elif(w==7):
                fichas=0
                print("você perdeu tudo!!!")
                return True
            else:
                return False
        while(loop_point()!=True):
            loop_point() 
def field():
    global fichas
    aposta=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
    z=sorteio()
    print(z)
    if(z==5 or z==6 or z==7 or z==8):
        print('Você perdeu tudo !!!')
    elif(z==3 or z==4 or z==9 or z==10 or z==11):
        fichas=fichas
        print(fichas)
    elif(z==2):
        fichas=fichas+2*aposta
        print(fichas)
    else:
        fichas=fichas+3*aposta
        print(fichas)
def anycraps():
    global fichas
    aposta=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
    z=sorteio()
    print(z)
    if(z==2 or z==3 or z==12):
        fichas=fichas+7*aposta
        print(fichas)
    else:
        fichas=fichas-aposta
        print(fichas)
def twelve():
    global fichas
    aposta=int(input("Quantas fichas gostaria de jogar? lembrando que você só pode jogar um número inteiro de fichas"))
    z=sorteio()
    print(z)
    if(z==12):
        fichas=fichas+30*aposta
        print(fichas)
    else:
            fichas=fichas-aposta
            print(fichas)
'''função apostas(não terminei)'''
def apostas():
    tipos=[]
    while True:
        tipo=input("Quais tipos de aposta você gostaria de fazer?\n Digite 'plb' e/ou 'field' e/ou'anycraps' e/ou'twelve' separado por virgulas\nQuando terminar de escolher digite 'acabei' ")
        if (tipo =='acabei'):
            break
        tipos.append(tipo)
    for word in tipos:
        if 'plb' in tipos:
            print("PlB:\n")
            plb()
            continue
        elif 'field'in tipos:
            print("FIELD:\n")
            field()
            continue
        elif 'anycraps' in tipos:
            print("ANYCRAPS:\n")
            anycraps()
            continue
        elif 'twelve'in tipos:
            print("TWELVE:\n")
            twelve()
            break



print("\nBem vindo ao Craps Insper, você esta na fase 'Come Out' e inicia com 100 fichas \n")

if (apostar()==True):
    while(fichas>0):
        apostas()
else:
    print("até mais")
