import os
import shutil
import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button, StringVar, messagebox, filedialog

def get_folder_list(path):
    try:
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        return folders
    except OSError as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return []

def on_select(event):
    selected_index = folder_listbox.curselection()
    if selected_index:
        selected_folder = folder_listbox.get(selected_index)
        selected_folder_var.set(selected_folder)
        confirm = messagebox.askquestion("Confirm", f"Do you want to process the folder '{selected_folder}'?", icon='question')
        if confirm == 'yes':
            process_selected_folder()

def update_folder_list(path):
    folder_listbox.delete(0, tk.END)
    folders = get_folder_list(path)
    for folder in folders:
        folder_listbox.insert(tk.END, folder)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        custom_path_var.set(folder_selected)
        update_folder_list(folder_selected)

def update_custom_path():
    custom_path = custom_path_entry.get()
    if os.path.exists(custom_path):
        custom_path_var.set(custom_path)
        update_folder_list(custom_path)
    else:
        messagebox.showerror("Invalid Path", "The specified path does not exist.")

def process_selected_folder():
    selected_folder = selected_folder_var.get()
    if not selected_folder:
        messagebox.showerror("No Folder Selected", "Please select a folder first.")
        return
    
    selected_folder_path = os.path.join(custom_path_var.get(), selected_folder)
    final(selected_folder_path)

# lib 폴더 처리 함수들
def is_folder_exist(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return folder_path
    return None

def remove_pycache(folder_path):
    pycache_path = os.path.join(folder_path, "__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)

def rename_old_pyc(folder_path):
    pyc_files = [f for f in os.listdir(folder_path) if f.endswith('.pyc')]
    for pyc_file in pyc_files:
        old_pyc_path = os.path.join(folder_path, pyc_file)
        new_pyc_name = "old_" + pyc_file
        new_pyc_path = os.path.join(folder_path, new_pyc_name)
        os.rename(old_pyc_path, new_pyc_path)

def compile_py_files(chk_subfolder_path):
    os.chdir(chk_subfolder_path)
    with open(os.devnull, 'w') as null_file:
        os.system('python3 -m compileall . > {} 2>&1'.format(null_file.name))

def get_python_files_except_init(subfolder_path):
    python_files = [f for f in os.listdir(subfolder_path) if f.endswith('.py') and f != '__init__.py']
    return python_files

def move_pycache_to_lib(folder, subfolder_path, chk_subfolder_path):
    folder_name = f"{folder}_lib"
    desktop_lib_path = os.path.join(os.path.expanduser("~"), 'Desktop', 'lib', folder_name)
    python_files = get_python_files_except_init(subfolder_path)

    for python_file in python_files:
        src_py_file_path = os.path.join(subfolder_path, python_file)
        dest_py_file_path = os.path.join(desktop_lib_path, python_file)
        
        if os.path.exists(src_py_file_path):
            os.makedirs(os.path.dirname(dest_py_file_path), exist_ok=True)
            shutil.move(src_py_file_path, dest_py_file_path)
        
        pyc_file = f"{os.path.splitext(python_file)[0]}.cpython-310.pyc"  # Python 버전에 따라 다를 수 있음
        pycache_path = os.path.join(chk_subfolder_path, "__pycache__", pyc_file)
        dest_pyc_file_path = os.path.join(subfolder_path, pyc_file)
        shutil.move(pycache_path, dest_pyc_file_path)

def final(path):
    folders = get_folder_list(path)
    for folder in folders:
        subfolder_path = os.path.join(path, folder, "lib")
        chk_subfolder_path = is_folder_exist(subfolder_path)
        
        if chk_subfolder_path is not None:
            remove_pycache(chk_subfolder_path)
            rename_old_pyc(chk_subfolder_path)
            compile_py_files(chk_subfolder_path)
            move_pycache_to_lib(folder, subfolder_path, chk_subfolder_path)
            remove_pycache(chk_subfolder_path)

# GUI 생성
root = tk.Tk()
root.title("ROS2 Workspace Folder List GUI")

# 사용자 홈 디렉토리 및 ROS2_WS 경로 설정
user_home = os.path.expanduser("~")
ros_ws_path = os.path.join(user_home, 'ros2_ws', 'src')

# 선택한 폴더를 저장할 변수
selected_folder_var = StringVar()

# 경로 수정을 위한 Entry와 확인 버튼
custom_path_var = StringVar()
custom_path_var.set(ros_ws_path)
custom_path_entry = Entry(root, textvariable=custom_path_var, width=40)
custom_path_entry.pack(pady=10)
Button(root, text="Update Path", command=update_custom_path).pack()

# 폴더 리스트 박스와 스크롤바
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
folder_listbox = Listbox(frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, width=40, height=10)
folder_listbox.pack(side=tk.LEFT)
scrollbar.config(command=folder_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 리스트 박스의 선택 이벤트 연결
folder_listbox.bind("<<ListboxSelect>>", on_select)

# 초기 ROS2_WS 경로에 대한 폴더 리스트 출력
update_folder_list(ros_ws_path)

# GUI 실행
root.mainloop()

