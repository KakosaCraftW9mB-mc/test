# open file
f = open("C:\SERVER\KakosaCraft_JE\DataBase\Groups\Sample.ini", "r")
f2 = open("C:\SERVER\KakosaCraft_JE\DataBase\Prefix%Suffix\Sample.ini", "r")
# open file final

# 1 DataBase
print('')
print('/DataBase-->')
print('')
print('1-Groups')
print('2-Prefix%Suffix')
print('3-Users')
print('')
db = input('Введите номер каталога: ')
# 1 Groups
if db == "1":
    print('')
    print('/Groups-->')
    print('')
    print('1-Sample.ini--->')

# 1 Groups List
if db == "1":
    print('')
if db == "1":
    data = f.read()
    print(data)
f.close()
# 1 final

# 2 Prefix%Suffix
if db == "2":
    print('')
    print('/Prefix%Suffix-->')
    print('')
    print('1-Sample.ini--->')
    print('')
    
# 2 Prefix%Suffix List
if db == "2":
    data = f2.read()
    print(data)
f2.close()
# 2 final

# 3 Users
if db == "3":
    print('')
    print('/Users--->')
    print('')
    print('Accounts--->')
    print('')
    print('0-Sample.ini-->')
    print('1-StevePro146.ini-->')
    print('2-WanLais.ini-->')
    print('3-Tasty_eye.ini-->')
# 3 Users final
input()
