import re
from itertools import zip_longest

# TODO: clean the code up and rename everything


def sharkdownparser(text):

    s = text

    # SET 1

    sa = []

    def sentences(s):
        s = re.split('\\n', s)
        return s

    def tokenize_1(sentences):
        tokens = re.split('(#\s|\\n##\s|\\n###\s|\\n####\s|\\n-\s)', sentences)
        return tokens

    def tokenize_2(arr):
        tokens = []
        for item in arr:
            tokens.append([item[0], re.split('\\n', item[1])])
        return tokens

    def pack_singles(tokens):
        tokens = zip(tokens[1::2], tokens[2::2])
        return tokens

    def convert_singles(tokens):
        sb = []
        s = []
        for code, text in tokens:
            if code == '# ':
                sb.append('<h1>')
                sb.append(text[0])
                sb.append('</h1>')
                for item in text[1:]:
                    sb.append(item)
            elif code == "\n## ":
                sb.append('<h2>')
                sb.append(text[0])
                sb.append('</h2>')
                for item in text[1:]:
                    sb.append(item)
            elif code == "\n### ":
                sb.append('<h3>')
                sb.append(text[0])
                sb.append('</h3>')
                for item in text[1:]:
                    sb.append(item)
            elif code == "\n#### ":
                sb.append('<h4>')
                sb.append(text[0])
                sb.append('</h4>')
                for item in text[1:]:
                    sb.append(item)
            elif code == "\n- ":
                sb.append('<ul><li>')
                sb.append(text[0])
                sb.append('</li></ul>')
                for item in text[1:]:
                    sb.append(item)
            else:
                sb.append(code)
                if text[1] != '':
                    for item in text[1:]:
                        sb.append(item)
            s.append(''.join(sb))
            sb = []
        return s

    def replace_newlines(s):
        return s.replace("\n", "<BR>")

    b = tokenize_1(s)
    b = pack_singles(b)
    b = tokenize_2(b)
    b = convert_singles(b)
    b = ''.join(b)

    # SET 2

    def tokenize(s):
        tokens = s
        tokens = re.split('(\*\*|_)', tokens)
        return tokens

    def pack_code(tokens):
        tokens = zip(tokens[1::4], tokens[2::4], tokens[3::4])
        return tokens

    def pack_text(tokens):
        tokens = tokens[0::4]
        return tokens

    def convert_enclosed(tokens):
        sb = []
        s = []
        for a, b, c in tokens:
            if a == '**' and c == '**':
                sb.append('<b>')
                sb.append(b)
                sb.append('</b>')
            elif a == '_' and c == '_':
                sb.append('<i>')
                sb.append(b)
                sb.append('</i>')
            elif a == '```' and c == '```':
                sb.append('<i>')
                sb.append(b)
                sb.append('</i>')
            else:
                sb.append(a)
                sb.append(b)
                sb.append(c)
            s.append(''.join(sb))
            sb = []
        return s

    def clean_list(arr):
        arr2 = []
        for index, item in enumerate(arr):
            if type(item[1]) == type(None):
                arr2.append([item[0], ''])
            else:
                arr2.append(item)
        return arr2

    tokens = tokenize(b)

    code = pack_code(tokens)

    text = pack_text(tokens)

    sb = convert_enclosed(code)

    sb = zip_longest(text, sb)

    sb = clean_list(sb)

    result = []

    for item in sb:
        result.append(' '.join(item))

    result = ' '.join(result)

    return result
