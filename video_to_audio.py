import os
from moviepy.editor import VideoFileClip


def extract_audio_from_video(video_path, output_format="mp3"):
    """
    从视频文件中提取音频，并保存为指定格式。

    参数：
    video_path (str): 视频文件路径
    output_format (str): 输出音频格式（默认是"mp3"）

    返回：
    str: 提取的音频文件路径
    """
    try:
        # 加载视频文件
        video = VideoFileClip(video_path)
        # 获取视频中的音频部分
        audio = video.audio
        # 设置音频文件路径，保持与视频文件名相同但扩展名不同
        audio_path = os.path.splitext(video_path)[0] + f".{output_format}"
        # 将音频写入文件
        if output_format == "mp3":
            audio.write_audiofile(audio_path, codec='mp3')
        elif output_format == "wav":
            audio.write_audiofile(audio_path, codec='pcm_s16le')
        elif output_format == "flac":
            audio.write_audiofile(audio_path, codec='flac')
        return audio_path
    except Exception as e:
        print(f"从 {video_path} 提取音频时出错：{e}")
        return None


def process_videos_in_directory(directory, output_format="mp3"):
    """
    处理指定目录中的所有视频文件，提取音频。

    参数：
    directory (str): 目标目录路径
    output_format (str): 输出音频格式（默认是"mp3"）
    """
    # 支持的视频文件格式
    supported_formats = (".mp4", ".avi", ".mov", ".mkv")
    for filename in os.listdir(directory):
        # 检查文件是否为支持的视频格式
        if filename.endswith(supported_formats):
            video_path = os.path.join(directory, filename)
            # 提取音频
            audio_path = extract_audio_from_video(video_path, output_format)
            if audio_path:
                print(f"提取的音频已保存到 {audio_path}")
