from PIL import Image, ImageDraw, ImageFont
import random

# numbers for loop
a = 0
b = 0
c = 0
x = 0
y = 0

# all phrases
words = [
    {
        'text': '"Может\nпойдем?"\n   - Сиди \n    нахуй',
        'font_size': 28,
        'coordinates': [{
            'x': 100,
            'y': 420
        }]
    },
    {
        'text': '  "Мы это\nвырежем"',
        'font_size': 28,
        'coordinates': [{
            'x': 90,
            'y': 460
        }]
    },
    {
        'text': '"Я в туалет,\n   можно?"\n  - Сцы тут',
        'font_size': 24,
        'coordinates': [{
            'x': 93,
            'y': 460
        }]
    },
    {
        'text': 'А можно\n    колу?\n   и лед!',
        'font_size': 28,
        'coordinates': [{
            'x': 100,
            'y': 450
        }]
    },
    {
        'text': 'Воздержа\n    ние от\nчего-либо\n   N-минут\nбез успеха',
        'font_size': 24,
        'coordinates': [{
            'x': 100,
            'y': 420
        }]
    },
    {
        'text': '  Всратая\n  реклама\nАвиасейлз',
        'font_size': 25,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },
    {
        'text': ' Двойничок\n    Смеются\n      только\n2 участника',
        'font_size': 22,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },
    {
        'text': 'Каламбуры\n  на уровне\nсловесного\n    поноса',
        'font_size': 23,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },
    {
        'text': 'Кокешки',
        'font_size': 30,
        'coordinates': [{
            'x': 93,
            'y': 470
        }]
    },
    {
        'text': 'Коллектив\n ное пение\n    в угаре',
        'font_size': 26,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },
    {
        'text': '          Кто-то\n    оговорился\n     и 20 минут\n это разгоняют',
        'font_size': 19,
        'coordinates': [{
            'x': 85,
            'y': 440
        }]
    },
    {
        'text': 'Начало тейбла\nчерез 30 минут\n после начала',
        'font_size': 18,
        'coordinates': [{
            'x': 93,
            'y': 460
        }]
    },
    {
        'text': '  Отслыки\n к другому\n    тейблу',
        'font_size': 28,
        'coordinates': [{
            'x': 84,
            'y': 440
        }]
    },
    {
        'text': '    Очень\nнеловкая\n    пауза',
        'font_size': 28,
        'coordinates': [{
            'x': 94,
            'y': 435
        }]
    },
    {
        'text': '  Попытка\nобъяснить\n    смысл\n   тейбла',
        'font_size': 26,
        'coordinates': [{
            'x': 93,
            'y': 430
        }]
    },
    {
        'text': '     Разгон\nзвуков или\nотдельных\n     слогов',
        'font_size': 24,
        'coordinates': [{
            'x': 93,
            'y': 435
        }]
    },
    {
        'text': 'Отсылка к\nСамохуну',
        'font_size': 27,
        'coordinates': [{
            'x': 90,
            'y': 455
        }]
    },
    {
        'text': '       Тема\n"Предметы\n     в жопе"',
        'font_size': 25,
        'coordinates': [{
            'x': 90,
            'y': 445
        }]
    },
    {
        'text': '          Шутка\n   "ну мы еще\nразгоны сюда\n    приносить\n       должны?"',
        'font_size': 20,
        'coordinates': [{
            'x': 88,
            'y': 430
        }]
    },
    {
        'text': '          Шутка\n"ты вырыл яму\n          и я-мы\n       нырнули"',
        'font_size': 20,
        'coordinates': [{
            'x': 84,
            'y': 440
        }]
    },
    {
        'text': '    Шутка\n"У нас тут\n  6 камер"',
        'font_size': 26,
        'coordinates': [{
            'x': 93,
            'y': 445
        }]
    },
    {
        'text': '      Шутка\n"Я лучше на\nвойну поеду"',
        'font_size': 21,
        'coordinates': [{
            'x': 93,
            'y': 450
        }]
    },
    {
        'text': '         Шутка\n     "Я лучше\nобратно в РФ"',
        'font_size': 19,
        'coordinates': [{
            'x': 90,
            'y': 455
        }]
    },
    {
        'text': '   Шутка\nв тишину',
        'font_size': 26,
        'coordinates': [{
            'x': 100,
            'y': 455
        }]
    },
    {
        'text': ' Шутка\nпро вес\n   Ильи',
        'font_size': 26,
        'coordinates': [{
            'x': 115,
            'y': 445
        }]
    }
]

# generate random number
num = random.randint(1, 3)

# open random image
image = Image.open(f"background/{num}.png")

# creating a filter list
indices = []

# cell filling
while a < 25:
    # generate index
    i = random.randint(0, len(words) - 1)

    # adding text to cells
    if i not in indices:
        a += 1

        # loop
        if a == 1:
            x = words[i]['coordinates'][0]['x']
            y = words[i]['coordinates'][0]['y']
        elif a in [2, 3, 4, 5]:
            b += 196
            x = words[i]['coordinates'][0]['x'] + b
            y = words[i]['coordinates'][0]['y']
        elif a == 6:
            c += 165
            b = 0
            x = words[i]['coordinates'][0]['x']
            y = words[i]['coordinates'][0]['y'] + c
        elif a in [7, 8, 9, 10]:
            b += 196
            x = words[i]['coordinates'][0]['x'] + b
            y = words[i]['coordinates'][0]['y'] + c
        elif a == 11:
            c += 185
            b = 0
            x = words[i]['coordinates'][0]['x']
            y = words[i]['coordinates'][0]['y'] + c
        elif a in [12, 13, 14, 15]:
            b += 196
            x = words[i]['coordinates'][0]['x'] + b
            y = words[i]['coordinates'][0]['y'] + c
        elif a == 16:
            c += 175
            b = 0
            x = words[i]['coordinates'][0]['x']
            y = words[i]['coordinates'][0]['y'] + c
        elif a in [17, 18, 19, 20]:
            b += 196
            x = words[i]['coordinates'][0]['x'] + b
            y = words[i]['coordinates'][0]['y'] + c
        elif a == 21:
            c += 175
            b = 0
            x = words[i]['coordinates'][0]['x']
            y = words[i]['coordinates'][0]['y'] + c
        elif a in [22, 23, 24, 25]:
            b += 196
            x = words[i]['coordinates'][0]['x'] + b
            y = words[i]['coordinates'][0]['y'] + c

        # select font
        font = ImageFont.truetype('font/Unbounded-Regular.ttf', words[i]['font_size'])

        # font color selection
        if num == 3:
            fill = 'black'
        else:
            fill = 'white'

        # adding text to the background
        drawer = ImageDraw.Draw(image)
        drawer.text((x, y), words[i]['text'], font=font, fill=fill)

        # adding an index to a list
        indices.append(i)

    # clear list
    if a == 25:
        indices.clear()

# save image
image.save(f'img/{a}.png')
image.show()