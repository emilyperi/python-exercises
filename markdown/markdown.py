import re


def replace_header_tag(single_line):
    header = "<h{n}>{line}</h{n}>"
    switcher = {
            6: '#{6}(.*)'
            5: '#{5}(.*)'
            4: '#{4}(.*)'
            3: '#{3}(.*)'
            2: '#{2}(.*)'
            1: '#{1}(.*)'
    }

    for n, pattern in switcher.items():
        if re.match(pattern, single_line):
            return header.format(n, single_line[n+1:], n)

def parse(markdown):
    """
    Convert markdown syntax to html syntax
    
    :param markdown: string representing markdown file
    :return: string representing html file derived from markdown
    """

    # split markdown string at each new line  
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    
    # replace hashtags with html header tags
    for line in lines:
        line = replace_header_tag(line)
        m = re.match(r'\* (.*)', line)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res
