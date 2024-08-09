<!-- 원래 pyc 파일 만드는 방법 -->
<details>
    <summary>원래 pyc 파일 만드는 방법</summary>

```
cd
cd /home/jinsunlee/ros2_ws/src/load_img/load_img/lib

python3 -m compileall .
```
    
위의 명령어를 실행하면 해당 경로의 파일을 전부 컴파일함  
</details>


<!-- 각 파일의 동작 설명 -->
<details>
    <summary>각 파일의 동작 설명</summary>

```
python3 convert_dll.py # 경로 무관하게 동작
```
동작하면 GUI가 출력됨 > Update Path를 클릭하면 리스트 갱신  
폴더를 클릭하면 클릭한 폴더명이 출력됨
X를 누르면 GUI가 닫힘  
  
```
python3 print_all_folder.py # 경로 무관하게 동작
```
ros2_ws/src/클릭한폴더/클릭한폴더/lib 안에 있던 py 파일이 pyc 파일이 붙음
원본 파일은 데스크탑에 lib라는 폴더가 생기면서 클릭한폴더_lib 폴더 안에 파일이 옮겨짐  
파이썬 파일이 없는데 계속 실행하면 old_가 붙은 pyc 파일로 바뀜
</details>

</br>
</br>



# 레포 다운로드
```
cd Desktop
git clone https://github.com/Jinsun-Lee/convert_pyc.git
```
</br>

# 동작
```
cd convert_pyc
python3 test.py
```
명령어를 실행하면, 사용자를 알아내서 ros2_ws/src 경로 생성  
경로 내의 폴더 리스트를 출력해서 GUI에 리스트로 띄움  
사용자가 폴더 경로를 수정하고 업데이트하면 반영이 됨  
폴더를 클릭하면 마이크로서비스 파일을 컴파일하고 옮겨줌
