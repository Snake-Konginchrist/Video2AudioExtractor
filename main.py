from tkinter import Tk, filedialog, Button, Label, StringVar, OptionMenu

from video_to_audio import process_videos_in_directory


def select_directory():
    """
    打开文件对话框以选择一个目录，并处理该目录中的所有视频文件。
    """
    directory = filedialog.askdirectory()
    if directory:
        process_videos_in_directory(directory, audio_format.get())
        result_label.config(text=f"已处理目录中的视频文件：{directory}")


# 设置 GUI
root = Tk()
root.title("视频转音频提取器")

label = Label(root, text="请选择要处理视频文件的目录")
label.pack(pady=10)

# 添加音频格式选项
audio_format = StringVar(root)
audio_format.set("mp3")  # 默认值

formats = ["mp3", "wav", "flac"]
format_menu = OptionMenu(root, audio_format, *formats)
format_menu.pack(pady=10)

select_button = Button(root, text="选择目录", command=select_directory)
select_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
