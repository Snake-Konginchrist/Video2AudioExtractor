# Video2AudioExtractor

## 简介
Video2AudioExtractor是一个简单的Python项目，允许用户从指定文件夹中的所有视频文件中无损提取音频，并将其保存为MP3格式。项目包括图形用户界面，方便用户选择目录并自动处理视频文件。

## 特性
- 支持多种视频格式（.mp4, .avi, .mov, .mkv）
- 支持多种音频格式（.mp3, .wav, .flac）
- 简单易用的图形用户界面

## 安装
首先，克隆此仓库到本地（把github替换为gitee即可使用中国大陆仓库）：
```bash
git clone https://github.com/Snake-Konginchrist/Video2AudioExtractor.git
cd Video2AudioExtractor
```

安装所需依赖：
```bash
pip install -r requirements.txt
```

## 使用
运行主程序：
```bash
python main.py
```

1. 启动程序后，选择需要的音频格式（默认是MP3）。
2. 点击“选择目录”按钮。
3. 在弹出的文件对话框中选择包含视频文件的目录。
4. 程序将自动处理该目录中的所有视频文件，并在同一目录下生成对应格式的音频文件。

## 项目结构
```
Video2AudioExtractor/
│
├── main.py
└── video_to_audio.py
```

## 依赖
- moviepy
- pydub
- tkinter

## 许可证
此项目基于 MIT 许可证，请参阅 [LICENSE](LICENSE) 文件了解更多详情。