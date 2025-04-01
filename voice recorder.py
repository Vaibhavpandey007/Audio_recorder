import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = int(input("Enter the tieduration in seconds: "))

record_voice = sd.rec(int(seconds * fs), samplerate = fs, channels=2 , dtype = 'int16')
sd.wait()
write("out.wav", fs, record_voice)

print("Finished...\nPlease check 'out.wav'.")
