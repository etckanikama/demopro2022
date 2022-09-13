import pyaudio
import wave

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

def WanWanWan():
    FILE_PATH = "./dog_barking1.wav"
    CHUNK = 256

    wf = wave.open(FILE_PATH, 'rb')
    print(1)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # read data
    data = wf.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()

# def main():
#     WanWanWan()

# if __name__ == "__main__":
#     main()