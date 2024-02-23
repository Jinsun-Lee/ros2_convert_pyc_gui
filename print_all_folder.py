"""
특정 경로 안에 있는 폴더 중 패키지 폴더는 출력에서 제외하도록

"""

import os

# 얘는 상위 폴더도 출력해서 안 씀
def print_subfolders(path):
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))

def print_subfolders_in_target(path):
    # 특정 경로의 폴더 목록을 가져옴
    folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]
    print(f"{folders} 패키지들의 하위 폴더 리스트를 출력합니다.\n\n")
    
    # 각 폴더의 서브폴더를 출력
    for folder in folders:
        subfolder_path = os.path.join(path, folder)
        for root, dirs, files in os.walk(subfolder_path):
            for dir_name in dirs:
                print(os.path.join(root, dir_name))
                
# 특정 경로 설정
user_home = os.path.expanduser("~")
target_path = os.path.join(user_home, 'ros2_ws/src')

# 함수 호출
print_subfolders_in_target(target_path)
