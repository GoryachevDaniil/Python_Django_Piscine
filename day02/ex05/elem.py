#!/usr/bin/python3

class Text(str):
    def __str__(self):
        result = super().__str__().replace('"', '&quot;')
        result = result.replace('<', '&lt;')
        result = result.replace('>', '&gt;')
        return result.replace('\n', '\n<br />\n')

class Elem:
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        self.tag_type = tag_type
        if content != None:
            self.add_content(content)
        else:
            self.add_content(Text(''))

    def __str__(self):
        if self.tag_type == 'double':
            result = f'<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>'
        elif self.tag_type == 'simple':
            result = f'<{self.tag}{self.__make_attr()}/>'
        return result

    def __make_attr(self):
        result = ''
        for elem in sorted(self.attr.items()):
            result += ' ' + str(elem[0]) + '="' + str(elem[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            for el in str(elem).split('\n'):
                result += f'  {el}\n'

        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    class ValidationError(Exception):
        pass

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

if __name__ == '__main__':
    title = Elem(tag='title', content=Text('"Hello ground!"'), tag_type='double')
    head = Elem(tag='head', content=title, tag_type='double')
    h1 = Elem(tag='h1', content=Text('"Oh no, not again!"'), tag_type='double')
    img = Elem(tag='img', attr={'src': "http://i.imgur.com/pfp3T.jpg"}, tag_type='simple')
    body = Elem(tag='body', content=[h1, img], tag_type='double')
    html = Elem(tag='html', content=[head, body], tag_type='double')
    print(html)