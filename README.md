# 설명  
How to use pyc files for python nodes in ROS2 Humble.     
ROS2 Humble 환경에서 Python 노드에 **pyc 파일을 활용하는 방법**을 정리한 레포지토리입니다.  

<br>

--- 

### 1. 레포지토리 다운로드
```
cd Desktop
git clone https://github.com/Jinsun-Lee/ros2_convert_pyc_gui.git convert_pyc
```

<br>  

### 2. pyc 파일 생성 — test.py 설명
추가 설명: [1. pyc 파일 생성을 위한 test.py 동작 설명](https://github.com/Jinsun-Lee/ros2_convert_pyc_gui/blob/master/docs/1_pyc_%ED%8C%8C%EC%9D%BC_%EC%83%9D%EC%84%B1%EC%9D%84_%EC%9C%84%ED%95%9C_test_py_%EB%8F%99%EC%9E%91_%EC%84%A4%EB%AA%85.md)
```
cd convert_pyc
python3 test.py
```
1. 사용자의 이름을 기반으로 ~/ros2_ws/src 경로를 자동 생성
2. 해당 경로 안의 폴더 리스트를 GUI에 출력
3. 사용자가 Path를 수정 후 Update 하면 즉시 반영됨
4. 폴더를 클릭하면 확인 팝업 표시
5. "O" 선택 시 → 해당 폴더의 마이크로서비스 py 파일을 컴파일(.pyc)
6. py 파일은 데스크탑으로 옮기고, 원래 위치에는 .pyc만 남음

<br>  

### 3. pyc 파일 사용 — test2.py 설명
추가 설명: https://youtu.be/mgs05eKuSv0
```
cd convert_pyc
python3 test2.py
```
1. 명령어를 실행하면, `docs` 폴더 안의 `lib.cpython-310.pyc`을 기준으로 동작
2. 함수를 수정하고 싶을 경우, `docs` 폴더 안의 `lib.py` 파일을 수정
3. `test2.py`를 동작 → 수정이 반영되지 않음(기존의 동작과 동일)
4. `lib.py` 파일 실행(pyc 파일이 갱신됨) → `test2.py`를 동작 → 수정이 반영됨(기존과 다른 동작)
