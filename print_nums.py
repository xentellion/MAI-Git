import random
phrases = ['ВАУ ОНИ ТАКИЕ КРУТЫЕ!\n', 'КОГДА НА КИКСТАРТЕР??\n', 'ЗАБЕРИТЕ МОИ ДЕНЬГИ!!\n', 'Я ХОЧУ ВИДЕТЬ ЭТО НА СВОЕМ УСТРОЙСТВЕ\n', 'ДУМАЮ ЭТО РЕШИТ ВСЕ МОИ ПРОБЛЕМЫ\n', 'ЭТОТ ДЕНЬ ВОЙДЕТ В ИСТОРИЮ\n', 'ДААААА\n', 'МЫ ЛЮБИМ ВАС!!\n', 'бабубэ)\n']


def f():
    for i in range(1, 11):
        print(i)


if __name__ == '__main__':
    print('РЕБЯТА ПОД ВАШИ АПЛОДИСМЕНТЫ, ПРЕДСТАВЛЯЕМ ВАШЕМУ ВНИМАНИЮ ЧИСЛА!!! ООООООТ!! ОДНОГО ДОООО ДЕСЯТИ!!!')
    f()
    print(random.choice(phrases))

