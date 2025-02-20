# 导入soundfile库
import soundfile as sf
# 导入numpy库方便后续计算
import numpy as np

# 指定需要读取的WAV文件的路径以及生成的WAV文件的存放路径
input_file_path = 'music.wav'
playback_file_path = 'playback_music.wav'
fast_file_path = 'fast_music.wav'
slow_file_path = 'slow_music.wav'
zoom_in_file_path = 'zoom_in_music.wav'
zoom_out_file_path = 'zoom_out_music.wav'
delay_file_path = 'delay_music.wav'

#使用soundfile读取WAV文件,data为音频数据数组，samplerate为采样率
data, samplerate = sf.read(input_file_path)

# 翻转数组生成倒放音频
sf.write(playback_file_path, data[::-1], samplerate)

# 计算加速减速的采样率
fast_samplerate = (int)(samplerate * 1.2)
slow_samplerate = (int)(samplerate * 0.8)

# 写入对应文件
sf.write(fast_file_path, data, fast_samplerate)
sf.write(slow_file_path, data, slow_samplerate)

# 新生成振幅加倍，减半的两个数组，并写入
zoom_in_data = [x * 2 for x in data]
sf.write(zoom_in_file_path, zoom_in_data, samplerate)
zoom_out_data = [x / 2 for x in data]
sf.write(zoom_out_file_path, zoom_out_data, samplerate)

# delay_s 表示延时的秒数
delay_s = 10
# 计算需要增加的数据点数量
cnt = delay_s * samplerate
# 生成10秒的静音数据（双声道）
front_data = np.zeros((cnt, 2))  # 双声道静音数据
# 将静音数据与原始音频数据拼接
delay_data = np.concatenate((front_data, data), axis=0)
# 保存带有10秒延时的音频文件
sf.write(delay_file_path, delay_data, samplerate)