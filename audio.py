import struct
import math
import pyaudio
import wave

p = pyaudio.PyAudio()

rate = 50100
channels = 2
formatting = pyaudio.paFloat32
stream = p.open(
        format=formatting,
        channels=channels,
        rate=rate,
        output=True)

music = ""

def generate_tone(freq, rate):
    data = []
    for i in range(rate):
        #data.append(math.sin(i / 200 * 2 * math.pi))
        data.append(math.sin(freq * (2 * math.pi) * i / rate))
    wave_data = b''.join([struct.pack('f', d) for d in data])
    return wave_data

stream.write(generate_tone(220, 44100))
music += generate_tone(220, 44100)
stream.write(generate_tone(261.626, 44100))
music += generate_tone(261.626, 44100)
stream.write(generate_tone(440, 44100))
music += generate_tone(440, 44100)


stream.write(generate_tone(220, 44100))
music += generate_tone(220, 44100)
stream.write(generate_tone(261.626, 44100))
music += generate_tone(261.626, 44100)
stream.write(generate_tone(440, 44100))
music += generate_tone(440, 44100)

stream.write(generate_tone(493.883, 44100))
music += generate_tone(493.883, 44100)
stream.write(generate_tone(523.251, 44100))
music += generate_tone(523.251, 44100)
stream.write(generate_tone(493.883, 44100))
music += generate_tone(493.883, 44100)


stream.write(generate_tone(523.251, 44100))
music += generate_tone(523.251, 44100)
stream.write(generate_tone(493.883, 44100))
music += generate_tone(493.883, 44100)
stream.write(generate_tone(391.995, 44100))
music += generate_tone(391.995, 44100)
stream.write(generate_tone(329.628, 44100))
music += generate_tone(329.628, 44100)


stream.write(generate_tone(220, 44100))
music += generate_tone(220, 44100)
stream.write(generate_tone(261.626, 44100))
music += generate_tone(261.626, 44100)
stream.write(generate_tone(440, 44100))
music += generate_tone(440, 44100)

stream.write(generate_tone(220, 44100))
music += generate_tone(220, 44100)
stream.write(generate_tone(246.942, 44100))
music += generate_tone(246.942, 44100)
stream.write(generate_tone(329.628, 44100))
music += generate_tone(329.628, 44100)

stream.write(generate_tone(493.883, 44100))
music += generate_tone(493.883, 44100)
stream.write(generate_tone(523.251, 44100))
music += generate_tone(523.251, 44100)

stream.write(generate_tone(391.995, 44100))
music += generate_tone(391.995, 44100)
stream.write(generate_tone(329.628, 44100))
music += generate_tone(329.628, 44100)

stream.write(generate_tone(293.665, 44100))
music += generate_tone(293.665, 44100)
stream.write(generate_tone(523.251, 44100))
music += generate_tone(523.251, 44100)
stream.write(generate_tone(293.665, 44100))
music += generate_tone(293.665, 44100)
stream.write(generate_tone(261.626, 44100))
music += generate_tone(261.626, 44100)


stream.stop_stream()
stream.close()
p.terminate()


soundFile = wave.open("music.wav", 'wb')
soundFile.setnchannels(channels)
soundFile.setsampwidth(p.get_sample_size(formatting))
soundFile.setframerate(rate)
soundFile.writeframes(b''.join(music))
soundFile.close()
