## Q1. Shell, Terminal, CLI 구분

### Problem
Terminal, Shell, CLI를 구분하고 `ls -la`에서 각각의 역할을 설명한다.

### My Answer
- Terminal: 명령어를 입력하고 결과를 보는 창/프로그램이다. 예: macOS Terminal, VS Code Terminal.
- Shell: 사용자가 입력한 명령어를 해석해서 OS에 실행 요청하는 프로그램이다. 예: bash, zsh.
- CLI: 텍스트 명령어로 컴퓨터나 프로그램과 상호작용하는 방식이다.

`ls -la`에서:
- Terminal: 사용자가 `ls -la`를 입력하는 창
- Shell: `ls` 명령어와 `-la` 옵션을 해석해서 실행하는 프로그램
- CLI: `ls -la`처럼 텍스트 명령어로 조작하는 방식

`ls -la` 의미:
- `ls`: directory contents를 보여준다.
- `-l`: long format으로 자세히 보여준다.
- `-a`: 숨김 파일까지 포함해서 보여준다.

## Q2. Path, Current Directory, Absolute/Relative Path

### Problem
현재 위치가 다음과 같다고 하자.

/Users/minseo/projects/health-record-api

폴더 구조는 다음과 같다.

health-record-api/
├── main.py
├── app/
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_records.py
└── README.md

질문:

1. 현재 위치를 확인하는 명령어는?
2. 현재 위치에서 app 폴더로 이동하는 명령어는?
3. app 폴더 안에서 다시 health-record-api 루트로 돌아가는 명령어는?
4. 현재 위치가 health-record-api일 때, models.py를 relative path로 표현하면?
5. models.py를 absolute path로 표현하면?
6. . 과 ..의 의미는?

### My Answer
1. pwd
2. cd app
3. cd ..
4. ce /health-record-api/app/models.py
5. I don't know the relative/absolute path difference.
6. . = current directory, .. = parent directory

### Correction
1. 현재 위치 확인:
pwd

2. 현재 위치에서 app 폴더로 이동:
cd app

3. app 폴더 안에서 루트로 돌아가기:
cd ..

4. 현재 위치가 health-record-api일 때 models.py의 relative path:
app/models.py

5. models.py의 absolute path:
/Users/minseo/projects/health-record-api/app/models.py

6. . 과 ..의 의미:
.  = current directory
.. = parent directory

### Key Point
- Absolute path: /부터 시작하는 전체 경로. 현재 어디에 있든 같은 파일/폴더를 가리킨다.
- Relative path: 현재 위치 기준 경로.
- cd는 directory로 이동할 때 쓰는 명령어다. 파일에는 cd할 수 없다.
- 파일 내용을 확인할 때는 cat, less 같은 명령어를 쓴다.

예:
cat app/models.py
less app/models.py


## Q3. cd vs cat vs less

### Problem
현재 위치가 다음과 같다고 하자.

/Users/minseo/projects/health-record-api

폴더 구조:

health-record-api/
├── main.py
├── app/
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_records.py
└── README.md

아래 작업을 하기 위한 명령어를 각각 써라.

1. app 폴더로 이동
2. main.py 파일 내용 출력
3. README.md 파일을 스크롤하면서 보기
4. tests 폴더로 이동
5. test_records.py 파일 내용 출력
6. 현재 위치가 tests일 때, app/routes.py 파일 내용 출력
7. 현재 위치가 tests일 때, 루트 폴더로 돌아가기

### My Answer
1. cd app
2. cd .. -> cat main.py
3. less README.md
4. cd tests
5. cat test_records.py
6. cat /Users/minseo/projects/health-record-api/app/routes.py
7. cd /Users/minseo/projects/health-record-api

### Correction
1. app 폴더로 이동

정답:
cd app

이건 맞음.

2. main.py 파일 내용 출력

네 답:
cd .. -> cat main.py

부분적으로 맞음. 하지만 문제의 현재 위치는 처음에 /Users/minseo/projects/health-record-api라고 했기 때문에, 2번만 독립적으로 보면 그냥 아래가 정답이다.

cat main.py

다만 1번에서 실제로 cd app을 한 뒤 이어서 2번을 한다면 네 답처럼 루트로 돌아온 뒤 cat main.py를 해야 한다.

cd ..
cat main.py

정리:
- 각 문항을 독립적으로 보면: cat main.py
- 1번 실행 후 이어서 한다고 보면: cd .. 후 cat main.py

3. README.md 파일을 스크롤하면서 보기

정답:
less README.md

맞음.

4. tests 폴더로 이동

정답:
cd tests

맞음. 단, 3번까지 실행한 현재 위치가 루트라는 전제에서 맞음.

5. test_records.py 파일 내용 출력

정답:
cat test_records.py

맞음. 현재 위치가 tests라면 맞다.

6. 현재 위치가 tests일 때, app/routes.py 파일 내용 출력

네 답:
cat /Users/minseo/projects/health-record-api/app/routes.py

이건 absolute path라서 실행은 된다. 하지만 문제는 relative path 감각을 보려는 문제였다.

현재 위치:
/Users/minseo/projects/health-record-api/tests

목표 파일:
/Users/minseo/projects/health-record-api/app/routes.py

tests에서 루트로 한 칸 올라간 뒤 app/routes.py로 가야 한다.

정답:
cat ../app/routes.py

absolute path도 가능하지만, Lec 01 복습 목적상 여기서는 relative path로 쓰는 게 더 좋다.

7. 현재 위치가 tests일 때, 루트 폴더로 돌아가기

네 답:
cd /Users/minseo/projects/health-record-api

맞음. absolute path로 돌아가는 방식이다.

더 짧은 답:
cd ..

현재 위치가 tests라면 parent directory가 health-record-api 루트이므로 cd ..가 더 간단하다.

### Final Correct Answer
1. cd app
2. cat main.py
3. less README.md
4. cd tests
5. cat test_records.py
6. cat ../app/routes.py
7. cd ..

### Key Point
- cd는 directory 이동.
- cat은 파일 내용을 바로 출력.
- less는 파일 내용을 스크롤하면서 보기.
- 파일에는 cd할 수 없다.
- 현재 위치가 tests일 때 app/routes.py를 보려면 ../app/routes.py를 쓴다.
- ..는 parent directory다.
- absolute path는 어디서든 작동하지만 길다.
- relative path는 현재 위치 기준이라 실전에서 더 자주 쓴다.

## Q4. ls, hidden files, project folder check

### Problem
현재 위치가 다음과 같다고 하자.

/Users/minseo/projects/health-record-api

폴더 구조는 다음과 같다.

health-record-api/
├── .env
├── .git/
├── .gitignore
├── main.py
├── README.md
├── app/
├── tests/
└── requirements.txt

아래 작업을 하기 위한 명령어를 각각 써라.

1. 현재 폴더의 일반 파일/폴더 목록 보기
2. 숨김 파일까지 포함해서 보기
3. 자세한 정보까지 포함해서 보기
4. 숨김 파일 + 자세한 정보까지 같이 보기
5. .env 파일 내용 출력
6. .gitignore 파일 내용 출력
7. 현재 폴더에 requirements.txt가 있는지 확인하기 위해 쓸 명령어

### My Answer
1. ls
2. ls -a
3. ls -l
4. ls -al
5. cat -a .env
6. cat -a .gitignore
7. ls requirements.txt

### Correction
1. 현재 폴더의 일반 파일/폴더 목록 보기:
ls

정답.

2. 숨김 파일까지 포함해서 보기:
ls -a

정답.

3. 자세한 정보까지 포함해서 보기:
ls -l

정답.

4. 숨김 파일 + 자세한 정보까지 같이 보기:
ls -al

정답. 보통 ls -la도 많이 쓴다. 둘 다 가능하다.

5. .env 파일 내용 출력:
cat .env

네 답은 cat -a .env였는데, 여기서는 굳이 -a가 필요 없다.
cat -a는 파일 내용을 볼 수는 있지만, 탭/줄끝 같은 특수문자까지 표시하는 옵션이다.
일반적으로 파일 내용 출력은 cat .env가 맞다.

주의:
실제 프로젝트에서 .env에는 SECRET_KEY, DATABASE_URL, API_KEY 같은 민감정보가 들어갈 수 있으므로 터미널에서 확인은 가능하지만 GitHub에 올리면 안 된다.

6. .gitignore 파일 내용 출력:
cat .gitignore

네 답은 cat -a .gitignore였는데, 마찬가지로 일반 확인 목적이면 cat .gitignore가 맞다.

7. 현재 폴더에 requirements.txt가 있는지 확인하기:
ls requirements.txt

정답. 파일이 있으면 이름이 출력되고, 없으면 No such file or directory 에러가 난다.

다른 방법:
test -f requirements.txt && echo "exists"
find . -name "requirements.txt"

하지만 지금 Lec 01 단계에서는 ls requirements.txt면 충분하다.

### Final Correct Answer
1. ls
2. ls -a
3. ls -l
4. ls -al
5. cat .env
6. cat .gitignore
7. ls requirements.txt

### Key Point
- ls는 현재 directory의 파일/폴더 목록을 보여준다.
- -a는 all의 의미로 숨김 파일까지 보여준다.
- -l은 long format의 의미로 권한, 소유자, 크기, 수정시간 등을 자세히 보여준다.
- ls -al 또는 ls -la는 숨김 파일까지 포함해서 자세히 보여준다.
- .env, .git, .gitignore처럼 .으로 시작하는 파일/폴더는 hidden file이다.
- cat은 파일 내용을 출력한다.
- cat -a는 특수문자까지 표시하는 옵션이라 일반 파일 확인에는 보통 필요 없다.
- .env 파일은 확인할 수는 있지만, 민감정보가 들어있을 수 있으므로 GitHub에 올리면 안 된다.

## Q5. mkdir, touch, cp, mv, rm

### Problem
현재 위치가 다음과 같다고 하자.

/Users/minseo/projects/health-record-api

아래 작업을 하기 위한 명령어를 각각 써라.

1. logs 폴더 만들기
2. temp.txt 파일 만들기
3. temp.txt를 logs 폴더 안으로 이동하기
4. logs/temp.txt를 logs/app.log라는 이름으로 바꾸기
5. README.md를 README_backup.md로 복사하기
6. logs/app.log 파일 삭제하기
7. logs 폴더 삭제하기

### My Answer
1. mkdir logs
2. touch temp.txt
3. mv temp.txt /Users/minseo/projects/health-record-api/logs or logs?
4. mv logs/temps.txt logs/app.log
5. cp README.md README_backupmd
6. rm logs/app.log
7. rm -r logs

### Correction
1. logs 폴더 만들기:
mkdir logs

정답.

2. temp.txt 파일 만들기:
touch temp.txt

정답.

3. temp.txt를 logs 폴더 안으로 이동하기:
mv temp.txt logs/

정답은 이게 가장 깔끔하다.

네가 쓴 absolute path도 가능하다:
mv temp.txt /Users/minseo/projects/health-record-api/logs/

하지만 현재 위치가 이미 /Users/minseo/projects/health-record-api이므로 relative path인 logs/가 더 낫다.

주의:
logs와 logs/는 대부분 상황에서 둘 다 작동하지만, directory라는 의도를 명확히 하려면 logs/처럼 쓰는 게 좋다.

4. logs/temp.txt를 logs/app.log라는 이름으로 바꾸기:
mv logs/temp.txt logs/app.log

네 답은 logs/temps.txt라고 되어 있었는데 파일명 오타다.
원래 파일은 temp.txt다.

5. README.md를 README_backup.md로 복사하기:
cp README.md README_backup.md

네 답은 README_backupmd라서 확장자 앞의 점이 빠졌다.
README_backup.md가 맞다.

6. logs/app.log 파일 삭제하기:
rm logs/app.log

정답.

7. logs 폴더 삭제하기:
rm -r logs

정답. 다만 logs가 빈 폴더라면 아래도 가능하다:
rmdir logs

실전에서는 rm -r은 조심해야 한다. 폴더 안의 내용까지 삭제한다.

### Final Correct Answer
1. mkdir logs
2. touch temp.txt
3. mv temp.txt logs/
4. mv logs/temp.txt logs/app.log
5. cp README.md README_backup.md
6. rm logs/app.log
7. rm -r logs

### Key Point
- mkdir logs: logs directory 생성
- touch temp.txt: 빈 파일 생성
- mv temp.txt logs/: temp.txt를 logs 폴더 안으로 이동
- mv logs/temp.txt logs/app.log: 파일 이름 변경
- cp README.md README_backup.md: 파일 복사
- rm logs/app.log: 파일 삭제
- rm -r logs: 폴더와 내부 내용 삭제
- mv는 이동과 이름 변경 둘 다 담당한다.
- cp는 복사라서 원본이 남는다.
- rm은 삭제라서 되돌리기 어렵다.
- relative path는 현재 위치 기준이다.
- absolute path는 /부터 시작하는 전체 경로다.

## Q6. Redirection and Pipe Basics

### Problem
현재 위치에 아래 파일이 있다고 하자.

app.log

app.log 내용:

INFO server started
ERROR database connection failed
INFO retrying
ERROR timeout
INFO server stopped

아래 작업을 하기 위한 명령어를 각각 써라.

1. app.log 파일 내용 전체 출력
2. app.log에서 ERROR가 들어간 줄만 출력
3. "hello"라는 문자열을 output.txt에 저장하기. 기존 내용은 덮어쓴다.
4. "world"라는 문자열을 output.txt 뒤에 추가하기.
5. app.log에서 ERROR가 들어간 줄만 errors.txt에 저장하기.
6. app.log에서 INFO가 들어간 줄의 개수를 세기.
7. nonexistent.txt를 출력하려고 했을 때 발생하는 에러 메시지를 error.txt에 저장하기.

### My Answer
1. cat app.log
2. grep "ERROR" app.log
3. "hello" > output.txt
4. "world" >> output.txt
5. grep "ERROR" app.log > errors.txt
6. wc -1 grep "INFO" app.log
7. cat nonexistent.txt 2> error.txt

### Correction
1. app.log 파일 내용 전체 출력:
cat app.log

정답.

2. app.log에서 ERROR가 들어간 줄만 출력:
grep "ERROR" app.log

정답.

3. "hello"라는 문자열을 output.txt에 저장하기:
echo "hello" > output.txt

네 답은 "hello" > output.txt였는데, 문자열만 단독으로 쓰면 명령어가 아니다.
터미널에서 문자열을 출력하려면 echo가 필요하다.

틀린 형태:
"hello" > output.txt

맞는 형태:
echo "hello" > output.txt

4. "world"라는 문자열을 output.txt 뒤에 추가하기:
echo "world" >> output.txt

마찬가지로 echo가 필요하다.

5. app.log에서 ERROR가 들어간 줄만 errors.txt에 저장하기:
grep "ERROR" app.log > errors.txt

정답.

6. app.log에서 INFO가 들어간 줄의 개수를 세기:
grep "INFO" app.log | wc -l

네 답:
wc -1 grep "INFO" app.log

틀린 이유:
- wc -1이 아니라 wc -l이다. 소문자 L이다.
- grep으로 INFO 줄을 먼저 뽑고, 그 결과를 wc -l로 넘겨야 한다.
- pipe | 를 써야 한다.

흐름:
grep "INFO" app.log → INFO가 들어간 줄만 출력
| → 앞 출력 결과를 뒤 명령어 입력으로 넘김
wc -l → 줄 수 계산

7. nonexistent.txt를 출력하려고 했을 때 발생하는 에러 메시지를 error.txt에 저장하기:
cat nonexistent.txt 2> error.txt

정답.

### Final Correct Answer
1. cat app.log
2. grep "ERROR" app.log
3. echo "hello" > output.txt
4. echo "world" >> output.txt
5. grep "ERROR" app.log > errors.txt
6. grep "INFO" app.log | wc -l
7. cat nonexistent.txt 2> error.txt

### Key Point
- cat file: 파일 내용 출력
- grep "ERROR" app.log: ERROR가 들어간 줄만 출력
- echo "hello": 문자열을 stdout으로 출력
- \> : stdout을 파일로 저장한다. 기존 내용은 덮어쓴다.
- \>> : stdout을 파일 뒤에 추가한다.
- | : 앞 명령어의 stdout을 뒤 명령어의 stdin으로 넘긴다.
- wc -l: line count. 줄 수를 센다.
- 2> : stderr를 파일로 저장한다.
- stdout과 stderr는 다르다.
- grep "INFO" app.log | wc -l 은 “INFO 줄만 뽑아서 그 줄 수를 세라”는 뜻이다.

## Q7. Permission and chmod Basics

### Problem
현재 위치에 run.sh 파일이 있다고 하자.

ls -l run.sh 결과가 아래와 같다.

-rw-r--r--  1 minseo  staff  120 May 17  run.sh

아래 질문에 답해라.

1. 이 파일은 현재 실행 권한이 있는가?
2. run.sh에 실행 권한을 추가하는 명령어는?
3. 실행 권한을 추가한 뒤 run.sh를 실행하는 명령어는?
4. chmod +x run.sh에서 +x의 의미는?
5. ./run.sh에서 ./의 의미는?
6. 왜 그냥 run.sh라고 치지 않고 ./run.sh라고 실행하는가?

### My Answer
1. 없음 -rw-r--r-- -> x 가 빠져있음
2. chmod +x run.sh
3. ./run.sh
4. 권한 추가 - 편집할 수 있게
5. run 실행해라
6. sh 파일의 특징?

### Correction
1. 이 파일은 현재 실행 권한이 있는가?

정답:
없음.

이유:
-rw-r--r-- 에 x가 없다.

권한 구조:
-rw-r--r--

첫 글자:
- = regular file

그 다음 3개:
rw- = owner 권한. 읽기/쓰기 가능, 실행 불가.

그 다음 3개:
r-- = group 권한. 읽기만 가능.

마지막 3개:
r-- = others 권한. 읽기만 가능.

x가 없으므로 실행 권한이 없다.

2. run.sh에 실행 권한을 추가하는 명령어:

정답:
chmod +x run.sh

맞음.

3. 실행 권한을 추가한 뒤 run.sh를 실행하는 명령어:

정답:
./run.sh

맞음.

4. chmod +x run.sh에서 +x의 의미는?

네 답:
권한 추가 - 편집할 수 있게

수정:
+x는 실행 권한을 추가한다는 뜻이다.

정확한 의미:
chmod +x run.sh = run.sh 파일에 execute permission을 추가한다.

x = execute
r = read
w = write

편집/수정 권한은 w다.
실행 권한은 x다.

5. ./run.sh에서 ./의 의미는?

네 답:
run 실행해라

수정:
./ 는 current directory를 의미한다.

즉:
./run.sh

의 의미는:
현재 디렉토리에 있는 run.sh 파일을 실행하라.

. = current directory
/ = 경로 구분자
./run.sh = 현재 폴더 안의 run.sh

6. 왜 그냥 run.sh라고 치지 않고 ./run.sh라고 실행하는가?

네 답:
sh 파일의 특징?

수정:
이건 .sh 파일의 특징 때문이 아니다.

이유:
shell은 명령어를 입력하면 PATH에 등록된 디렉토리들에서 실행 파일을 찾는다.
하지만 현재 디렉토리 . 은 보통 PATH에 포함되어 있지 않다.

그래서:
run.sh

라고 치면 shell은 PATH 안에서 run.sh를 찾는다.

하지만 현재 폴더의 run.sh를 실행하려면 명시적으로:
./run.sh

라고 해야 한다.

즉:
./run.sh = 현재 폴더에 있는 run.sh를 실행하라고 정확히 지정하는 것.

### Final Correct Answer
1. 없음. -rw-r--r-- 에 x가 없기 때문에 실행 권한이 없다.
2. chmod +x run.sh
3. ./run.sh
4. +x는 execute permission, 즉 실행 권한을 추가한다는 뜻이다.
5. ./는 current directory, 즉 현재 폴더를 의미한다.
6. shell은 기본적으로 현재 디렉토리에서 실행 파일을 자동으로 찾지 않고 PATH에서 찾기 때문에, 현재 폴더의 파일을 실행하려면 ./run.sh처럼 명시해야 한다.

### Key Point
- r = read
- w = write
- x = execute
- chmod +x run.sh는 실행 권한을 추가한다.
- 편집/수정 권한은 w이고, 실행 권한은 x다.
- . 은 current directory다.
- .. 은 parent directory다.
- ./run.sh는 현재 디렉토리에 있는 run.sh를 실행하라는 뜻이다.
- 그냥 run.sh라고 치면 shell은 PATH에서 run.sh를 찾는다.
- 현재 디렉토리는 보통 PATH에 포함되어 있지 않기 때문에 ./run.sh라고 써야 한다.

## Q8. Lec 01 Final Review - Project Folder Scenario

### Problem
현재 위치가 다음과 같다고 하자.

/Users/minseo/projects/health-record-api

폴더 구조는 다음과 같다.

health-record-api/
├── .env
├── .gitignore
├── README.md
├── main.py
├── app/
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_records.py
└── run.sh

아래 작업을 하기 위한 명령어를 각각 써라.

1. 현재 위치 확인
2. 숨김 파일까지 포함해서 자세히 보기
3. app/routes.py 파일 내용 출력
4. README.md 파일을 스크롤하면서 보기
5. tests 폴더로 이동
6. 현재 위치가 tests일 때, app/models.py 파일 내용 출력
7. 루트 폴더로 돌아가기
8. logs 폴더 만들기
9. "server started" 문자열을 logs/app.log에 저장하기
10. "ERROR database failed" 문자열을 logs/app.log 뒤에 추가하기
11. logs/app.log에서 ERROR가 들어간 줄만 출력
12. logs/app.log에서 ERROR가 들어간 줄만 errors.txt에 저장
13. run.sh에 실행 권한 추가
14. run.sh 실행
15. logs 폴더 삭제

### My Answer
1. pwd
2. ls -al
3. cat app/routes.py
4. less README.md
5. cd tests
6. cat ../app/models.py
7. 루트폴더가 정확히 디폴트 디렉토리 말하는거야? cd ~ / 루트폴더가 health-record-api를 말하는거면 cd .. 만 해도 되는거고
8. mkdir logs
9. echo "server started" > logs/app.log
10. echo "ERROR database failed" >> logs/app.log
11. grep "ERROR" logs/app.log
12. grep "ERROR" logs/app.log > errors.txt
13. chmod +x run.sh
14. ./run.sh
15. rm -r logs

### Correction
1. 현재 위치 확인:
pwd

정답.

2. 숨김 파일까지 포함해서 자세히 보기:
ls -al

정답. ls -la도 가능하다.

3. app/routes.py 파일 내용 출력:
cat app/routes.py

정답.

4. README.md 파일을 스크롤하면서 보기:
less README.md

정답.

5. tests 폴더로 이동:
cd tests

정답.

6. 현재 위치가 tests일 때, app/models.py 파일 내용 출력:
cat ../app/models.py

정답.

현재 위치:
health-record-api/tests

목표 파일:
health-record-api/app/models.py

따라서:
.. 로 health-record-api로 올라간 뒤 app/models.py로 간다.

7. 루트 폴더로 돌아가기:

여기서 말한 루트 폴더는 시스템 root / 가 아니라 프로젝트 루트 health-record-api를 의미한다.

현재 위치가 tests라면 정답:
cd ..

네가 지적한 것처럼 cd ~는 home directory로 이동한다.
cd / 는 시스템 root directory로 이동한다.
이 문제에서는 둘 다 의도한 답이 아니다.

정답:
cd ..

8. logs 폴더 만들기:
mkdir logs

정답.

주의:
이전 작업 흐름상 7번에서 프로젝트 루트로 돌아왔기 때문에 mkdir logs가 맞다.

9. "server started" 문자열을 logs/app.log에 저장하기:
echo "server started" > logs/app.log

정답.

10. "ERROR database failed" 문자열을 logs/app.log 뒤에 추가하기:
echo "ERROR database failed" >> logs/app.log

정답.

11. logs/app.log에서 ERROR가 들어간 줄만 출력:
grep "ERROR" logs/app.log

정답.

12. logs/app.log에서 ERROR가 들어간 줄만 errors.txt에 저장:
grep "ERROR" logs/app.log > errors.txt

정답.

13. run.sh에 실행 권한 추가:
chmod +x run.sh

정답.

14. run.sh 실행:
./run.sh

정답.

15. logs 폴더 삭제:
rm -r logs

정답.

### Final Correct Answer
1. pwd
2. ls -al
3. cat app/routes.py
4. less README.md
5. cd tests
6. cat ../app/models.py
7. cd ..
8. mkdir logs
9. echo "server started" > logs/app.log
10. echo "ERROR database failed" >> logs/app.log
11. grep "ERROR" logs/app.log
12. grep "ERROR" logs/app.log > errors.txt
13. chmod +x run.sh
14. ./run.sh
15. rm -r logs

### Key Point
- 프로젝트 루트는 현재 프로젝트의 최상위 폴더를 의미한다. 여기서는 health-record-api다.
- 시스템 root는 / 이다. 프로젝트 루트와 다르다.
- home directory는 ~ 이다. 프로젝트 루트와 다르다.
- cd .. 는 parent directory로 이동한다.
- 현재 위치가 tests라면 cd .. 로 health-record-api 프로젝트 루트로 돌아간다.
- ls -al과 ls -la는 둘 다 가능하다.
- echo "text" > file 은 기존 내용을 덮어쓴다.
- echo "text" >> file 은 기존 내용 뒤에 추가한다.
- grep "ERROR" file 은 ERROR가 들어간 줄만 보여준다.
- chmod +x run.sh 는 실행 권한을 추가한다.
- ./run.sh 는 현재 폴더의 run.sh를 실행한다.