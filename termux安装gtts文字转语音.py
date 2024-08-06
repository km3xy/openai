import os
from gtts import gTTS
from pydub import AudioSegment

def change_pitch(audio_segment, semitones):
    new_sample_rate = int(audio_segment.frame_rate * (2.0 ** (semitones / 12.0)))
    return audio_segment._spawn(audio_segment.raw_data, overrides={'frame_rate': new_sample_rate}).set_frame_rate(audio_segment.frame_rate)

# 定义音效预设处理函数
def apply_preset(audio, preset):
    if preset == "男声":
        # 降低音高约4个半音
        audio = change_pitch(audio, -4)
    elif preset == "女声":
        # 提高音高约4个半音
        audio = change_pitch(audio, 4)
    return audio

# 定义函数以将文本转换为语音并保存
def text_to_speech(text, lang='zh', preset=""):
    count = 1
    while True:
        filename = f"response_{count}.mp3"
        if not os.path.exists(filename):
            break
        count += 1

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    # 加载音频文件
    audio = AudioSegment.from_file(filename)

    # 应用音效预设
    if preset:
        audio = apply_preset(audio, preset)

    # 保存处理后的音频文件
    audio.export(filename, format="mp3")

    # 使用mpv播放音频文件
    os.system(f"mpv {filename}")

# 示例用法
if __name__ == "__main__":
    while True:
        user_input = input("请输入你想转换成音频的文本 (输入'exit'退出): ")
        if user_input.lower() == 'exit':
            break
        preset_input = input("请选择预设音效 (男声, 女声): ")
        # 转换文本为语音并播放
        text_to_speech(user_input, lang='zh', preset=preset_input)





