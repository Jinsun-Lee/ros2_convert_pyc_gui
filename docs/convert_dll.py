"""
사용자의 계정을 알아내고 ros2_ws/src와 결합
결합한 경로의 폴더를 자동으로 출력

특정 경로에 있는 폴더 리스트를 출력해서 GUI에 리스트로 띄움
만약 사용자가 폴더 경로를 수정하고 확인 버튼을 누르면 
수정한 경로의 폴더를 다시 출력
"""

import os
import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button, StringVar, messagebox

def get_ros_src_folders(user_home):
    ros_ws_path = os.path.join(user_home, 'ros2_ws', 'src')
    folders = get_folder_list(ros_ws_path)
    return folders

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
        messagebox.showinfo("Selected Folder", f"You selected: {selected_folder}")

def update_folder_list(path):
    folder_listbox.delete(0, tk.END)
    folders = get_folder_list(path)
    for folder in folders:
        folder_listbox.insert(tk.END, folder)

def browse_folder():
    folder_selected = tk.filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)
        update_folder_list(folder_selected)

def update_custom_path():
    custom_path = custom_path_entry.get()
    if os.path.exists(custom_path):
        path_var.set(custom_path)
        update_folder_list(custom_path)
    else:
        messagebox.showerror("Invalid Path", "The specified path does not exist.")

# GUI 생성
root = tk.Tk()
root.title("ROS2 Workspace Folder List GUI")

# 사용자 홈 디렉토리 및 ROS2_WS 경로 설정
user_home = os.path.expanduser("~")
ros_ws_path = os.path.join(user_home, 'ros2_ws', 'src')

# 경로 수정을 위한 Entry와 확인 버튼
custom_path_var = StringVar()
custom_path_var.set(ros_ws_path)
custom_path_entry = Entry(root, textvariable=custom_path_var, width=40)
custom_path_entry.pack(pady=10)
Button(root, text="Update Path", command=update_custom_path).pack()


# 폴더 선택 버튼과 경로 표시 레이블
path_var = tk.StringVar()
path_var.set(ros_ws_path)


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

