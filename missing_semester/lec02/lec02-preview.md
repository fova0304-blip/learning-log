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

## Lec 02 - Q2. stdin, stdout, stderr

### Problem
아래 명령어들을 보고 질문에 답해라.

python app.py > output.txt 2> error.txt

질문:

1. python app.py는 무엇을 실행하는 명령어인가?
2. \> output.txt는 무엇을 의미하는가?
3. 2> error.txt는 무엇을 의미하는가?
4. stdout과 stderr의 차이는 무엇인가?
5. 만약 app.py가 정상적으로 "server started"를 출력하면 어디에 저장되는가?
6. 만약 app.py에서 ModuleNotFoundError가 발생하면 어디에 저장되는가?
7. 이 명령어 전체를 네 말로 해석하면?

### My Answer
1. app.py을 실행시켜라
2. 정상 출력은 output.txt에 저장
3. 에러 출력은 error.txt에 저장
4. stdout 정상출력 stderror는 에러 출력
5. output.txt 정상출력이라서
6. 에러니깐 error.txt
7. app.py를 실행시키고 정상출력은 output.txt에 저장 오류 출력은 error.txt에 저장

### Correction
1. python app.py는 무엇을 실행하는 명령어인가?

정답:
Python interpreter로 app.py 파일을 실행한다.

네 답도 의미상 맞다. 더 정확히는 python이라는 프로그램이 app.py를 argument로 받아 실행하는 것이다.

2. \> output.txt는 무엇을 의미하는가?

정답:
stdout, 즉 정상 출력을 output.txt 파일로 보낸다.

맞음.

3. 2> error.txt는 무엇을 의미하는가?

정답:
stderr, 즉 에러 출력을 error.txt 파일로 보낸다.

맞음.

4. stdout과 stderr의 차이는 무엇인가?

정답:
stdout은 정상 출력 stream이고, stderr는 에러/경고 출력 stream이다.

네 답도 맞음. 단, 명칭은 stderror가 아니라 stderr다.

5. app.py가 정상적으로 "server started"를 출력하면 어디에 저장되는가?

정답:
output.txt

맞음.

6. app.py에서 ModuleNotFoundError가 발생하면 어디에 저장되는가?

정답:
error.txt

맞음.

7. 이 명령어 전체를 네 말로 해석하면?

정답:
python으로 app.py를 실행하고, 정상 출력은 output.txt에 저장하고, 에러 출력은 error.txt에 저장한다.

네 답 맞음.

### Final Correct Answer
1. python interpreter로 app.py를 실행한다.
2. \> output.txt는 stdout을 output.txt에 저장한다는 뜻이다.
3. 2> error.txt는 stderr를 error.txt에 저장한다는 뜻이다.
4. stdout은 정상 출력이고 stderr는 에러/경고 출력이다.
5. output.txt
6. error.txt
7. python으로 app.py를 실행하고, 정상 출력은 output.txt에 저장하고, 에러 출력은 error.txt에 저장한다.

### Key Point
- python app.py = python 프로그램이 app.py 파일을 실행한다.
- \> 는 stdout redirection이다.
- 2> 는 stderr redirection이다.
- stdout = 정상 출력
- stderr = 에러 출력
- stderr는 standard error의 줄임말이다.
- stdout과 stderr는 둘 다 화면에 보일 수 있지만 내부적으로는 다른 stream이다.
- 1은 stdout, 2는 stderr를 의미한다.

## Lec 02 - Q3. Pipe and stdout/stderr

### Problem
아래 명령어를 보고 질문에 답해라.

python app.py | grep "ERROR"

질문:

1. | 는 무엇을 하는가?
2. python app.py의 어떤 출력이 grep "ERROR"로 넘어가는가?
3. stderr도 자동으로 grep으로 넘어가는가?
4. app.py가 stdout으로 "ERROR database failed"를 출력하면 grep 결과에 보이는가?
5. app.py가 stderr로 "ERROR database failed"를 출력하면 grep 결과에 보이는가?
6. stderr까지 grep으로 넘기고 싶으면 어떤 식으로 써야 하는가?
7. 이 명령어 전체를 네 말로 해석하면?

### My Answer
1. 왼쪽 stdout을 오른쪽 stdout으로 넘김
2. 정상출력을 넘김
3. ㄴㄴ stderr는 걸름
4. ERROR database failed이지만 정상출력이면 보이지
5. ERROR database failed이 평소처럼 출력오류면 안보이지
6. 2>&1 으로 파이프를 대체해야지
7. app.py을 실행시키고 정상출력을 오른쪽으로 넘겨라 그럼 오른쪽에서 error가 있는 문장을 출력시킬거다

### Correction
1. | 는 무엇을 하는가?

네 답:
왼쪽 stdout을 오른쪽 stdout으로 넘김

수정:
| 는 왼쪽 명령어의 stdout을 오른쪽 명령어의 stdin으로 넘긴다.

정확한 구조:
python app.py 의 stdout -> grep "ERROR" 의 stdin

stdout에서 stdout으로 넘기는 게 아니다.
오른쪽 프로그램은 입력을 stdin으로 받는다.

2. python app.py의 어떤 출력이 grep "ERROR"로 넘어가는가?

정답:
stdout, 즉 정상 출력이 넘어간다.

맞음.

3. stderr도 자동으로 grep으로 넘어가는가?

정답:
아니다. pipe는 기본적으로 stderr를 넘기지 않는다.

맞음.

4. app.py가 stdout으로 "ERROR database failed"를 출력하면 grep 결과에 보이는가?

정답:
보인다.

이유:
stdout은 pipe를 통해 grep으로 넘어가고, 그 안에 ERROR가 있기 때문이다.

맞음.

5. app.py가 stderr로 "ERROR database failed"를 출력하면 grep 결과에 보이는가?

정답:
grep 결과에는 안 보인다.

이유:
stderr는 기본 pipe로 넘어가지 않기 때문이다.

단, stderr 자체는 터미널에 따로 보일 수 있다. 중요한 차이다:
- grep이 잡아서 보여주는 것은 아님
- stderr가 터미널에 직접 출력될 수는 있음

6. stderr까지 grep으로 넘기고 싶으면 어떤 식으로 써야 하는가?

네 답:
2>&1 으로 파이프를 대체해야지

수정:
pipe를 대체하는 게 아니다.
stderr를 stdout에 합친 뒤, 그 합쳐진 stdout을 pipe로 넘긴다.

정답:
python app.py 2>&1 | grep "ERROR"

의미:
2>&1 = stderr를 stdout과 같은 곳으로 보낸다.
| grep "ERROR" = 합쳐진 stdout을 grep의 stdin으로 넘긴다.

7. 이 명령어 전체를 네 말로 해석하면?

네 답:
app.py을 실행시키고 정상출력을 오른쪽으로 넘겨라 그럼 오른쪽에서 error가 있는 문장을 출력시킬거다

수정:
python으로 app.py를 실행하고, app.py의 stdout을 grep의 stdin으로 넘긴다. grep은 그중 "ERROR"가 포함된 줄만 출력한다.

### Final Correct Answer
1. | 는 왼쪽 명령어의 stdout을 오른쪽 명령어의 stdin으로 넘긴다.
2. python app.py의 stdout이 grep "ERROR"로 넘어간다.
3. 아니다. stderr는 자동으로 pipe를 타지 않는다.
4. 보인다.
5. grep 결과에는 안 보인다. 다만 stderr 자체가 터미널에 따로 보일 수는 있다.
6. python app.py 2>&1 | grep "ERROR"
7. python으로 app.py를 실행하고, app.py의 stdout을 grep의 stdin으로 넘겨서 "ERROR"가 포함된 줄만 출력한다.

### Key Point
- pipe | 는 stdout -> stdin 연결이다.
- 오른쪽 명령어는 입력을 stdin으로 받는다.
- pipe는 기본적으로 stderr를 넘기지 않는다.
- stderr는 터미널에 따로 보일 수 있지만 grep이 잡은 결과는 아니다.
- 2>&1은 stderr를 stdout으로 합치는 redirection이다.
- command 2>&1 | grep "ERROR"는 stdout과 stderr를 합쳐서 grep으로 넘긴다.

## Lec 02 - Q4. Environment Variable and PATH

### Problem
아래 상황을 보고 질문에 답해라.

터미널에서 다음 명령어를 실행했다.

export DATABASE_URL="mysql+aiomysql://user:pass@localhost/health"

그리고 Python 코드 안에서는 다음처럼 값을 읽는다.

DATABASE_URL = os.getenv("DATABASE_URL")

질문:

1. export DATABASE_URL=... 은 무엇을 하는 명령어인가?
2. DATABASE_URL은 코드 안에 직접 박아도 되는 값인가? 이유는?
3. os.getenv("DATABASE_URL")은 무엇을 하는 코드인가?
4. .env 파일과 export의 차이를 간단히 설명해라.
5. PATH 환경변수는 무엇을 위해 쓰이는가?
6. uvicorn을 쳤을 때 shell은 uvicorn 실행 파일을 어디서 찾는가?
7. command not found가 뜨는 대표적인 원인 2가지는?

### My Answer
1. key point에서는 shell과 child process가 본다네? 모르겠음
2. ㄴㄴ .env로 숨겨놔야함 데이터를 유출 문제때문에
3. 운영체제를 사용해 env 파일에 저장되있는 DATABASE_URL 을 가져옴
4. 몰라
5. 몰라
6. 몰라
7. 없거나 못찾거나

### Correction
1. export DATABASE_URL=... 은 무엇을 하는 명령어인가?

정답:
현재 shell 환경에 DATABASE_URL이라는 환경변수를 등록하고, 그 shell에서 실행되는 child process들도 그 값을 볼 수 있게 한다.

쉽게 말하면:
터미널 세션에 DATABASE_URL 값을 임시로 심어두는 것이다.

예:
export DATABASE_URL="mysql+aiomysql://user:pass@localhost/health"
python app.py

이렇게 하면 python app.py로 실행된 Python process는 DATABASE_URL 환경변수를 읽을 수 있다.

중요:
export는 .env 파일에 저장하는 게 아니다.
현재 터미널 세션의 환경에 넣는 것이다.

2. DATABASE_URL은 코드 안에 직접 박아도 되는 값인가? 이유는?

네 답:
ㄴㄴ .env로 숨겨놔야함 데이터를 유출 문제때문에

방향 맞음.

정답:
직접 박으면 안 된다. DB 주소, username, password 같은 민감정보가 코드에 들어가면 GitHub에 올라가거나 공유될 때 유출될 수 있다.

나쁜 예:
DATABASE_URL = "mysql+aiomysql://user:pass@localhost/health"

좋은 예:
DATABASE_URL = os.getenv("DATABASE_URL")

또는 pydantic-settings 같은 설정 관리 도구로 .env를 읽는다.

주의:
.env는 숨겨주는 마법 파일이 아니다.
.env도 GitHub에 올리면 똑같이 유출된다.
그래서 .gitignore에 .env를 넣어야 한다.

3. os.getenv("DATABASE_URL")은 무엇을 하는 코드인가?

네 답:
운영체제를 사용해 env 파일에 저장되있는 DATABASE_URL 을 가져옴

절반만 맞음.

수정:
os.getenv("DATABASE_URL")은 현재 process의 environment variable 중 DATABASE_URL 값을 읽는다.

중요:
os.getenv는 .env 파일을 직접 읽는 함수가 아니다.

os.getenv가 읽는 것:
현재 실행 중인 Python process가 가지고 있는 environment variable

.env 파일을 읽으려면 보통:
- python-dotenv
- pydantic-settings
- Docker Compose env_file
같은 도구가 먼저 .env 값을 environment variable로 로드해줘야 한다.

즉:
.env 파일 -> 로더가 읽음 -> environment variable로 주입 -> os.getenv가 읽음

4. .env 파일과 export의 차이를 간단히 설명해라.

정답:
.env는 환경변수를 파일로 저장해두는 방식이다.
export는 현재 shell 세션에 환경변수를 직접 등록하는 명령어다.

차이:
.env = 저장용 파일
export = 현재 shell에 즉시 등록

예:
.env 파일 안:
DATABASE_URL=mysql+aiomysql://user:pass@localhost/health

터미널에서 export:
export DATABASE_URL="mysql+aiomysql://user:pass@localhost/health"

.env는 파일이라 남아있다.
export는 현재 터미널 세션이 끝나면 보통 사라진다.

단, .zshrc나 .bashrc에 export를 적어두면 터미널 시작 때마다 자동 적용된다.

5. PATH 환경변수는 무엇을 위해 쓰이는가?

정답:
PATH는 shell이 실행 파일을 찾는 디렉토리 목록이다.

예:
python
uvicorn
git
docker

이런 명령어를 칠 때 shell은 PATH에 등록된 폴더들을 뒤져서 해당 실행 파일을 찾는다.

확인 명령어:
echo $PATH

6. uvicorn을 쳤을 때 shell은 uvicorn 실행 파일을 어디서 찾는가?

정답:
PATH에 등록된 디렉토리들에서 uvicorn이라는 실행 파일을 찾는다.

예:
uvicorn

이라고 치면 shell은 대략 이런 곳들을 뒤진다.

/usr/local/bin
/usr/bin
/bin
현재 venv/bin
...

가상환경을 켜면:
source venv/bin/activate

PATH 앞쪽에 venv/bin이 추가된다.
그래서 그 안의 uvicorn을 먼저 찾게 된다.

확인:
which uvicorn

7. command not found가 뜨는 대표적인 원인 2가지는?

네 답:
없거나 못찾거나

맞음. 더 정확히 쓰면:

정답:
1. 해당 프로그램이 설치되어 있지 않다.
2. 설치는 되어 있지만 실행 파일 위치가 PATH에 등록되어 있지 않다.

추가로 자주 있는 원인:
3. 가상환경에 설치했는데 venv를 activate하지 않았다.
4. 명령어 이름을 잘못 쳤다.

### Final Correct Answer
1. export DATABASE_URL=... 은 현재 shell 환경에 DATABASE_URL 환경변수를 등록하고, 그 shell에서 실행되는 child process들이 그 값을 볼 수 있게 한다.
2. 코드 안에 직접 박으면 안 된다. DB 비밀번호 같은 민감정보가 GitHub 등을 통해 유출될 수 있기 때문이다.
3. os.getenv("DATABASE_URL")은 현재 Python process의 environment variable에서 DATABASE_URL 값을 읽는다.
4. .env는 환경변수를 파일로 저장하는 방식이고, export는 현재 shell 세션에 환경변수를 직접 등록하는 명령어다.
5. PATH는 shell이 실행 파일을 찾을 때 확인하는 디렉토리 목록이다.
6. shell은 PATH에 등록된 디렉토리들에서 uvicorn 실행 파일을 찾는다.
7. command not found의 대표 원인은 프로그램이 설치되지 않았거나, 설치됐지만 PATH에서 찾을 수 없는 경우다.

### Key Point
- environment variable은 프로그램 실행 환경에 주입되는 설정값이다.
- export VAR=value는 현재 shell과 그 child process들이 VAR 값을 볼 수 있게 한다.
- child process는 현재 shell에서 실행된 프로그램이다. 예: python app.py, uvicorn main:app
- os.getenv("VAR")는 현재 process의 environment variable 값을 읽는다.
- os.getenv는 .env 파일을 직접 읽지 않는다.
- .env는 환경변수를 파일 형태로 저장하는 방식이다.
- .env를 실제 environment variable로 로드해주는 도구가 필요하다.
- PATH는 shell이 실행 파일을 찾는 디렉토리 목록이다.
- which uvicorn을 치면 실제 어떤 uvicorn이 실행되는지 확인할 수 있다.
- .env는 반드시 .gitignore에 넣어야 한다.

## Lec 02 - Q5. Exit Code, &&, ||

### Problem
아래 명령어들을 보고 질문에 답해라.

pytest && echo "tests passed"
pytest || echo "tests failed"

질문:

1. exit code에서 0은 무슨 의미인가?
2. exit code에서 non-zero는 무슨 의미인가?
3. echo $? 는 무엇을 확인하는 명령어인가?
4. pytest && echo "tests passed" 는 언제 echo가 실행되는가?
5. pytest || echo "tests failed" 는 언제 echo가 실행되는가?
6. FastAPI 프로젝트에서 pytest가 실패하면 GitHub Actions나 배포 과정에서 왜 문제가 되는가?
7. 이 개념을 네 말로 정리하면?

### My Answer
1. 0은 성공
2. 0이 아닌 모든것은 실패
3. 직전 명령어 실행후 exit code 출력
4. pytest 성공후
5. pytest 실패할때만
6. 진짜 서버 띄우고 했을때 이 오류가 날수있다는거지 뭐 코드 수정해야지
7. pytest로 확인을 잘 하고 서버를 운영하고 띄우자?

### Correction
1. exit code에서 0은 무슨 의미인가?

정답:
0은 성공을 의미한다.

맞음.

2. exit code에서 non-zero는 무슨 의미인가?

정답:
0이 아닌 값은 실패를 의미한다.

맞음.

3. echo $? 는 무엇을 확인하는 명령어인가?

정답:
직전 명령어의 exit code를 출력한다.

맞음.

예:
pytest
echo $?

pytest가 성공하면 보통 0이 나온다.
pytest가 실패하면 1 같은 non-zero 값이 나온다.

4. pytest && echo "tests passed" 는 언제 echo가 실행되는가?

정답:
pytest가 성공했을 때만 echo "tests passed"가 실행된다.

맞음.

5. pytest || echo "tests failed" 는 언제 echo가 실행되는가?

정답:
pytest가 실패했을 때만 echo "tests failed"가 실행된다.

맞음.

6. FastAPI 프로젝트에서 pytest가 실패하면 GitHub Actions나 배포 과정에서 왜 문제가 되는가?

네 답:
진짜 서버 띄우고 했을때 이 오류가 날수있다는거지 뭐 코드 수정해야지

방향은 맞음. 더 정확히는:

pytest가 실패하면 exit code가 non-zero가 된다.
GitHub Actions, Docker build script, 배포 script 같은 자동화 시스템은 이 exit code를 보고 작업 성공/실패를 판단한다.
따라서 pytest가 실패하면 CI pipeline이 실패 처리되고, 보통 다음 단계인 build/deploy가 중단된다.

즉:
테스트 실패 → exit code non-zero → CI 실패 → 배포 차단

이게 정상적인 구조다.
실패한 코드를 서버에 올리지 않기 위해서다.

7. 이 개념을 네 말로 정리하면?

네 답:
pytest로 확인을 잘 하고 서버를 운영하고 띄우자?

수정:
명령어는 실행 후 exit code를 남기고, shell과 CI/CD는 그 값을 기준으로 다음 명령어를 실행할지 말지 결정한다. 0이면 성공, non-zero면 실패다. &&는 성공했을 때 다음 명령어를 실행하고, ||는 실패했을 때 다음 명령어를 실행한다.

### Final Correct Answer
1. 0은 성공을 의미한다.
2. non-zero는 실패를 의미한다.
3. echo $? 는 직전 명령어의 exit code를 출력한다.
4. pytest && echo "tests passed" 에서 echo는 pytest가 성공했을 때만 실행된다.
5. pytest || echo "tests failed" 에서 echo는 pytest가 실패했을 때만 실행된다.
6. pytest가 실패하면 non-zero exit code가 나오고, GitHub Actions나 배포 pipeline은 이를 실패로 판단한다. 그래서 보통 build/deploy 단계가 중단된다.
7. 명령어는 실행 후 성공/실패를 exit code로 남긴다. shell과 CI/CD는 이 값을 기준으로 다음 작업을 계속할지 중단할지 결정한다.

### Key Point
- exit code 0 = 성공
- exit code non-zero = 실패
- echo $? = 직전 명령어의 exit code 확인
- A && B = A가 성공했을 때만 B 실행
- A || B = A가 실패했을 때만 B 실행
- pytest 실패 = non-zero exit code
- CI/CD는 exit code를 보고 성공/실패를 판단한다.
- 테스트 실패 시 배포를 막는 것은 정상이다. 망가진 코드를 서버에 올리지 않기 위한 안전장치다.

## Lec 02 - Q6. Process, PID, Signal

### Problem
아래 상황을 보고 질문에 답해라.

터미널에서 FastAPI 서버를 실행했다.

uvicorn main:app --reload

그런데 다른 터미널에서 다시 서버를 실행하려고 하니 아래 에러가 났다.

Address already in use

질문:

1. uvicorn main:app --reload를 실행하면 uvicorn은 무엇이 되는가?
2. PID는 무엇인가?
3. Address already in use는 보통 무슨 뜻인가?
4. 8000번 포트를 사용 중인 process를 찾는 명령어는?
5. process를 정상 종료 요청하는 명령어는?
6. Ctrl-C는 실행 중인 process에 어떤 signal을 보내는가?
7. kill -9를 처음부터 쓰는 것이 왜 좋지 않은가?

### My Answer
1. 코드 수정시 재시작 서버 띄우는거지 뭐
2. process ID
3. 다른 process에서 이미 이 포트를 사용중임
4. lsof -i :포트번호
5. kill term PID
6. SIGINT 즉 종료
7. 강제종료라서 뭐가 문제인지 파악못하고 걍 바로 끄는거라서 급할때만 써야지

### Correction
1. uvicorn main:app --reload를 실행하면 uvicorn은 무엇이 되는가?

네 답:
코드 수정시 재시작 서버 띄우는거지 뭐

수정:
uvicorn main:app --reload를 실행하면 uvicorn 프로그램이 실행 중인 process가 된다.

정답:
실행 중인 프로그램, 즉 process가 된다.

추가 설명:
--reload는 코드 변경 시 자동 재시작하는 옵션이고, 이 질문의 핵심은 “실행된 프로그램은 process가 된다”는 점이다.

2. PID는 무엇인가?

네 답:
process ID

정답.

PID = Process ID
운영체제가 실행 중인 process를 구분하기 위해 붙이는 번호다.

3. Address already in use는 보통 무슨 뜻인가?

네 답:
다른 process에서 이미 이 포트를 사용중임

정답.

정확히는:
해당 address/port 조합을 이미 다른 process가 사용 중이라는 뜻이다.
FastAPI에서는 보통 8000번 포트를 이미 기존 uvicorn process가 쓰고 있을 때 발생한다.

4. 8000번 포트를 사용 중인 process를 찾는 명령어는?

네 답:
lsof -i :포트번호

정답.

8000번이면:
lsof -i :8000

lsof = list open files
-i = internet/network 관련 열린 파일/소켓을 보겠다는 옵션
:8000 = 8000번 포트

5. process를 정상 종료 요청하는 명령어는?

네 답:
kill term PID

방향은 맞는데 문법 수정 필요.

정답:
kill -TERM <PID>

예:
kill -TERM 12345

보통 아래처럼 짧게도 가능하다:
kill 12345

기본 signal이 TERM인 경우가 많기 때문이다.
하지만 명시적으로 쓰면:
kill -TERM 12345

6. Ctrl-C는 실행 중인 process에 어떤 signal을 보내는가?

네 답:
SIGINT 즉 종료

거의 맞음. 단, “종료”라기보다 “interrupt signal”이다.

정답:
Ctrl-C는 보통 foreground process에 SIGINT를 보낸다.

SIGINT = Signal Interrupt

의미:
실행 중인 process에게 중단 요청을 보낸다.
대부분의 프로그램은 SIGINT를 받으면 종료하지만, 엄밀히는 강제 종료가 아니라 interrupt 요청이다.

7. kill -9를 처음부터 쓰는 것이 왜 좋지 않은가?

네 답:
강제종료라서 뭐가 문제인지 파악못하고 걍 바로 끄는거라서 급할때만 써야지

방향 맞음. 더 정확히는:

kill -9는 SIGKILL을 보내는 강제 종료다.
process가 cleanup할 기회를 받지 못한다.
그래서 파일 저장, DB 연결 종료, lock 해제, child process 정리 같은 작업을 못 하고 죽을 수 있다.

정답:
kill -9는 process를 즉시 강제 종료하므로 graceful shutdown이 불가능하다. 리소스 정리, 파일/DB 연결 정리, lock 해제 등을 못 할 수 있으므로 처음부터 쓰면 좋지 않다. 먼저 kill -TERM을 쓰고, 그래도 안 죽을 때 마지막 수단으로 쓴다.

### Final Correct Answer
1. uvicorn은 실행 중인 program, 즉 process가 된다.
2. PID는 Process ID로, 운영체제가 process를 구분하기 위해 붙이는 번호다.
3. Address already in use는 해당 포트를 다른 process가 이미 사용 중이라는 뜻이다.
4. lsof -i :8000
5. kill -TERM \<PID>
6. Ctrl-C는 보통 SIGINT, 즉 interrupt signal을 보낸다.
7. kill -9는 SIGKILL 강제 종료라서 process가 cleanup할 기회를 받지 못한다. 그래서 처음부터 쓰지 말고 kill -TERM 후에도 안 죽을 때 마지막 수단으로 쓴다.

### Key Point
- 실행 중인 프로그램은 process다.
- PID = Process ID
- Address already in use = 해당 port를 이미 다른 process가 사용 중
- lsof = list open files
- lsof -i :8000 = 8000번 포트를 쓰는 process 확인
- -i = internet/network 관련 항목 확인
- kill -TERM \<PID> = 정상 종료 요청
- Ctrl-C = SIGINT, interrupt 요청
- SIGINT = Signal Interrupt
- kill -9 = SIGKILL, 강제 종료
- SIGKILL은 cleanup 기회를 주지 않기 때문에 마지막 수단이다.

## Lec 02 - Q7. Job Control: Ctrl-Z, jobs, bg, fg

### Problem
터미널에서 아래 명령어를 실행했다고 하자.

sleep 1000

그 다음 Ctrl-Z를 눌렀다.

질문:

1. Ctrl-Z는 process를 완전히 종료하는가, 아니면 일시정지하는가?
2. Ctrl-Z가 보내는 signal은 무엇인가?
3. 현재 shell의 job 목록을 확인하는 명령어는?
4. 일시정지된 job을 background에서 계속 실행시키는 명령어는?
5. background job을 다시 foreground로 가져오는 명령어는?
6. 처음부터 background에서 실행하려면 명령어 뒤에 무엇을 붙이는가?
7. sleep 1000 & 는 무슨 의미인가?

### My Answer
1. 일시정지만함
2. SIGSTP
3. jobs
4. bg
5. fg
6. &
7. sleep 1000을 백그라운드에서 실행해라

### Correction
1. Ctrl-Z는 process를 완전히 종료하는가, 아니면 일시정지하는가?

정답:
일시정지한다.

맞음.

2. Ctrl-Z가 보내는 signal은 무엇인가?

네 답:
SIGSTP

수정:
정확한 이름은 보통 SIGTSTP다.

정답:
SIGTSTP

의미:
terminal stop signal. 터미널에서 실행 중인 foreground process를 일시정지시키는 signal이다.

주의:
SIGSTOP이라는 signal도 있다.
SIGSTOP은 process를 강제로 stop시키며 process가 무시할 수 없다.
Ctrl-Z는 일반적으로 SIGTSTP를 보낸다.

3. 현재 shell의 job 목록을 확인하는 명령어는?

정답:
jobs

맞음.

4. 일시정지된 job을 background에서 계속 실행시키는 명령어는?

정답:
bg

맞음.

5. background job을 다시 foreground로 가져오는 명령어는?

정답:
fg

맞음.

6. 처음부터 background에서 실행하려면 명령어 뒤에 무엇을 붙이는가?

정답:
&

맞음.

7. sleep 1000 & 는 무슨 의미인가?

정답:
sleep 1000을 background에서 실행한다.

맞음.

### Final Correct Answer
1. 일시정지한다.
2. SIGTSTP
3. jobs
4. bg
5. fg
6. &
7. sleep 1000을 background에서 실행한다.

### Key Point
- Ctrl-Z는 종료가 아니라 일시정지다.
- Ctrl-Z는 보통 SIGTSTP를 보낸다.
- SIGTSTP = terminal stop signal
- Ctrl-C는 SIGINT다.
- Ctrl-Z는 SIGTSTP다.
- jobs는 현재 shell의 job 목록을 보여준다.
- bg는 stopped job을 background에서 계속 실행한다.
- fg는 job을 foreground로 가져온다.
- &는 처음부터 background 실행을 의미한다.
- sleep 1000 & 는 sleep 1000을 background에서 실행한다는 뜻이다.

## Lec 02 - Q8. SSH Basics: local vs remote

### Problem
아래 명령어를 보고 질문에 답해라.

ssh ubuntu@12.34.56.78

질문:

1. ssh는 무엇을 하기 위한 명령어인가?
2. ubuntu는 무엇을 의미하는가?
3. 12.34.56.78은 무엇을 의미하는가?
4. 이 명령어가 성공하면 너는 local 컴퓨터에 있는가, remote 서버에 들어간 것인가?
5. SSH 접속 후에 pwd, ls, cat을 실행하면 어느 컴퓨터의 파일을 보는 것인가?
6. ssh -i key.pem ubuntu@12.34.56.78 에서 -i key.pem은 무엇을 의미하는가?
7. private key 파일인 key.pem을 GitHub에 올리면 왜 위험한가?
8. 이 명령어 전체를 네 말로 해석하면?

### My Answer
1. remote 서버에서 실행하기 위해서
2. remote server 이름
3. 우분서 서버 IP
4. 리모트 서버로 들어간거지
5. 리모트 서버 컴터 파일 보는거임
6. 집 열쇠마냥 인증하고 들어가는거지
7. 우분투 서버의 권한을 누구든 가질수있어서
8. 우분투 서버 접속 서버 ip는 12.34.56.78

### Correction
1. ssh는 무엇을 하기 위한 명령어인가?

네 답:
remote 서버에서 실행하기 위해서

거의 맞음.

정답:
SSH는 remote server에 안전하게 접속해서 그 서버에서 명령어를 실행하기 위한 명령어/프로토콜이다.

즉:
내 컴퓨터 터미널에서 원격 서버의 shell에 들어가는 방식이다.

2. ubuntu는 무엇을 의미하는가?

네 답:
remote server 이름

수정:
ubuntu는 서버 이름이 아니라 remote server에 있는 username이다.

정답:
ubuntu는 remote server에 로그인할 사용자 계정 이름이다.

예:
ssh ubuntu@12.34.56.78

의미:
12.34.56.78 서버에 ubuntu 유저로 접속한다.

AWS EC2에서 Ubuntu 이미지를 쓰면 기본 유저가 ubuntu인 경우가 많다.

3. 12.34.56.78은 무엇을 의미하는가?

네 답:
우분서 서버 IP

맞음.

정답:
12.34.56.78은 remote server의 IP address다.

4. 이 명령어가 성공하면 너는 local 컴퓨터에 있는가, remote 서버에 들어간 것인가?

정답:
remote server에 들어간 것이다.

맞음.

주의:
물리적으로 네 컴퓨터를 쓰고 있지만, 그 터미널 세션에서 실행하는 명령어는 remote server에서 실행된다.

5. SSH 접속 후에 pwd, ls, cat을 실행하면 어느 컴퓨터의 파일을 보는 것인가?

정답:
remote server의 파일을 보는 것이다.

맞음.

예:
ssh 접속 후 cat .env를 하면 local Mac의 .env가 아니라 remote server의 .env를 보는 것이다.

6. ssh -i key.pem ubuntu@12.34.56.78 에서 -i key.pem은 무엇을 의미하는가?

네 답:
집 열쇠마냥 인증하고 들어가는거지

방향 맞음.

정답:
-i key.pem은 SSH 인증에 사용할 private key 파일을 지정하는 옵션이다.

즉:
비밀번호 대신 key.pem이라는 private key로 인증해서 ubuntu 계정으로 서버에 접속한다.

7. private key 파일인 key.pem을 GitHub에 올리면 왜 위험한가?

네 답:
우분투 서버의 권한을 누구든 가질수있어서

맞음.

더 정확히:
private key가 유출되면 해당 key를 가진 사람이 서버에 접속할 수 있다. 서버 안의 코드, DB 설정, .env, API key, 로그 등에 접근할 수 있으므로 치명적이다.

8. 이 명령어 전체를 네 말로 해석하면?

네 답:
우분투 서버 접속 서버 ip는 12.34.56.78

수정:
12.34.56.78이라는 IP 주소를 가진 remote server에 ubuntu 사용자로 SSH 접속한다.

### Final Correct Answer
1. ssh는 remote server에 안전하게 접속해서 그 서버에서 명령어를 실행하기 위한 명령어다.
2. ubuntu는 remote server에 로그인할 username이다.
3. 12.34.56.78은 remote server의 IP address다.
4. remote server에 들어간 것이다.
5. remote server의 파일을 보는 것이다.
6. -i key.pem은 SSH 인증에 사용할 private key 파일을 지정하는 옵션이다.
7. key.pem이 유출되면 다른 사람이 서버에 접속할 수 있어서 위험하다.
8. 12.34.56.78 서버에 ubuntu 유저로 SSH 접속한다.

### Key Point
- SSH는 remote machine에 안전하게 접속하기 위한 방식이다.
- ubuntu@12.34.56.78에서 ubuntu는 username이다.
- 12.34.56.78은 remote server의 IP address다.
- SSH 접속 후 실행하는 명령어는 remote server에서 실행된다.
- local과 remote를 구분해야 한다.
- -i key.pem은 private key 파일을 인증에 사용한다는 뜻이다.
- private key는 서버 접속 열쇠다.
- key.pem, .env, API key, DB password는 GitHub에 올리면 안 된다.

## Lec 02 - Q9. Final Review: CLI Environment Scenario

### Problem
FastAPI 프로젝트를 EC2 서버에 배포한다고 하자.

상황:
- local 컴퓨터에서 SSH로 remote server에 접속한다.
- remote server에서 프로젝트 폴더로 이동한다.
- .env 파일이 있는지 확인한다.
- uvicorn 서버를 실행한다.
- 8000번 포트가 이미 사용 중이면 해당 process를 찾아 종료한다.
- 서버 로그에서 ERROR가 들어간 줄만 찾는다.

아래 작업을 하기 위한 명령어 또는 개념을 각각 써라.

1. 12.34.56.78 서버에 ubuntu 유저로 SSH 접속
2. key.pem private key를 사용해서 SSH 접속
3. 현재 remote server에서 내 위치 확인
4. 숨김 파일까지 자세히 보기
5. .env 파일 내용 확인
6. uvicorn으로 main.py 안의 app 객체를 0.0.0.0:8000에서 실행
7. 8000번 포트를 사용 중인 process 찾기
8. PID가 12345인 process에 정상 종료 요청 보내기
9. 서버 실행 중 Ctrl-C를 누르면 어떤 signal이 가는가?
10. 로그 파일 app.log에서 ERROR 줄만 출력
11. app.log의 ERROR 줄만 errors.txt에 저장
12. 이 전체 흐름에서 local과 remote를 헷갈리면 어떤 문제가 생기는가?

### My Answer
1. ssh ubuntu@12.34.56.78
2. ssh -i key.pem ubuntu@12.34.56.78
3. pwd
4. ls -al or -la
5. cat .env
6. uvicorn main:app --reload --host 0.0.0.0 port 8000
7. lsof -i 8000
8. kill TERM 12345
9. SIGTSTP
10. grep "ERROR" app.log > errors.txt
11. 생략
12. ssh는 리모트 서버에서만 가능하니

### Correction
1. 12.34.56.78 서버에 ubuntu 유저로 SSH 접속

정답:
ssh ubuntu@12.34.56.78

맞음.

의미:
12.34.56.78 IP를 가진 remote server에 ubuntu 유저로 접속한다.

2. key.pem private key를 사용해서 SSH 접속

정답:
ssh -i key.pem ubuntu@12.34.56.78

맞음.

의미:
key.pem private key를 인증에 사용해서 remote server에 접속한다.

3. 현재 remote server에서 내 위치 확인

정답:
pwd

맞음.

주의:
SSH 접속 후 pwd를 치면 local Mac의 위치가 아니라 remote server 안에서의 현재 위치를 보여준다.

4. 숨김 파일까지 자세히 보기

정답:
ls -al

또는:
ls -la

맞음.

5. .env 파일 내용 확인

정답:
cat .env

맞음.

주의:
.env는 민감정보가 들어 있을 수 있으므로 확인은 가능하지만 GitHub에 올리면 안 된다.

6. uvicorn으로 main.py 안의 app 객체를 0.0.0.0:8000에서 실행

네 답:
uvicorn main:app --reload --host 0.0.0.0 port 8000

수정:
--port에서 --가 빠졌다.

정답:
uvicorn main:app --host 0.0.0.0 --port 8000

개발 중이면 아래도 가능:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

다만 서버/배포 환경에서는 보통 --reload를 쓰지 않는다.
--reload는 코드 변경 시 자동 재시작하는 개발용 옵션이다.

7. 8000번 포트를 사용 중인 process 찾기

네 답:
lsof -i 8000

수정:
포트 번호 앞에 :가 필요하다.

정답:
lsof -i :8000

의미:
8000번 포트를 사용 중인 process를 찾는다.

8. PID가 12345인 process에 정상 종료 요청 보내기

네 답:
kill TERM 12345

수정:
TERM 앞에 -가 필요하다.

정답:
kill -TERM 12345

또는 보통:
kill 12345

하지만 명시적으로 쓰려면 kill -TERM 12345가 좋다.

9. 서버 실행 중 Ctrl-C를 누르면 어떤 signal이 가는가?

네 답:
SIGTSTP

수정:
Ctrl-C는 SIGINT다.
Ctrl-Z가 SIGTSTP다.

정답:
SIGINT

정리:
Ctrl-C = SIGINT = interrupt 요청
Ctrl-Z = SIGTSTP = 일시정지 요청

10. 로그 파일 app.log에서 ERROR 줄만 출력

네 답:
grep "ERROR" app.log > errors.txt

수정:
이건 출력이 아니라 파일 저장이다.

정답:
grep "ERROR" app.log

11. app.log의 ERROR 줄만 errors.txt에 저장

정답:
grep "ERROR" app.log > errors.txt

네가 10번에 쓴 답이 사실은 11번 정답이다.

12. 이 전체 흐름에서 local과 remote를 헷갈리면 어떤 문제가 생기는가?

네 답:
ssh는 리모트 서버에서만 가능하니

수정:
SSH는 local에서 remote server로 접속할 때 쓰는 것이다.
SSH 접속 전에는 local에서 명령어를 실행하고, SSH 접속 후에는 remote server에서 명령어를 실행한다.

local과 remote를 헷갈리면:
- local 프로젝트 폴더에서 작업한다고 생각했는데 remote server 파일을 수정할 수 있다.
- remote server의 .env를 봐야 하는데 local .env를 보고 착각할 수 있다.
- remote에서 서버를 띄워야 하는데 local에서 uvicorn을 실행할 수 있다.
- remote 포트 문제를 봐야 하는데 local 포트만 확인할 수 있다.
- 배포 서버에는 코드가 없는데 local에만 코드가 있는 상태로 착각할 수 있다.

즉:
어느 컴퓨터에서 명령어가 실행되는지 헷갈리면 배포, 디버깅, 파일 수정이 전부 꼬인다.

### Final Correct Answer
1. ssh ubuntu@12.34.56.78
2. ssh -i key.pem ubuntu@12.34.56.78
3. pwd
4. ls -al 또는 ls -la
5. cat .env
6. uvicorn main:app --host 0.0.0.0 --port 8000
   개발 중이면: uvicorn main:app --reload --host 0.0.0.0 --port 8000
7. lsof -i :8000
8. kill -TERM 12345
9. SIGINT
10. grep "ERROR" app.log
11. grep "ERROR" app.log > errors.txt
12. SSH 접속 전 명령어는 local에서 실행되고, SSH 접속 후 명령어는 remote server에서 실행된다. 이걸 헷갈리면 local 파일과 remote 파일, local 포트와 remote 포트, local 서버와 remote 서버를 착각해서 배포와 디버깅이 꼬인다.

### Key Point
- ssh user@host = remote server에 user로 접속
- ssh -i key.pem user@host = private key를 사용해서 접속
- SSH 접속 후 명령어는 remote server에서 실행된다.
- pwd = 현재 위치 확인
- ls -la = 숨김 파일 포함 자세히 보기
- cat .env = .env 내용 확인
- uvicorn main:app --host 0.0.0.0 --port 8000 = main.py의 app 객체를 모든 네트워크 인터페이스의 8000번 포트에서 실행
- --reload는 개발용 옵션이다.
- lsof -i :8000 = 8000번 포트를 쓰는 process 확인
- kill -TERM PID = 정상 종료 요청
- Ctrl-C = SIGINT
- Ctrl-Z = SIGTSTP
- grep "ERROR" app.log = ERROR 줄 출력
- grep "ERROR" app.log > errors.txt = ERROR 줄을 파일에 저장