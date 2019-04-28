#!/usr/bin/python
# -*- coding: UTF-8 -*-
# made by 3s_NwGeek


f = open('createdict.txt', 'w')
name='li hai yan'

try_to_bruteforce=name.split(' ')
temp=''
b_f0=name.replace(' ','')   #zhangsanmiao
b_f1=b_f0.capitalize()      #Zhangsanmiao
b_f2=try_to_bruteforce[0]   #zhangsm
for i, char in enumerate( try_to_bruteforce):
    if i>0 : b_f2=b_f2+char[0:1]
b_f3=b_f2.capitalize()      #Zhangsm
b_f4=''                     #zsm
for char in try_to_bruteforce:
    b_f4=b_f4+char[:1]
b_f5=b_f4.capitalize()      #Zsm
b_f6=b_f5.upper()           #ZSM
b_f7=try_to_bruteforce[0]+'_'   #zhang_sanmiao
for i, char in enumerate( try_to_bruteforce):
    if i>0 : b_f7=b_f7+char
b_f8=try_to_bruteforce[0]+'_'   #zhang_sm
for i, char in enumerate( try_to_bruteforce):
    if i>0 : b_f8=b_f8+char[0:1]
b_f9=try_to_bruteforce[0].capitalize()+'_'   #Zhang_sm
for i, char in enumerate( try_to_bruteforce):
    if i>0 : b_f9=b_f9+char[0:1]

for brute in  open('dict.txt', 'r').read().splitlines():
    f.write(b_f0 + brute + '\n')
    f.write(b_f1 + brute + '\n')
    f.write(b_f2 + brute + '\n')
    f.write(b_f3 + brute + '\n')
    f.write(b_f4 + brute + '\n')
    f.write(b_f5 + brute + '\n')
    f.write(b_f6 + brute + '\n')
    f.write(b_f7 + brute + '\n')
    f.write(b_f8 + brute + '\n')
    f.write(b_f9 + brute + '\n')

for brute in  open('dict_re.txt', 'r').read().splitlines():
    f.write(brute + b_f0 + '\n')
    f.write(brute + b_f1 + '\n')
    f.write(brute + b_f2 + '\n')
    f.write(brute + b_f3 + '\n')
    f.write(brute + b_f4 + '\n')
    f.write(brute + b_f5 + '\n')
    f.write(brute + b_f6 + '\n')
    f.write(brute + b_f7 + '\n')
    f.write(brute + b_f8 + '\n')
    f.write(brute + b_f9 + '\n')

f.close()

print b_f0
print b_f1
print b_f2
print b_f3
print b_f4
print b_f5
print b_f6
print b_f7
print b_f8
print b_f9
