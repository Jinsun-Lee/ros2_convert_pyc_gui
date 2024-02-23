"""
특정 경로 안에 있는 폴더 중 패키지 폴더를 지정해 주면
바탕화면에 lib라는 폴더를 만들고 
각 패키지_lib 폴더를 생성

패키지의 lib 폴더 안에 있는 python 파일을 빌드하고
python 파일은 바탕화면/lib/패키지_lib 폴더 안으로 이동
pyc 파일은 패키지의 lib 폴더 안으로 이동

---

# TODO로 해야할 것 정리해 둠
- 파이썬 파일이 없으면 컴파일이 안 되니 pyc 파일 삭제하지 않기, 이름 바꾸지 않기
- old 도 lib으로 옮기기 (바로 옮겨버리면 이전의 old 파일이 기존의 old 파일을 대체하게 되니 옮길 때 이름에 old_를 더 붙이든 해야함)
- 코드 작성할 때 lib에 있는 파이썬 파일을 다시 원위치 시키기 귀찮으니 그 코드도 있으면 좋을 듯?
- py 파일도 수정하게끔... < 이건 걍 수작업 할까 생각중
"""

import os
import shutil
import subprocess

def get_folder_list(folder_path):
    folder_list = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
    return folder_list

def is_folder_exist(folder_path):
    chk_exist = os.path.exists(folder_path)  # 주어진 경로에 파일 또는 폴더가 존재하는지
    chk_folder = os.path.isdir(folder_path)  # 해당 경로가 폴더인지
    if chk_exist and chk_folder:
        return folder_path
    else:
        return None

def remove_pycache(folder_path):
    # __pycache__ 폴더 삭제
    pycache_path = os.path.join(folder_path, "__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
        #print(f"Removed __pycache__ folder in {folder_path}")

def rename_old_pyc(folder_path):
    # 기존의 pyc 파일 이름 수정 (old_ 를 붙여서 저장)
    pyc_files = [f for f in os.listdir(folder_path) if f.endswith('.pyc')]
    for pyc_file in pyc_files:
        #print(os.path.join(folder_path, pyc_file))
        old_pyc_path = os.path.join(folder_path, pyc_file)
        new_pyc_name = "old_" + pyc_file
        new_pyc_path = os.path.join(folder_path, new_pyc_name)
        os.rename(old_pyc_path, new_pyc_path)
        #print(f"Renamed: {old_pyc_path} -> {new_pyc_path}")
              
def compile_py_files(chk_subfolder_path):
    os.chdir(chk_subfolder_path)

    #os.system('python3 -m compileall .')
    # 위의 코드로 컴파일하니 출력이 나와서 리디렉션을 통해 출력을 숨김
    with open(os.devnull, 'w') as null_file:
        os.system('python3 -m compileall . > {} 2>&1'.format(null_file.name))
        
def get_python_files_except_init(subfolder_path):
    # init 파일은 pyc 파일로 빌드도 안 하고 옮기지도 않으려고 제외
    python_files = [f for f in os.listdir(subfolder_path) if f.endswith('.py') and f != '__init__.py']
    return python_files

def move_old_pyc_files(folder_path): 
    # TODO 기존의 pyc 파일을 패키지 폴더 말고 바탕화면/lib/패키지_lib 폴더 안으로 이동하게끔
    pyc_files = [f for f in os.listdir(folder_path) if f.endswith('.pyc') and f.startswith('old_')]
    for pyc_file in pyc_files:
        src_path = os.path.join(folder_path, pyc_file)
        
        
        #dest_path = os.path.join(folder_path, pyc_file)
        #shutil.move(src_path, dest_path)
        #print(f"Moved {pyc_file} from {src_path} to {dest_path}")
        
def move_pycache_to_lib(folder, subfolder_path, chk_subfolder_path):
    
    # 패키지_lib 이름의 폴더 안으로 원본 파이썬 파일을 옮겨야 함 
    folder_name = f"{folder}_lib"
    desktop_lib_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'lib', folder_name)
    # print("옮길 대상 폴더", desktop_lib_path)
    
    # lib 폴더에 있는 원본 .py 파일을 바탕화면의 desktop_lib_path 옮기는데, subfolder_path에 있는 .py의 파일 중 __init__ 파일을 제외
    python_files = get_python_files_except_init(subfolder_path)

    for python_file in python_files:
        src_py_file_path = os.path.join(subfolder_path, python_file)
        dest_py_file_path = os.path.join(desktop_lib_path, python_file)
        
        if os.path.exists(src_py_file_path):
            os.makedirs(os.path.dirname(dest_py_file_path), exist_ok=True)
            #print(f"{python_file}을 {src_py_file_path}에서 {dest_py_file_path}로 이동")
            shutil.move(src_py_file_path, dest_py_file_path)
        
        # pyc는 기존 패키지의 subfolder_path로 이동
        pyc_file = f"{os.path.splitext(python_file)[0]}.cpython-310.pyc" # 파이썬 버전마다 숫자가 달라짐
        pycache_path = os.path.join(chk_subfolder_path, "__pycache__", pyc_file)
                
        dest_pyc_file_path = os.path.join(subfolder_path, pyc_file)
        #print(f"{pycache_path}에서 {dest_pyc_file_path}로 이동")
        shutil.move(pycache_path, dest_pyc_file_path)



def final(path):
    folders = get_folder_list(path)
    for folder in folders:
        subfolder_path = os.path.join(path, folder, folder, "lib")
        # print(subfolder_path) # /home/jinsunlee/ros2_ws/src/yolov8_ros/yolov8_ros/lib
        
        chk_subfolder_path = is_folder_exist(subfolder_path)
        # print(chk_subfolder_path) # lib 폴더가 있는 폴더로만 걸러짐
        
        if chk_subfolder_path is not None:
            
            # TODO
            # 기능이 추가되거나 바뀌면 이 부분 순서 변경이 고려됨
            remove_pycache(chk_subfolder_path)
            rename_old_pyc(chk_subfolder_path)
            
            compile_py_files(chk_subfolder_path)
            
            move_pycache_to_lib(folder, subfolder_path, chk_subfolder_path)
            remove_pycache(chk_subfolder_path)


user_home = os.path.expanduser("~")
target_path = os.path.join(user_home, 'ros2_ws/src')

final(target_path)