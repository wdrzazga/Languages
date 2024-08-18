def greet(name, lan):
    greeting = {'PL': f'Cześć {name}!',
                'EN': f'Hello {name}!',
                'ES': f'¡Hola {name}!',
                'RU': f'Привет {name}!'}
    print (greeting[lan])
age_question = {'PL': 'Jak się nazywasz?: ',
                'EN': "What's your name?: ",
                'ES': '¿Cómo te llamas?: ',
                'RU': 'Как тебя зовут?: '}
