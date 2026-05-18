## Command Line Environment

Command-line environment = shell에서 프로그램을 실행하고, 입출력, 환경변수, return code, signal, remote machine 등을 제어하는 환경.

## ARGUMENTS

### - (short option) vs -- (long option)

- short option - can be combined
- long option - more readable

### { } - brace expansion
- 여러 파일을 한번에 만들때 사용
- touch file{1,2,3}.txt = touch file1.txt file2.txt file3.txt

### * - glob wildcard
- 아무 문자열 0개 이상과 매칭

```bash
main.py
models.py
run.sh
README.md
data.csv

ls *.py = ls main.py models.py

결과:
main.py
models.py
```

### ** - recursive glob
- 현재 폴더 + 하위 폴더까지 재귀적으로 매칭
```bash
project/
├── main.py
├── app/
│   ├── models.py
│   └── routes.py
└── tests/
    └── test_records.py

ls **/*.py

결과:
app/models.py
app/routes.py
tests/test_records.py
```

## STREAM

### stdout / stderr
- stdout = 정상 출력
- stderr = 에러 출력

### > and >>
- \>  = 덮어쓰기 / stdout 저장
- \>> = 뒤에 추가하기 / stdout 저장

### 2> - stderr 저장
- stderr를 파일에 저장

### |
- 왼쪽 명령어의 stdout을 오른쪽 명령어의 stdin으로 넘김

## ENVIRONMENT VARIABLES

### $ 
- 변수 값(variable)을 꺼낼 때 씀

## RETURN CODES
- 0      = 성공
- non-0  = 실패

### && and ||
- && - execute when previous one success
- || - execute when previous one fail

```bash
-q = --quiet

grep -q 1 numbers.txt && echo "Pattern Found"

grep -q "a" numbers.txt || echo "Pattern Not Found"
```

## Signals

### ^C
- Sends SIGINT.
- SIGINT = Signal Interrupt.
- It asks the foreground process to interrupt/stop.
- Most programs terminate when they receive SIGINT, but technically it is an interrupt request, not the same as forced kill.

### ^Z
- Sends SIGTSTP.
- SIGTSTP = terminal stop signal.
- It pauses/suspends the foreground process.
- It does not fully terminate the process.

### jobs
- Shows the current shell's job list.
- It shows jobs started from the current shell, especially stopped/background jobs.
- It is not the same as showing all system processes.

### kill
- Sends a signal to a process by PID.
- Despite the name, kill does not always mean “kill immediately.”
```bash
- Example:
  - kill -TERM PID = request normal termination
  - kill -KILL PID or kill -9 PID = force kill
  - kill -INT PID = send SIGINT
  - kill -TSTP PID = send stop/suspend signal
  ```

## REMOTE MACHINE

Remote Server not in personal computer

### ssh
- ssh example@server.address

### ssh key - private/public key

- authorize without passwords

```bash
ls ~/.ssh - 키 보여줌

cd ~/.ssh - ssh로 이동
cat pem key - 키보여줌

로그인:

ssh -i ~/.ssh/key_name example@server_address

```

## TERMINAL MULTIPLEXERS
- 터미널 세션을 여러 개로 나누고, 끊겨도 유지하게 해주는 도구

### tmux
- Ctrl-b c - create new window
- Ctrl-b d   = detach
- tmux attach - checking the session
- tmux new -s deploy - 새 session 만들기
- tmux ls - session 목록 보기
- tmux attach -t deploy - session에 다시 들어가기
- Ctrl-b 누르고 d - session에서 빠져나오기, 종료 아님
- exit - 종료

## CUSTOMIZING YOUR SHELL

Shell customization = 터미널을 내 작업 방식에 맞게 설정하는 것.

### 설정 파일

- macOS zsh: `~/.zshrc`
- bash: `~/.bashrc`

수정 후 적용:

```bash
source ~/.zshrc
```

### Alias

긴 명령어를 짧게 줄이는 별명.

```bash
alias ll="ls -la"
alias gs="git status"
alias act="source venv/bin/activate"
```

### PATH

Shell이 실행 파일을 찾는 경로 목록.

```bash
echo $PATH
which python
which uvicorn
```

### Environment Variable

프로그램이 읽는 설정값.

```bash
export EDITOR="code"
```

주의: `DATABASE_URL`, `API_KEY` 같은 secret은 `.zshrc`에 넣지 않는 게 안전하다.

### Function

여러 명령어를 하나로 묶는 것.

```bash
mkcd() {
  mkdir -p "$1"
  cd "$1"
}
```

### 핵심 정리

- `.zshrc` / `.bashrc` = shell 설정 파일
- `alias` = 명령어 별명
- `PATH` = 실행 파일 검색 경로
- `export` = 환경변수 설정
- `source ~/.zshrc` = 설정 다시 적용
- 너무 많이 커스터마이징하면 오히려 헷갈릴 수 있음

## AI IN THE SHELL


AI in the shell = 터미널 작업 중 AI를 보조 도구로 사용하는 것.

### 대표 용도

1. 명령어 생성
- “현재 폴더 아래 모든 .log 파일에서 ERROR 찾는 명령어”
- 결과: `grep -r "ERROR" . --include="*.log"`

2. 에러 설명
- Docker, Python, Git 에러 메시지를 붙여넣고 원인 분석

3. 로그 요약
- 긴 서버 로그에서 핵심 에러만 요약

4. Shell script 작성 보조
- 반복 작업을 자동화하는 bash script 초안 생성

5. 명령어 옵션 설명
- `tar -xzvf`, `rsync -avz`, `find . -name "*.py"` 같은 명령어 해석

## One-line Mental Model

Command-line environment는 프로그램을 argument/flag로 실행하고, stdout/stderr로 출력하고, environment variable을 읽고, return code로 성공/실패를 남기고, process/signal로 제어하는 환경이다.










