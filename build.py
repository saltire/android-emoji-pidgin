import os
import re
from xml.etree import ElementTree as etree


themedir = './android-emoji-theme'

# Exclude modifier symbols.
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
    ['1F3FB'],
    ['1F3FC'],
    ['1F3FD'],
    ['1F3FE'],
    ['1F3FF']
]

def filename_to_sequence(filename):
    m = re.match(r'emoji_u(\w+)\.png', filename)
    if m:
        return m.group(1).upper().split('_')


def sequence_to_text(sequence):
    return ''.join([chr(int(code, 16)) for code in sequence])


def theme_line(filename, sequence, name=''):
    return '{}\t{}{}\n'.format(filename,
        ':{}:\t'.format(name.replace(' ', '_')) if name else '',
        sequence_to_text(sequence))


emojis = []
filenames = []
names = {}

print('Reading Unicode emoji list')
with open('./emoji-ordering.txt', 'r', encoding='utf-8') as textfile:
    for line in textfile.readlines():
        m = re.match(r'((?:U\+[A-F\d]+ )+); ([\d.]+) # (\S+) (.+)$', line)
        if m:
            sequence = [code[2:] for code in m.group(1).lower().strip().split(' ')]
            filename = 'emoji_u{}.png'.format('_'.join(sequence))

            emojis.append({
                'sequence': sequence,
                'version': m.group(2),
                'chars': m.group(3),
                'name': m.group(4),
                'filename': filename,
            })
            filenames.append(filename)

print('Read', len(emojis), 'emojis.')


images = []
for imgfile in os.listdir(themedir):
    m = re.match(r'emoji_u(\w+)\.png', imgfile)
    if m:
        sequence = m.group(1).upper().split('_')
        if sequence not in exclude:
            images.append(imgfile)


# Build Pidgin smiley theme.
with open(os.path.join(themedir, 'theme'), 'w', encoding='utf-8', newline='') as newtheme:
    newtheme.write(
        'Name=Android Emoji Theme\n'
        'Description=Emoji from Google\'s Noto font\n'
        'Icon=emoji_u1f601.png\n'
        'Author=saltire sable\n\n'
        '[default]\n'
        )

    total = 0
    for emoji in emojis:
        if emoji['sequence'] in exclude:
            print('Skipping image:', emoji['filename'], emoji['name'])
        if emoji['filename'] in images:
            newtheme.write(theme_line(emoji['filename'], emoji['sequence'], emoji['name']))
            total += 1
            print('Added image:', emoji['filename'], emoji['name'].encode('utf-8'))
        else:
            print('Image not found:', emoji['filename'], emoji['name'].encode('utf-8'))

    for imgfile in sorted(images):
        if imgfile not in filenames:
            sequence = filename_to_sequence(imgfile)
            if sequence in exclude:
                print('Skipping image:', imgfile)
            else:
                newtheme.write(theme_line(imgfile, sequence))
                total += 1
                print('Found and added extra image:', imgfile)

    print('Added', total, 'emojis to Pidgin theme.')


# Build Adium emoticon theme.
plist = etree.Element('plist', {'version': '1.0'})
dict1 = etree.SubElement(plist, 'dict')
etree.SubElement(dict1, 'key').text = 'AdiumSetVersion'
etree.SubElement(dict1, 'integer').text = '1'
etree.SubElement(dict1, 'key').text = 'Emoticons'
dict2 = etree.SubElement(dict1, 'dict')

def create_element(dict_elem, filename, sequence, name):
    etree.SubElement(dict_elem, 'key').text = filename
    dict3 = etree.SubElement(dict_elem, 'dict')
    etree.SubElement(dict3, 'key').text = 'Equivalents'
    array = etree.SubElement(dict3, 'array')
    etree.SubElement(array, 'string').text = sequence_to_text(sequence)
    etree.SubElement(dict3, 'key').text = 'Name'
    etree.SubElement(dict3, 'string').text = name

total = 0
for emoji in emojis:
    if emoji['sequence'] in exclude:
        print('Skipping image:', emoji['filename'], emoji['name'])
    if emoji['filename'] in images:
        create_element(dict2, emoji['filename'], emoji['sequence'], emoji['name'])
        total += 1
        print('Added image:', emoji['filename'], emoji['name'].encode('utf-8'))
    else:
        print('Image not found:', emoji['filename'], emoji['name'].encode('utf-8'))

for imgfile in images:
    if imgfile not in filenames:
        sequence = filename_to_sequence(imgfile)
        if sequence in exclude:
            print('Skipping image:', imgfile)
        else:
            create_element(dict2, imgfile, sequence, '***' + imgfile)
            total += 1
            print('Found and added extra image:', imgfile)

print('Added', total, 'emojis to Adium theme.')

etree.ElementTree(plist).write(os.path.join(themedir, 'Emoticons.plist'),
    encoding='utf-8', xml_declaration=True)
