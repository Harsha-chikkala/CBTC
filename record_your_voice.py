import sounddevice as sd
from scipy.io.wavfile import write
import time

def record_audio():
    try: 
        desired_time = int(input("Enter the number of seconds you want to record: "))
        print("Recording Started")
        print(f"Recording for {desired_time} seconds...")
        recording = sd.rec(int(desired_time * 44100), samplerate=44100, channels=2)
        for i in reversed(range(0, desired_time + 1)):
            seconds = i % 60
            minutes = int(i / 60) % 60
            hours = int(i / 3600)
            print(f"\rTime remaining: {hours:02}:{minutes:02}:{seconds:02}", end='', flush=True)
            time.sleep(1)

        print("\nTime's up!")

        sd.wait() 
        filename = "demo.wav"
        write(filename, 44100, recording)
        
        print(f"Recording ended. Your audio has been saved as '{filename}'")
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")

record_audio()
