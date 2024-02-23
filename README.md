# convert_pyc

```
cd
cd /home/jinsunlee/ros2_ws/src/load_img/load_img/lib

python3 -m compileall .
```
위의 명령어는 걍 전체 컴파일   
컴파일하고 알려준대로 옮기면 됨   

</br> 

# TODO
```
python3 print_all_folder.py
```
현재 위의 명령어 실행 시 ros2_ws/src 경로 안에 있는 패키지들을 읽어서, 우리 마이크로서비스 파일을 컴파일하고 옮기게끔 작성해 둠
자세한 건 코드 열어서 주석 보면 됨
</br>  
</br>

1. print_all_folder.py 파일의 기능을 convert_dll.py 파일처럼 GUI화 하기
![convert_dll.py 실행 시 사진](https://github.com/Jinsun-Lee/convert_pyc/blob/master/docs/convertdll.png?raw=true "convert_dll.py 실행 시")



