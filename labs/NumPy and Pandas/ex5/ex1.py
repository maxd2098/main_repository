mul = open('mul_table.html', 'w')
print('''<!DOCTYPE HTML>
          <html> 
          <head>
          <title>Умножение</title>
          </head>
          <body>
          <table>
          ''', file=mul)

for i in range(1, 11):
    print('''<tr>''', file=mul)
    for j in range(1, 11):    
        print(f'''<td> <a href=http://{i*j}.ru>{i*j}</a> </td>''', file=mul)
    print('''</tr>''', file=mul)
print('''</table>
          </body>
          </html>''', file=mul)
mul.close()


