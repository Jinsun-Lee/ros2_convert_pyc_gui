# 레포 다운로드
```
cd Desktop
git clone https://github.com/Jinsun-Lee/convert_pyc.git
```
</br>

--- 

#### test.py 설명
```
cd convert_pyc
python3 test.py
```
1. 명령어를 실행하면, 사용자를 알아내서 ros2_ws/src 경로 생성  
2. 경로 내의 폴더 리스트를 출력해서 GUI에 리스트로 띄움  
3. 사용자가 폴더 경로를 수정하고 업데이트하면 반영이 됨  
4. 폴더를 클릭하면 확인 팝업이 나타나고, 사용자가 "O"를 선택했을 때만  
5. 마이크로서비스 파일을 컴파일하고 바탕화면에 파이썬 파일을 옮겨줌
6. 원래 경로에는 pyc 파일이 대신하게 됨

추가 설명: https://github.com/Jinsun-Lee/convert_pyc/wiki

--- 

#### test2.py 설명
```
cd convert_pyc
python3 test2.py
```
1. 명령어를 실행하면, `docs` 폴더 안의 `lib.cpython-310.pyc`을 기준으로 동작
2. 함수를 수정하고 싶을 경우, `docs` 폴더 안의 `lib.py` 파일을 수정
3. `test2.py`를 동작 → 수정이 반영되지 않음(기존의 동작과 동일)
4. `lib.py` 파일 실행(pyc 파일이 갱신됨) → `test2.py`를 동작 → 수정이 반영됨(기존과 다른 동작)

추가 설명: https://youtu.be/mgs05eKuSv0
