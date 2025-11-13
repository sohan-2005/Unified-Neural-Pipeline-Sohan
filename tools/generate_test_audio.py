import numpy as np
import soundfile as sf

def generate_test_audio(filename, duration=4, freq=440, sr=16000):
    t = np.linspace(0, duration, sr * duration, endpoint=False)
    tone = 0.2 * np.sin(2 * np.pi * freq * t)
    sf.write(filename, tone, sr)
    print(f"Generated audio file saved as: {filename}")

if __name__ == "__main__":
    generate_test_audio("sample_inputs/mixture_audio.wav", duration=4, freq=440)

    generate_test_audio("sample_inputs/target_sample.wav", duration=4, freq=600)

    generate_test_audio("sample_inputs/target_sample2.wav", duration=5, freq=800)
