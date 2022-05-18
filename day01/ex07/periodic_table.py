import sys
def make_html(my_dict):
    my_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>MyGenerate</title>
        <style>
        table { 
         width: 10%; /* Ширина таблицы */
         border: 4px solid black; /* Рамка вокруг таблицы */
         border-collapse: collapse; /* Отображать только одинарные линии */
        }
        th { 
         padding: 5px; /* Поля вокруг содержимого ячеек */
         border: 1px solid black; /* Граница вокруг ячеек */
        }
        td { 
         padding: 5px; /* Поля вокруг содержимого ячеек */
         border: 1px solid black; /* Граница вокруг ячеек */
        }
    </style>
    </head>
    <body>
    <table><tr>'''
    position = 0
    for key, value in my_dict.items():
        empty = 0
        if int(value[0]) < position:
            my_html += '</tr><tr>'
            position = int(value[0])
        if int(value[0]) > position:
            empty = int(value[0]) - position - 1
            position = int(value[0])
        for _ in range(empty):
            my_html += '<td style="border: 1px solid black; padding: 10px"></td>'
        my_html += f'''
        <td style="border: 1px solid black; padding: 10px">
            <h4>{key}</h4>
            <ul>
                <li>No {value[1]}</li>
                <li>{value[2]}</li>
                <li>{value[3]}</li>
                <li>{value[4]} electron</li>
            </ul>
        </td>'''
    my_html += '''</tr>
    </table>
    </body>'''
    return my_html

def periodic_table():
    my_dict = {}
    for line in open('periodic_table.txt', 'r').readlines():
        element, character = line.split('=')
        my_dict[element] = [line.split(':', 1)[1] for line in map(str.strip, character.split(','))]
    my_html = open('periodic_table.html', 'w')
    my_html.write(make_html(my_dict))

if __name__ == '__main__':
    periodic_table()