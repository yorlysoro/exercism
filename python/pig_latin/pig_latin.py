def translate(text):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    qu = 'qu'
    xr = 'xr'
    yt = 'yt'
    new_text = ''
    words = text.split(' ')
    for word in words:
        index_qu = word.find(qu)
        if index_qu > 0 and word[0] not in vowels:
            count = 0
            for i in word:
                if i in consonants or i == 'u':
                    count += 1
                else:
                    break
            word = word[count:] + word[0:count] + 'ay'
        elif word.startswith(yt) or word.startswith(xr) or word[0] in vowels:
            word += 'ay'
        else:
            count = 0
            for i in word:
                if i in consonants and i != 'y':
                    count += 1
                else:
                    break
            if word[0] == 'y':
                word = word[1:] + word[0] + 'ay'
            else:
                word = word[count:] + word[0:count] + 'ay'
        new_text += ' '+word if new_text != '' else word
    return new_text