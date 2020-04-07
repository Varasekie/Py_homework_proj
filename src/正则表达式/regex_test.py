import os
import requests
import re

####加了r，使得其变成正常的字符
a = re.search(r'123', '123 .com')
print(a)
# <re.Match object; span=(0, 3), match='123'>

b = re.search(r'\n', '一个换行符\n')
print(b)
# <re.Match object; span=(5, 6), match='\n'>



#####.

####用点来代替任何除了换行符以外的符号
c = re.search(r'Vara.', 'Varasekie')
# <re.Match object; span=(0, 5), match='Varas'>


#####逻辑或
k = re.search(r'[a-z]|[0-9]','Hello')
print(k)
# <re.Match object; span=(1, 2), match='e'>
k = re.search(r'[a-z]|[0-9]','H2ello')
print(k)
# <re.Match object; span=(1, 2), match='2'>


####前置的脱字符，要求必须以某字符串开头
l = re.search(r'^Vara','Varasekie')
print(l)
l = re.search(r'^Vara','123Vara')
print(l)
####注意必须是以整个字符开头
l = re.search(r'^Vara','Vars')
print(l)
# <re.Match object; span=(0, 4), match='Vara'>
# None
# None

####后置的字符$，要求以某整个字符结尾
m = re.search(r'kie$','Varase')
print(m)
#None
m = re.search(r'kie$','Varasekie')
print(m)
# None
# <re.Match object; span=(6, 9), match='kie'>



####反斜杠

#1.
####字符串中，可以运用\,接触特殊功能
####比如说，想让.单纯的只是表示一个.（.本来表示的是一个字母
f = re.search(r'\.', 'hello.com')
print(f)

#2.
###使一个普通字符变成特殊字符
####用\d来表示数字
b = re.search(r'\d\d\d', '123.com')
print(b)
# <re.Match object; span=(0, 3), match='123'>

#3.
####引用序号所对应的子组表示的字符串（复杂的表达）
####子组就是一个小括号括起来的，\1代表第一个子组（算是简写方式
####一定要加上r，否则可能不会生效
a = re.search(r'(abc)(def)\1\1','abcdefabcabc')
print(a)

#4.
####可以用\来表示八进制数（ASCLL码，来表示某个字符
####比如0的ASCII码，对应八进制是060
###三位数就可以表示是八进制
n = re.search(r'Varasekie\060','Varasekie0')
print(n)
# <re.Match object; span=(0, 10), match='Varasekie0'>
n = re.search(r'\141','a')
print(n)
# <re.Match object; span=(0, 1), match='a'>


####[]
####将里面的字符都当作普通字符来看待
o = re.search(r'[.]','test.\n')
print(o)
# <re.Match object; span=(4, 5), match='.'>


####几种特殊字符
#（1）
####\即便是在[]中，也是表达的转义字符的意思，整个字符是一体的
a = re.findall(r'[\n]','Varasekie\n')
print(a)
# ['\n']

####(2)
####表示一个范围
h = re.findall(r'[a-z]','hello')
print(h)
# ['h', 'e', 'l', 'l', 'o']

####(3)^
####在[]中表示取反，注意只能放在最前
####如果是在最后，就是本身而已
a = re.findall(r'[^a-z]','Varasekie')
print(a)
# ['V']



#2.
####[]可以表示，其中任意一个匹配上即可（只匹配第一个）
####py的这个则表达式严格区分大小写,可以关闭大小写敏感模式
g = re.search(r'[helo]','HELLOhhhhh')
print(g)
# <re.Match object; span=(5, 6), match='h'>


####注意如果要匹配数字，要注意是吧数字当成字符来匹配
j = re.search(r'[0-255]','188')
print(j)
#<re.Match object; span=(0, 1), match='1'>
# 正确写法：
####注意是用-连接，而且数字之间不用，分隔开
j = re.search(r'[0-1][0-9][0-9]','188')
print(j)
# <re.Match object; span=(0, 3), match='188'>





####{}代表一种循环

####用大括号表示重复几次
d = re.search(r'Vara(.){3}', 'Varasekie')
print(d)
####默认是只对前一个字符进行迭代，如果对多个字母迭代，用（）
e = re.search(r'Vara.{3}', 'Varasekie')
print(e)
# <re.Match object; span=(0, 7), match='Varasek'>
# <re.Match object; span=(0, 7), match='Varasek'>

####重复次数：
# {M,}至少重复M次
# {.N}等价于{0，N}
# {N}需要匹配N次

####表示b重复的次数在2-5内都可以
i = re.search(r'ab{2，5}c','abbc')
print(i)
#None

####注意，(除了1之外）在边缘上的循环数字次数是不会被匹配的，所以i才是None
i = re.search(r'ab{1,10}c','abc')
print(i)
# <re.Match object; span=(0, 3), match='abc'>


####*，+，？(尽量用，py有运算优化
# *：匹配0次或多次，等价于{0，}
# +：匹配1次或多次，等价于{1，}
# ？：匹配0次或1次，等价于{0，1}

a = re.findall(r'abc*','abccccccc')
print(a)
# ['abccccccc']

a = re.findall(r'abc*','ab')
print(a)
# ['ab']

b = re.findall(r'[ab?c]','ac')
print(b)
# ['a', 'c']

d = re.findall(r'a+bc','bc')
print(d)
###此时无法匹配，就返回了一个空list
# []

####贪婪和非贪婪
####默认是贪婪，会尽可能多的去配对
####举例：
s = '<html><img src = \'abc \'></html>'
a = re.findall(r'<img.+>',s)
print(a)
# ["<img src = 'abc '></html>"]
####默认将里面所有的都包含在内了
####开启非贪婪：在表示重复的字符后，加一个？，开启非贪婪模式
a = re.findall(r'<img.+?>',s)
print(a)
# ["<img src = 'abc '>"]

a = src="https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2981719391,3903827923&fm=26&gp=0.jpg"