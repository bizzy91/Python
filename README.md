### git 설정
```
$ git init
$ git add README.md
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/bizzy91/Python.git
$ git push -u origin main
```

### 가상환경
가상환경을 위한 virtualenv 설치
```
$ python3 -m pip3 install --user -U virtualenv
```
현재 경로에서 가상환경을 위한 하위 경로 생성하기
```
$ virtualenv [경로 이름]
(example)$ virtualenv bizzy
```
특정 버전을 지정하려면 아래 명령어를 추가한다.
```
$ virtualenv [경로 이름] --python=[python version]
(example)$ virtualenv bizzy --python=python3.8
(example)$ virtualenv bizzy --python=python3.9
```
가상 환경 활성화
```
$ source [경로 이름]/bin/activate
(example)$ virtualenv bizzy/bin/activate
```
가상 환경 비활성화
```
$ deactivate
```