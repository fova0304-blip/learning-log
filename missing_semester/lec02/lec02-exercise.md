## Exercise 1. `--` special argument

### Goal
`--`가 왜 필요한지 직접 확인한다.

### Step 1
터미널에서 임시 연습 폴더를 만들어라.

```bash
mkdir lec02-exercises
cd lec02-exercises
```

### Step 2
`-myfile`이라는 이름의 파일을 만들어라.

```bash
touch -- -myfile
```

### Step 3
파일이 생겼는지 확인해라.

```bash
ls -la
```

### Step 4
일부러 아래 명령어를 실행해봐라.

```bash
rm -myfile
```

### Question 1
위 명령어를 실행했을 때 어떤 일이 생겼는지 적어라.

### Step 5
이제 올바르게 삭제해라.

```bash
rm -- -myfile
```

### Step 6
삭제됐는지 확인해라.

```bash
ls -la
```

### Question 2
왜 `rm -myfile`은 문제가 되고, `rm -- -myfile`은 되는지 설명해라.

### My Answer
1. `rm -myfile` 실행 결과:
2. `--`가 필요한 이유: