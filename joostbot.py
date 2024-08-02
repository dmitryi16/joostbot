evropa = ['европапа']
noevropa = ['хз']
i = 0
w = False
print('Привет, мир! это joostbot \nкоманды: list, nolist')
while True:
    a = (input('введите слово: '))
    b = [a]
    if a == "list":
        for str in evropa:
            print(f"{i}. {str}")
            i += 1
        i = 0
        continue
    if  a == 'nolist':
        for str in noevropa:
            print(f"{i}. {str}")
            i += 1
        i = 0
        continue
    
    for str in evropa:
            if str == a:
                print('joostbot: это связано с йостом')
                w = True
    if w == True:
        continue
    for str in noevropa:
            if str == a:
                print('joostbot: это не связано с йостом')
                w = True
    if w == True:
        continue
    print('joostbot: это связано с йостом?')
    while True:
            xc = input('введите "да" или "нет": ')
            if xc == "да":
                evropa += b
                print('joostbot: хорошо,  запомню')
                break
            elif xc == 'нет':
                noevropa += b
                print('joostbot: запомню')
                break
            else:
                print(f"joostbot: ПОЖАЛУЙСТА, скажите, слово '{a}' связано с йостом?(да или нет)")
