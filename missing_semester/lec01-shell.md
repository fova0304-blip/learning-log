# Lec 1: Course Overview + Shell

**Source:** https://missing.csail.mit.edu/2026/course-shell/

## Notes
(영상 보면서 핵심만 짧게)
shell - interface with computer with texts
Inside of Terminal, run shell
Shell- bash in Linux, but for Mac, Zsh is used these days
Zsh- easier to interface with
Bash and Zsh

shell- automate, programming language, combine programs, interact with opensource,
configuring

## Commands
(새로 본 명령어 + 한 줄 설명)
date - 날짜 출력


## ""
- echo "xxx" - 변수확장

name = "Minseo"
echo "Hello $name" -> Hello Minseo

example(변수 쓸때):
echo "Hello $USER, today is $(date)"
filename="my file.txt"
cat "$filename"          # 공백 있어서 따옴표 필요


## ''
- echo "xxx" - 변수확장X, 전부 문자 그대로

name="민서"
echo 'Hello $name' -> Hello $name

example(특수문자 그대로):
grep 'hello world' file.txt
echo 'price is $100'      # $100 그대로
sed 's/foo/bar/g' file    # sed 패턴


## \
- echo "xxx \$xxx" - 바로 다음 한글자만 escape(특수의미무시) or 줄바꿈 무시

echo hello \$name -> hello \$name

echo hello \
name
-> hello name

example:
echo "I cost \$5"         # $5 → 그대로 $5
mkdir my\ folder          # 공백 있는 폴더명
ls -la \
   /tmp                   # 명령어 한 줄로 이음


## man - manual
- man echo - echo 사용법 알려줌

## xxx --help 
- 사용법 알려줌

## cd - change directory
- cd /bin -> bin으로 이동


## 경로 관련
- . - current directory 
- .. - upper directory
- ~ - default directory
- tab button - possible option


## Path 
- environmental variable, 셸이 명령어 찾는 디렉토리 목록 

echo $PATH

## which 
- print out the location of the program

which python
which date
어디 경로에 있는지 알려줌

관계: 터미널에 python 치면, 셸이 PATH에 나열된 디렉토리를 순서대로 뒤져서 python이라는 실행파일을 찾아. which는 어디서 찾았는지 보여주는 도구


## 짜잘한거
- s - list, list out all the contents of the directory
- cat - concatenate 붙이거나 출력함
- sort - 줄 단위로 정렬함
- nvim - Neovim, 텍스트 에디터 vim의 업그레이드 버전
- uniq - unique print out only unique, but only consecutive
- head/tail - print out first 10 or last 10 

## grep 
- file searcher, 패턴 매칭으로 줄 검색

-i 대소문자 무시, -r 재귀, -n 줄번호, -v 역매칭

 자주 파이프와: `cat log | grep ERROR`

## sed 
- stream editor. 텍스트 치환/편집 도구 usually for search and replacement (줄 단위 치환)


sed    s/패턴/대체/플래그
       │  │   │    │
       │  │   │    └─ g, i, 숫자 등
       │  │   └─ 바꿀 내용
       │  └─ 찾을 패턴 (정규식 가능)
       └─ substitute

sed -i 's/grep/jon/g' file.txt
환해라(s), grep을(찾을 거), jon으로(바꿀 거), 줄 전체에서 모든 매칭을(g)
grep을 jon으로 다 바꿔라

## find 
- 찾아줌 디렉토리에 있는 파일들 / grep는 너무 심플할수도 있어서 find를 쓸때가 많음

find ~/Downloads -type f -name "*.zip"
다운로드에 있는 zip파일 찾아줌


## Control + C 
- 멈춤


## awk 
- parsing file also editor like sed / 컬럼/필드 단위 텍스트 처리 도구

for csv, it is very useful ?
score.txt:
Alice 85 math
Bob 92 science
Charlie 78 math

awk '{print $1}' scores.txt
Alice
Bob
Charlie

awk '{print $2}' scores.txt
85
92
78

awk '{print $1, $3}' scores.txt
Alice math
Bob science
Charlie math

data.csv:
Alice,85,math
Bob,92,science

awk -F, '{print $2}' data.csv
85
92

awk '$2 > 90 {print $1}' scores.txt - 90점 넘는사람만


ssh = Secure Shell. 원격 컴퓨터에 접속하는 도구


## | 
- pipeline / 왼쪽 명령의 출력을 → 오른쪽 명령의 입력으로 보냄.

ls | grep ".py" - ls로 리스트 출력 그담에는 py를 이름으로 가지고 있는 패턴 파일들만 출력하기


## bash 
- 문법들- 다른 언어랑 비슷함

if grep 2026 thedate.txt; then echo "it's 2026"; fi 

for varname in a b c d; do echo "$varname"; done
while grep 2026 thedate.txt; do echo "it's still 2026"; date > thedate.txt  

if test/[ - test/[] program in shell

if [ "hello" = "world]; then echo "equal"; else echo "not equal"; fi


## shebang line 
- 스크립트 첫 줄의 #!

## chomd
- change the permission of the file

- +x - becomes executable

chmod +x lecture.sh -> then it become executable

## Exercises
xercises
All classes in this course are accompanied by a series of exercises. Some give you a specific task to do, while others are open-ended, like “try using X and Y programs”. We highly encourage you to try them out.

We have not written solutions for the exercises. If you are stuck on anything in particular, feel free to post in #missing-semester-forum on Discord or send us an email describing what you’ve tried so far, and we will try to help you out. These exercises will also likely work well as initial prompts in a conversation with an LLM where you can interactively dive into the topic. The real value in these exercises is the journey of discovering the answers, not the answer itself. We encourage you to follow tangents and ask “why” as you work through them, rather than just looking for the shortest path to the solution.

For this course, you need to be using a Unix shell like Bash or ZSH. If you are on Linux or macOS, you don’t have to do anything special. If you are on Windows, you need to make sure you are not running cmd.exe or PowerShell; you can use Windows Subsystem for Linux or a Linux virtual machine to use Unix-style command-line tools. To make sure you’re running an appropriate shell, you can try the command echo $SHELL. If it says something like /bin/bash or /usr/bin/zsh, that means you’re running the right program.

What does the -l flag to ls do? Run ls -l / and examine the output. What do the first 10 characters of each line mean? (Hint: man ls)

In the command find ~/Downloads -type f -name "*.zip" -mtime +30, the *.zip is a “glob”. What is a glob? Create a test directory with some files and experiment with patterns like ls *.txt, ls file?.txt, and ls {a,b,c}.txt. See Pattern Matching in the Bash manual.

What’s the difference between 'single quotes', "double quotes", and $'ANSI quotes'? Write a command that echoes a string containing a literal $, a !, and a newline character. See Quoting.

The shell has three standard streams: stdin (0), stdout (1), and stderr (2). Run ls /nonexistent /tmp and redirect stdout to one file and stderr to another. How would you redirect both to the same file? See Redirections.

$? holds the exit status of the last command (0 = success). && runs the next command only if the previous succeeded; || runs it only if the previous failed. Write a one-liner that creates /tmp/mydir only if it doesn’t already exist. See Exit Status.

Why does cd have to be built into the shell itself rather than a standalone program? (Hint: think about what a child process can and cannot affect in its parent.)

Write a script that takes a filename as an argument ($1) and checks whether the file exists using test -f or [ -f ... ]. It should print different messages depending on whether the file exists. See Bash Conditional Expressions.

Save the script from the previous exercise to a file (e.g., check.sh). Try running it with ./check.sh somefile. What happens? Now run chmod +x check.sh and try again. Why is this step necessary? (Hint: look at ls -l check.sh before and after the chmod.)

What happens if you add -x to the set flags in a script? Try it with a simple script and observe the output. See The Set Builtin.

Write a command that copies a file to a backup with today’s date in the filename (e.g., notes.txt → notes_2026-01-12.txt). (Hint: $(date +%Y-%m-%d)). See Command Substitution.

Modify the flaky test script from the lecture to accept the test command as an argument instead of hardcoding cargo test my_test. (Hint: $1 or $@). See Special Parameters.

Use pipes to find the 5 most common file extensions in your home directory. (Hint: combine find, grep or sed or awk, sort, uniq -c, and head.)

xargs converts lines from stdin into command arguments. Use find and xargs together (not find -exec) to find all .sh files in a directory and count the lines in each with wc -l. Bonus: make it handle filenames with spaces. (Hint: -print0 and -0). See man xargs.

Use curl to fetch the HTML of the course website (https://missing.csail.mit.edu/) and pipe it to grep to count how many lectures are listed. (Hint: look for a pattern that appears once per lecture; use curl -s to silence the progress output.)

jq is a powerful tool for processing JSON data. Fetch the sample data at https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json with curl and use jq to extract just the names of people whose version is greater than 6. (Hint: pipe to jq . first to see the structure; then try jq '.[] | select(...) | .name')

awk can filter lines based on column values and manipulate output. For example, awk '$3 ~ /pattern/ {$4=""; print}' prints only lines where the third column matches pattern, while omitting the fourth column. Write an awk command that prints only lines where the second column is greater than 100, and swaps the first and third columns. Test with: printf 'a 50 x\nb 150 y\nc 200 z\n'

Dissect the SSH log pipeline from the lecture: what does each step do? Then build something similar to find your most-used shell commands from ~/.bash_history (or ~/.zsh_history).



## Summary
(영상 끝나고 내 말로 한두 줄)