# ROS2 노드에서 `.pyc` 파일 사용 방법
`.pyc` 파일이 `__pycache__`에 있으면 `import test`로 사용 가능        
원본 `.py` 없이 `.pyc`만 존재해도 import 가능

<br>

예시 파일 구조
```py
ros2_ws/
└── control_motor/
    └── control_motor/
        ├── __init__.py
        ├── control_motor_node.py
        ├── convert_protocol_node.py          ❸ 
        └── lib/
            ├── __init__.py                   ❷ 
            ├── lib_motor.cpython-310.pyc     ❶
            └── lib_protocol.cpython-310.pyc
```

<br>

❶. `.pyc` 파일을 lib 폴더 내로 이동         
❷. lib 폴더 내의 `__init__.py`에 pyc 로딩 함수 작성        
```py
import os
import types
import marshal

def get_path(file_name=None):
    p = os.path.dirname(os.path.abspath(__file__)).split("/")
    LIB_PATH = os.path.join("/", *p[1:4], "src", *p[5:6],*p[5:6], "lib", file_name)
    return LIB_PATH

def get_pyc(module_file):
    file_path = get_path(module_file)
    print('\n파일명:', file_path, '\n\n')
    pyc = open(file_path, 'rb').read()
    code = marshal.loads(pyc[16:])
    module = types.ModuleType('module_name')
    exec(code, module.__dict__)
    return module

control_motor = get_pyc("lib_motor.cpython-310.pyc")
convert_protocol = get_pyc("lib_protocol.cpython-310.pyc")
```
❸. 노드 내에서 pyc 기반 함수 import하고 사용       
control_motor_node.py
```py
from .lib import control_motor as CONTROL
from .lib import convert_protocol as PROTOCOL

class SendSignal():
  def __init__(self):
    CONTROL.arduino_pinsetting(pin1, pin2, ...) # pyc 내부 함수 이렇게 사용

def main(args=None):
  rclpy.init(args=args)
  node = MotorControlNode()
  try:
      rclpy.spin(node)
  except KeyboardInterrupt:
      print("\n\nshutdown\n\n")

      message = PROTOCOL.protocol_with_differential(0, 0, 0) # 이렇게 사용
      ser.write(message.encode())
      pass
```

<br>

---

# pyc 활용 방식 — 추가 예시
아래처럼도 쓸 수 있음 
```py
from load_img.lib import get_path
IMAGE_DIRECTORY_PATH = get_path("Collected_Datasets")
```

<br>

#### A1. 노드와 같은 경로에 있는 init에 내용을 작성할 경우
`yolov8_ros/__init__.py` 예시:
```py
import os
from datetime import datetime

def get_path(file_name=None):
    p = os.path.dirname(os.path.abspath(__file__)).split("/")
    LIB_PATH = os.path.join("/", *p[1:4], "src", *p[5:6], *p[5:6], "lib", file_name)
    return LIB_PATH

def get_time(is_img=True):
    now = datetime.now()
    now = now.strftime('%y%m%d_%H%M%S')
    if is_img:
        result = now + '.png' 
    return result
```
node 코드
```py
from yolov8_ros import *
MODEL = get_path('best.pt') # lib 안에 위치한 pt 파일명
```

<br>

#### A2. 하나의 파일 안에서 사용할 경우
data_collection.py 예시:
```py
import cv2
import string
import time
import sys
import os
import marshal
import types

real_path = os.path.dirname(os.path.realpath(__file__))
pyc = open((real_path)+'/data_collection_func.cpython-310.pyc', 'rb').read()
code = marshal.loads(pyc[16:])
module = types.ModuleType('module_name')
exec(code, module.__dict__)

def main():
    data_collector = module.Data_Collect(path=DATA_COLLECTION_PATH, cam_num=CAM_NUM, ser_port=PORT, arduino_info=arduino_init_info)
    
    try:
        data_collector.process()
    except KeyboardInterrupt:
        data_collector.interrupt_process()

    data_collector.ser.close()

    if data_collector.cap.isOpened():
        data_collector.cap.release()

    cv2.destroyAllWindows()
    sys.exit(0)

if __name__ == '__main__':
    main()
```

<br>

---

# 기타 GUI 관련 스크립트
```py
python3 convert_dll.py # 경로 무관하게 동작
```
동작하면 GUI가 출력됨 > Update Path를 클릭하면 리스트 갱신     
폴더를 클릭하면 클릭한 폴더명이 출력됨      
X를 누르면 GUI가 닫힘  

<br>  

```py
python3 print_all_folder.py # 경로 무관하게 동작
```
ros2_ws/src/클릭한폴더/클릭한폴더/lib 안에 있던 py 파일이 pyc 파일이 붙음              
원본 파일은 데스크탑에 lib라는 폴더가 생기면서 클릭한폴더_lib 폴더 안에 파일이 옮겨짐                   
파이썬 파일이 없는데 계속 실행하면 old_가 붙은 pyc 파일로 바뀜 
