import os

def function():
    print("Hello")

def function2():
    print("world")
    return "finish"
    
if __name__ == "__main__":
    import py_compile

    # 경로 설정
    base_path = os.path.dirname(os.path.realpath(__file__))
    pyc_folder = os.path.join(base_path) # pyc 파일을 어디에 저장할 건지
    target_file = "lib.py" # 라이브러리화 할 파이썬 파일

    # 1. __pycache__ 폴더 삭제
    pycache_path = os.path.join(base_path, "__pycache__")
    if os.path.exists(pycache_path):
        import shutil
        shutil.rmtree(pycache_path)

    # 2. pyc_folder 폴더 내 기존 pyc 파일 삭제
    pyc_file_to_delete = os.path.join(pyc_folder, "lib.cpython-310.pyc")
    if os.path.exists(pyc_file_to_delete):
        os.remove(pyc_file_to_delete)
        print("기존 pyc 파일 삭제")

    # 3. 특정 파일 컴파일
    source_file_path = os.path.join(base_path, target_file)
    if os.path.exists(source_file_path):
        py_compile.compile(source_file_path, cfile=pyc_file_to_delete)
        print("끝")
    else:
        print(f"File not found: {source_file_path}")
