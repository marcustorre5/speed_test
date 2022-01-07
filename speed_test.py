import speedtest
from time import sleep

def speed_test():
    print('Gerando resultados, espere ....')
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    speed.results.share()

    results_dict = speed.results.dict()

    print(results_dict)

speed_test()

def quest():
    q = str(input('\n repetir teste: s/n ?'))
    if q == 's':
        speed_test()
        quest()
    if q == 'n':
        print('sair')
        sleep(1)
        sair()

quest()

def sair():
    print('sair')
sair()
