import re


def display_menu(options):
    x = 0
    for option in options:
        print(f'{x + 1}. {option}')
        x += 1


latin_to_cyrillic_dict = {
    'a': 'а',
    'b': 'б',
    'c': 'ц',
    'd': 'д',
    'e': 'э',
    'f': 'ф',
    'g': 'г',
    'h': 'х',
    'i': 'и',
    'j': 'й',
    'k': 'к',
    'l': 'л',
    'm': 'м',
    'n': 'н',
    'o': 'о',
    'p': 'п',
    'q': 'қ',
    'r': 'р',
    's': 'с',
    't': 'т',
    'u': 'у',
    'v': 'в',
    'w': 'в',
    'y': 'ы',
    'z': 'з',
    'ż': 'ж',
    'A': 'А',
    'B': 'Б',
    'C': 'Ц',
    'D': 'Д',
    'E': 'Э',
    'F': 'Ф',
    'G': 'Г',
    'H': 'Х',
    'I': 'И',
    'J': 'Й',
    'K': 'К',
    'L': 'Л',
    'M': 'М',
    'N': 'Н',
    'O': 'О',
    'P': 'П',
    'Q': 'Қ',
    'R': 'Р',
    'S': 'С',
    'T': 'Т',
    'U': 'У',
    'V': 'В',
    'W': 'В',
    'X': 'Кс',
    'Y': 'Ы',
    'Z': 'З',
    'Ż': 'Ж'
}


def latin_to_cyrillic(text):
    def replace_match(match):
        char = match.group(0)
        return latin_to_cyrillic_dict.get(char, char)

    pattern = re.compile('|'.join(re.escape(key) for key in latin_to_cyrillic_dict.keys()))
    return pattern.sub(replace_match, text)
