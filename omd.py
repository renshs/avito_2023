# Guido van Rossum <guido@python.org>


def get_answer():
    '''
    Function that asks for answer from stdin
    '''
    answer = ''
    while '1' not in answer and '2' not in answer:
        print('Я не понял, повторите ответ, пожалуйста')
        answer = input()
    return answer


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    '''
    Function that is continues branch with umbrella
    '''
    options = {
        'Веруться домой': 1,
        'Идём в бар!': 2,
    }
    print('Конечно взять! Дождь обещали!\n'
          '🦆 прошла всего 5 минут, и тут же начался ливень!!!\n'
          'Хорошо, что зонт под крылом!\n'
          'Но погода ухудшается, порывы ветра начинают вырывать зонт \n'
          'Что же делать?!\n'
          'Выберите: Зонт жалко, пойдём домой! - 1\n'
          'Следующая пятница только через неделю! - 2')
    
    answer = get_answer()

    if answer == '1':
        print('Вот 🦆 и дома! Она обажает смотреть на дождь из окна!\n')
    else:
        print('Как же тяжело удерживать зонт!\n'
              'Ууу-ууу-ууу!\n'
              'Зонт улетел (\n'
              'Но бар стоит на месте, так что выходные не испорчены!')


def step2_no_umbrella():
    '''
    Function that is continues branch without umbrella
    '''
    print('Зонт ни к чему, погода обещает быть замечательной!\n'
          'На небе всего лишь одна малеькая тучка, не стоит  беспокоиться.\n'
          'О нет! Кажется, собирается ливень!\n'
          'Что мы будем делать?!\n'
          'Выберите: Вернуться домой! - 1\n'
          'Продолжить путешествие - 2\n')
    
    answer = get_answer()
    
    if answer == '1':
        print('Ура! 🦆 не промокла )')
    else:
        print('🦆 дошла до бара не промокнув, она же утка!')


if __name__ == '__main__':
    step1()
