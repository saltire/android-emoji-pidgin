import os
import re

from bs4 import BeautifulSoup
import requests


themedir = './android-emoji-theme'

exclude = [
    ['0023'],
    ['0030'],
    ['0031'],
    ['0032'],
    ['0033'],
    ['0034'],
    ['0035'],
    ['0036'],
    ['0037'],
    ['0038'],
    ['0039'],
    ['00A9'],
    ['00AE'],
]


def filename_to_sequence(filename):
    m = re.match('emoji_u(\w+)\.png', filename)
    if m:
        return m.group(1).upper().split('_')


emojis = []
print('Reading Unicode 8 list')
with open('./emoji-unicode8.txt', 'r', encoding='utf-8') as unicode8:
    for line in unicode8.readlines():
        m = re.match('((?:U\+[A-F\d]+ )+)(\S+) (.+)$', line)
        if m:
            emojis.append({
                'sequence': [code[2:] for code in m.group(1).lower().strip().split(' ')],
                'chars': m.group(2),
                'name': m.group(3),
            })
print('Read', len(emojis), 'emojis.')


with open(os.path.join(themedir, 'theme2'), 'w', encoding='utf-8', newline='') as newtheme:
    newtheme.write(
        'Name=Android Emoji Theme\n'
        'Description=Emoji from Google\'s Noto font\n'
        'Icon=emoji_u1f601.png\n'
        'Author=saltire sable\n\n'
        '[default]\n'
        )

    filenames = []
    names = {}
    for emoji in emojis:
        filename = 'emoji_u{}.png'.format('_'.join(emoji['sequence']))
        filenames.append(filename)
        names[filename] = emoji['name']

    total = 0
    # find all existing image files and add them to the theme, if they are in the text file
    for imgfile in os.listdir(themedir):
        m = re.match('emoji_u(\w+)\.png', filename)
        sequence = m.group(1).upper().split('_')

        if sequence and sequence not in exclude:
            newtheme.write('{}\t{}\n'.format(imgfile, ''.join([chr(int(code, 16)) for code in sequence])))

            if imgfile in filenames:
                print('Added image:', imgfile, names[imgfile])
                total += 1
            else:
                print('Extra image found:', imgfile)

    # mention all emojis in the text file that do not have a matching image
    for filename in filenames:
        if not os.path.exists(os.path.join(themedir, filename)):
            print('Image not found:', filename, names[filename].encode('utf-8'))

    print('Added', total, 'emojis to theme.')
