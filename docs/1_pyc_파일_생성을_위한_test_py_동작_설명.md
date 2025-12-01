<details><summary>pyc 파일 생성 방법 정리(test.py 파일과 무관)</summary>

Python 스크립트를 실행하면 `__pycache__` 아래에 자동으로 .pyc 파일이 생성
```
python3 test.py
```

.pyc 파일은 아래 명령어를 사용해서 수동 생성이 가능
```
python3 -m py_compile test.py
```

현재 위치한 경로의 파일을 모두 컴파일하고 싶다면 아래 명령어를 사용(폴더 전체 컴파일)
```
python3 -m compileall .
```
</details>

<br>

### 초기화면
![스크린샷 2024-08-09 12-32-07](https://github.com/user-attachments/assets/60d36fc0-5df1-4504-9dd1-281222024617)

<br>

### 폴더 클릭
![스크린샷 2024-08-09 12-32-37](https://github.com/user-attachments/assets/b617d0fe-57bc-49fc-a37a-25c5cc57ce94)

<br>

### pyc 파일이 생김
![스크린샷 2024-08-09 12-33-23](https://github.com/user-attachments/assets/e7135e3a-cf80-4740-8eea-04012a8ade72)

<br>

### b는 선택하지 않아 생기지 않음
![스크린샷 2024-08-09 12-33-40](https://github.com/user-attachments/assets/5c600a7c-5cf9-4eca-8d78-126e1d6d6bc4)

<br>

### b도 컴파일 선택
![스크린샷 2024-08-09 12-33-52](https://github.com/user-attachments/assets/ceea870f-b625-4d11-8465-85b108f6acd2)

<br>

### b도 생김
![스크린샷 2024-08-09 12-33-58](https://github.com/user-attachments/assets/c369f17f-109a-40d8-a7b5-80aee1f4e6a4)

<br>

### 파이썬 파일이 옮겨진 것도 확인
![스크린샷 2024-08-09 12-34-02](https://github.com/user-attachments/assets/5ade5aed-0011-45c2-97d2-1ba68369fd57)

<br>

### 파일을 다시 옮긴 후 컴파일하면 어떻게 될까
![스크린샷 2024-08-09 12-34-09](https://github.com/user-attachments/assets/88ac1778-4922-4ee6-9fb5-fe10cdd83206)

<br>

### pyc가 있는데 컴파일 진행
![스크린샷 2024-08-09 12-34-16](https://github.com/user-attachments/assets/55a790ae-b923-4497-850e-6e0c58f7b499)

<br>

### 기존의 pyc는 old_가 붙고 새로 생성됨
![스크린샷 2024-08-09 12-34-22](https://github.com/user-attachments/assets/99839e86-66da-4543-83b0-4226c82e6bd0)

<br>

### a는 무관
![스크린샷 2024-08-09 12-34-37](https://github.com/user-attachments/assets/712e2819-de94-4de7-8de4-d480b43ef59b)
