"""
1. 시스템의 입력/출력 인코딩 방식
2. 출력
3. 변수 선언
4. 조건문
5. 반복문
6. 함수 선언
7. 클래스
8. 객체 생성
"""
# 시스템의 입력/출력 인코딩 방식
import sys

print("---시스템의 입력/출력 인코딩 방식---")
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력
print("---출력---")
print("Hello, Python!")

# 변수 선언
print("---변수 선언---")
myname = "bizzy"
print(myname)

# 조건문
print("---조건문---")
if myname == "bizzy":
    print("Hi, bizzy!")

# 반복문
print("---반복문---")
for i in range(1, 10):
    for j in range(1, 10):
        print( ("%d * %d = " % (i, j)), i*j )

# 함수 선언
print("---함수 선언---")
def Hello():
    print("Hello")

Hello()

# 클래스
print("---클래스---")
class Food:
    pass

# 객체 생성
food = Food()
