import itertools
name_file = input('Name of file: ')
contacts = list()


def perm_fio(fio):
    perms = list()
    arr = fio.split()
    perms2 = list()
    for r in range(1, len(arr)+1):
        perms.append(list(itertools.permutations(arr, r=r)))
    for i in perms:
        for j in i:
            perms2.append(' '.join(j).lower())
    return perms2


class Contact:
    def __init__(self, fio, number, email):
        self.fio = fio
        self.number = number
        self.email = email

    def __str__(self):
        return f'Contact {self.fio}'


with open(f'{name_file}.txt', encoding='utf-8') as f:
    for line in f.readlines():
        arr = line.split(',')
        try:
            if '\n' in arr[2]:
                s = arr[2].replace('\n', '')
            contact = Contact(arr[0], arr[1][1:], s[1:])
            contacts.append(contact)
        except:
            continue


while True:
    con = None
    ques = '***'
    try:
        type_of_search = int(input('Введите 1 чтобы начать поиск по номеру 2 по почте 3 по фио 4 чтобы вывести всех у кого не заполнен номер и или почта 5 чтобы вывести все контакты:  '))
    except:
        print('Некорректный ввод')
        continue
    if type_of_search != 1 and type_of_search != 2 and type_of_search != 3 and type_of_search != 4 and type_of_search != 5:
        print('Некорректный ввод')
        continue
    if type_of_search == 1:
        number = input('Number: ')
        for i in contacts:
            if i.number == number:
                print(f'Found contact by number: fio: {i.fio}, nubmer: {i.number}, email: {i.email}')
                con = i
                ques = input('Введите 1 чтобы изменить контакт или введите 2 чтобы выйти: ')
                if ques == '1':
                    try:
                        selec = int(input('Введите 1 чтобы изменить фио 2 чтобы изменить номер 3 чтобы изменить почту: '))
                    except:
                        print('Некорректный ввод')
                        continue
                    if selec != 1 and selec != 2 and selec != 3 and selec != 4:
                        print('Некорректный ввод')
                        continue
                    else:
                        if selec == 1:
                            con.fio = input('New fio: ')
                        if selec == 2:
                            con.number = input('New number: ')
                        if selec == 3:
                            con.email = input('New email')
        if ques == '***':
            print('Not found by number')
            continue
    if type_of_search == 2:
        email = input('Email: ')
        for i in contacts:
            if i.email == email:
                print(f'Found contact by email: fio: {i.fio}, nubmer: {i.number}, email: {i.email}')
                con = i
                ques = input('Введите 1 чтобы изменить контакт или введите 2 чтобы выйти: ')
                if ques == '1':
                    try:
                        selec = int(input('Введите 1 чтобы изменить фио 2 чтобы изменить номер 3 чтобы изменить почту: '))
                    except:
                        print('Некорректный ввод')
                        continue
                    if selec != 1 and selec != 2 and selec != 3 and selec != 4:
                        print('Некорректный ввод')
                        continue
                    else:
                        if selec == 1:
                            con.fio = input('New fio: ')
                        if selec == 2:
                            con.number = input('New number: ')
                        if selec == 3:
                            con.email = input('New email')
        if ques == '***':
            print('Not found by email')
            continue
    if type_of_search == 3:
        fio = input('Введите имя или фамилию или фио или инициалы  или набор: ').lower()
        for i in contacts:
            perms_fio = perm_fio(i.fio)
            for b in perms_fio:
                if fio == b:
                    print(f'Found contact by fio: fio: {i.fio}, nubmer: {i.number}, email: {i.email}')
                    ques = input('Введите 1 чтобы изменить контакт или введите 2 чтобы выйти: ')
                    if ques == '1':
                        try:
                            selec = int(input(
                                'Введите 1 чтобы изменить фио 2 чтобы изменить номер 3 чтобы изменить почту: '))
                        except:
                            print('Некорректный ввод')
                            continue
                        if selec != 1 and selec != 2 and selec != 3 and selec != 4:
                            print('Некорректный ввод')
                            continue
                        else:
                            if selec == 1:
                                con.fio = input('New fio: ')
                            if selec == 2:
                                con.number = input('New number: ')
                            if selec == 3:
                                con.email = input('New email')
        if ques == '***':
            print('Not found by fio')
            continue
    if type_of_search == 4:
        for i in contacts:
            if len(i.email) <= 1 or len(i.number) <= 1:
                print(f'{i.fio}')
    if type_of_search == 5:
        for i in contacts:
            print(f'fio: {i.fio}, nubmer: {i.number}, email: {i.email}')



