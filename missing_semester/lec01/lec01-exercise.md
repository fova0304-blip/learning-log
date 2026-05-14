# Lec 1: Shell - Exercises

## Exercise 1: ls -l flag
What does the -l flag to ls do? Run ls -l / and examine the output. What do the first 10 characters of each line mean? (Hint: man ls)

`ls -l`의 `-l` 플래그는 뭘 하나? `ls -l /` 실행해서 출력 확인.
각 줄의 첫 10글자는 무슨 의미? (Hint: `man ls`) 

### 시도
ls - list down contents

-l - List files in the long format

### 결과
ls -l: 
list down content with in long format

List the contents of the current working directory in long format

### 막힌 거
man ls 사용후 나가는데 :q 써야함

각 줄의 첫 10글자는 무슨 의미?:

-rwxr-xr-x에서 첫 글자는 파일 종류, 뒤 9글자는 owner/group/others의 rwx 권한.


## Exercise 2: Glob
In the command find ~/Downloads -type f -name "*.zip" -mtime +30, the *.zip is a “glob”. What is a glob? Create a test directory with some files and experiment with patterns like ls *.txt, ls file?.txt, and ls {a,b,c}.txt. See Pattern Matching in the Bash manual.[https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html]

`find ~/Downloads -type f -name "*.zip"` 에서 `*.zip`이 "glob".

glob이 뭔가? 테스트 폴더 만들어서 패턴 실험:
`ls *.txt`, `ls file?.txt`, `ls {a,b,c}.txt`

### 시도
ls *.txt  
cbt_history_20260303_1445.txt

ls file?.txt  
zsh: no matches found: file?.txt

ls {a,b,c}.txt

ls: a.txt: No such file or directory

ls: b.txt: No such file or directory

ls: c.txt: No such file or directory

### 결과
glob은 trying to find file that matches the character in certain patterns

더 정확한 답변:
```
Glob is a pattern syntax the shell uses to match filenames. Before running a command, the shell expands the pattern into a list of matching filenames
```

### 막힌 거
[https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html] 를 참고함

## Exercise 3: Quotes
What’s the difference between 'single quotes', "double quotes", and \$'ANSI quotes'? Write a command that echoes a string containing a literal $, a !, and a newline character. See Quoting.

`'작은따옴표'`, `"큰따옴표"`, `$'ANSI 따옴표'` 차이는?
literal `$`, `!`, 개행문자를 포함한 문자열을 echo 하는 명령 작성.

### 시도
echo 'single $quote'
single $quote

echo "single $quote"
single 

echo $'ANSI quotes'
ANSI quotes

echo a'ANSI quotes'
aANSI quotes

echo !'ANSI quotes'
!ANSI quotes

### 결과
"" - include literal such as $
'' - ignore literal such as $

고친거:

" " - doesn't treat $ literally, allows variable expansion

' ' - does treat $ literally, no variable expansion

### 막힌 거
처음에는 반대로씀 그래서 고침


## Exercise 4: Standard streams
The shell has three standard streams: stdin (0), stdout (1), and stderr (2). Run ls /nonexistent /tmp and redirect stdout to one file and stderr to another. How would you redirect both to the same file? See Redirections.

셸의 3개 표준 스트림: stdin(0), stdout(1), stderr(2).
`ls /nonexistent /tmp` 실행해서 stdout은 한 파일에, stderr는 다른 파일에 리다이렉트.
둘 다 같은 파일로 보내려면?

### 시도
ls /nonexistent /tmp 후 결과 출력:

ls: /nonexistent: No such file or directory

/tmp: claude-501

stderr - 에러출력
stdout - 정상출력

그러니 에러출력은 따로 에러출력.txt로
정상출력은 따로 정상출력.txt로 

### 결과
stdout / stderr 다른 파일로 보내기:

ls /nonexistent /tmp > 정상출력.txt 2> 에러출력.txt

같은파일로 보내기:
ls /nonexistent /tmp > 모든출력.txt 2>&1

2>&1은 stderr를 stdout이 현재 가고있는곳으로 보내라 

### 막힌 거
리다이렉션 문법:
명령어 > 정상출력파일
명령어 2> 에러출력파일
이걸 몰랐음


## Exercise 5: Exit status & && ||
$? holds the exit status of the last command (0 = success). && runs the next command only if the previous succeeded; || runs it only if the previous failed. Write a one-liner that creates /tmp/mydir only if it doesn’t already exist. See Exit Status.

`$?`는 마지막 명령의 exit status (0 = 성공).
`&&`는 이전 성공시만, `||`는 이전 실패시만 다음 실행.
`/tmp/mydir`이 없을 때만 생성하는 한 줄 작성.

### 시도
1 trial:

/tmp/mydir $? = 0 && touch /tmp/mydir || touch /tmp/mydir

2 trial:

if /tmp/mydir $? = 0; then echo "yes"; else echo "no"; fi

3 trial
/tmp ls -l grep mydir && mkdir /tmp/mydir

4 trial
ls /tmp/mydir || mkdir /tmp/mydir

ls /tmp/mydir 해봐 실패하면 만들어 /tmp/mydir

### 결과
ls /tmp/mydir || mkdir /tmp/mydir

or

test -d /tmp/mydir || mkdir /tmp/mydir
### 막힌 거
코덱스 피셜:
/tmp/mydir이 있는지 확인하려면 test, [ ... ], 또는 ls 같은 명령어가 필요해요

어떤_명령어 || mkdir /tmp/mydir

더 정확한 답은 디렉토리 존재 여부까지 파악해야하기때문에
test -d를 사용하는게 맞음

test -d /tmp/mydir || mkdir /tmp/mydir

## Exercise 7: File check script
Write a script that takes a filename as an argument ($1) and checks whether the file exists using test -f or [ -f ... ]. It should print different messages depending on whether the file exists. See Bash Conditional Expressions.

파일명을 인자(`$1`)로 받아서 `test -f` 또는 `[ -f ... ]`로
파일 존재 여부 확인. 존재 여부에 따라 다른 메시지 출력.

### 시도
if test -f dsa; then echo "file exist"; else echo "file does not exist";  fi

output : file does not exist

takes a filename as an argument $1

if test -f $1; then echo "file exists"; else echo "file does not exist";  fi

output : file exists

### 결과
if test -f $1; then echo "file exists"; else echo "file does not exist";  fi
대신 "$1"을 감싸는게 더 좋음

### 막힌 거
takes a filename as an argument $1을 까먹음



## Exercise 8: chmod +x
Save the script from the previous exercise to a file (e.g., check.sh). Try running it with ./check.sh somefile. What happens? Now run chmod +x check.sh and try again. Why is this step necessary? (Hint: look at ls -l check.sh before and after the chmod.)

Exercise 7 스크립트를 `check.sh`로 저장.
`./check.sh somefile` 실행 → 어떻게 됨?
`chmod +x check.sh` 후 다시 → 왜 이 단계가 필요?
(Hint: chmod 전후로 `ls -l check.sh` 비교)

### 시도
아예 이해를 못했음

### 결과
chmod +x check.sh 권한 부여 이후:

-rwxr-xr-x@ 1 admin  staff  86  5월 14 18:29 check.sh

### 막힌 거
1. check.sh 파일을 만들고
2. ls -l check.sh 실행함 - 실행권한(x) 없음 

- -rw-r--r--@ 1 admin  staff  86  5월 14 18:29 check.sh

3. chmod +x check.sh 권한 부여

4. ls -l check.sh 실행함 - 권한 있음 
- -rwxr-xr-x@ 1 admin  staff  86  5월 14 18:29 check.sh


## Exercise 10: Date backup
Write a command that copies a file to a backup with today’s date in the filename (e.g., notes.txt → notes_2026-01-12.txt). (Hint: $(date +%Y-%m-%d)). See Command Substitution.

파일을 오늘 날짜가 들어간 백업 파일로 복사하는 명령 작성.
(예: notes.txt → notes_2026-01-12.txt)
(Hint: `$(date +%Y-%m-%d)`)

### 시도
$(date +%Y-%m-%d) > notes.txt
zsh: command not found: 2026-05-14

echo $(date +%Y-%m-%d) > notes.txt
만들어짐

대신 문제에서는 txt파일의 이름을 이렇게 만들라고 해서:

cp notes.txt notes_$(date +%Y-%m-%d).txt

cp stands for copy

복사를 하고 이름만 바꿔서 똑같은 파일 만드는거임

## 결과
cp notes.txt notes_$(date +%Y-%m-%d).txt

notes.txt 복사후 이름을 따로 지어줌

notes_2026-05-14.txt로

### 막힌 거
$(date +%Y-%m-%d) 출력하는 명령이 아님 그래서 echo를 추가해줘야함

## Exercise 12: Pipes - top 5 extensions
Use pipes to find the 5 most common file extensions in your home directory. (Hint: combine find, grep or sed or awk, sort, uniq -c, and head.)

파이프를 써서 홈 디렉토리에서 가장 흔한 파일 확장자 5개 찾기.
(Hint: find, grep/sed/awk, sort, uniq -c, head 조합)

### 시도

find . -name "*.py" - 실패 / 의도가 다름

홈 디렉토리의 모든 파일을 찾고

find ~ -type f  |

각 파일명에서 확장자만 뽑고,

awk -F. 'NF>1 {print $NF}' |

확장자를 정렬하고,

sort |

같은 확장자 개수를 세고,

uniq -c |

많은 순으로 정렬하고,

sort -nr |

상위 5개만 출력한다.

head -5

### 결과

find ~ -type f |
awk -F. 'NF>1 {print $NF}' |
sort |
uniq -c |
sort -nr |
head -5

### 막힌 거
extension의 정의를 잘 몰랐음- 파이썬 자바 pdf 등등임

처음에는 특정 확장자 하나를 찾는 문제로 이해했는데,
실제로는 모든 파일의 확장자를 세고 top 5를 구하는 문제였음.


