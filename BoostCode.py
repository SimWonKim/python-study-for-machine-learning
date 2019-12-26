items = 'zero one two three'.split()
print(items)

example = 'python,jquery,javascript'
print(example.split(","))

example = 'python,jquery,javascript'
a, b, c = example.split(",")
print(a, b, c)

example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split(".")
print(subdomain, domain, tld)

# split는 자르는 용도.


colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors)  # 연결 시 빈칸 1칸으로 연결
print(result)

result = ', '.join(colors)  # 연결 시 ", "으로 연결
print(result)

result = '-'.join(colors)  # 연결 시 "-"으로 연결
print(result)

# join은 붙이는 용도.


result = [i for i in range(10) if i % 2 == 0]
print('List comprehensions result ', result)
# [0, 2, 4, 6, 8]

result = [[i] for i in range(10) if i % 2 == 0]
print('List comprehensions result ', result)
# [[0], [2], [4], [6], [8]]


word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]
print('List comprehensions result', result)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

result = [a + b for a in case_1 for b in case_2]
print('loop result ', result)
# loop result  ['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF']
# a가 먼저 고정 됨.

result = [[a + b for a in case_1] for b in case_2]
print('loop result ', result)
# loop result  [['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AF', 'BF', 'CF']]
# b가 먼저 고정 됨.

result = [b + a for a in case_2 for b in case_1]
print('loop result ', result)
# loop result  ['AD', 'BD', 'CD', 'AE', 'BE', 'CE', 'AF', 'BF', 'CF']


for i, v in enumerate(['a', 'b', 'c']):
    print('index : ', i, 'value : ', v)
    # i는 index , v는 value.

mylist = ['a', 'b', 'c', 'd']
print('list value ', list(enumerate(mylist)))
# list value  [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# list를 빼고 출력하면 : list value  <enumerate object at 0x108826300> 메모리 주소값 나옴.

print('dict type result : ', {i: j for i, j in enumerate('this is test sentence, i`m so happy'.split())})
# dict 타입은 json 같은 느낌이다.
# 텍스트 마이닝시 처음에 이렇게 하는 경우가 많다????

print('sum list is ', [sum(x) for x in zip((1, 2, 3), (100, 200, 300), (10, 20, 30))])
# zip을 이용하면 같은 인덱스에 있는 여러 list의 값을 병렬로 추출 가능.
