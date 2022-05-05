# 기본 출력
print("---기본 출력---")
print('Hello, Python!')
print("Hello, Python!")
print('''Hello, Python!''')
print("""Hello, Python!""")

# Separator 옵션
print("---Separator 옵션---")
print("T", "E", "S", "T")
print("T", "E", "S", "T", sep="")
print("2022", "05", "05", sep="-")
print("bizzy", "gmail.com", sep="@")

# End 옵션
print("---End 옵션---")
print("Welcome to Python")
print("Welcome to", end=" ")
print("Python", end="\n")
print()

# Format 옵션
print("---Format 옵션---")
print("{} and {}".format("You", "Me"))
print("{0} and {1} and {0}".format("You", "Me"))
print("{a} and {b}".format(a="You", b="Me"))

# %s: 문자, %d: 정수, %f: 실수
print("---%s: 문자, %d: 정수, %f: 실수---")
print("%s favorite number is %d" % ("My", 3))
print("Test1: %3d, Test2: %5d, Test3: %4.2f" % (999, 999, 1234.5678))
print("Test1:{0: 3d}, Test2: {1: 5d}, Test3:{2: 4.2f}".format(999, 999, 1234.5678))
print("Test1:{a: 3d}, Test2: {b: 5d}, Test3:{c: 4.2f}".format(a=999, b=999, c=1234.5678))

"""
Escape Code
\n: 줄 바꿈
\t: 탭
\b: 백스페이스
\000: 널문자
\\: 슬래시
\': 작은 따옴표
\": 큰 따옴표
\r: 줄 바꿈, 커서를 앞으로 이동
\f: 줄 바꿈, 커서를 다음 줄로 이동
\a: 벨소리
"""
print("---Escape Code---")
print("\t This is tab and this is new line\n")
print("This is null \000")
print("This is \\")
print("This is \'")
print("This is \"")
print("This is \r")
print("This is \f")
