# Unified Neural Pipeline — Submission by SOHAN

This project contains a simple modular pipeline that simulates a Target Speaker
Diarization + ASR workflow. The goal of this submission is to demonstrate the
pipeline structure, data flow, module organization, and output formatting as
required in the task document.

## Project Structure
- modules/ — individual components of the pipeline  
- sample_inputs/ — test audio generated using a small utility script  
- sample_outputs/ — diarization JSON produced by the pipeline  
- tools/ — helper script used to generate test audio  
- requirements.txt — basic libraries used for file handling  
- submission_statement.txt — declaration for the task

## How to Run
Generate test audio (optional):
~~~
python tools/generate_test_audio.py
~~~

Run the pipeline:
~~~
python modules/main.py --mixture sample_inputs/mixture_audio.wav --target sample_inputs/target_sample.wav
~~~

The output will be saved at:
~~~
sample_outputs/diarization.json
~~~

## Notes
- This is a lightweight mock implementation intended to demonstrate system
  design, not real ASR or diarization.
- Models such as Whisper, pyannote, etc., are not executed due to hardware and
  resource constraints. The focus is on modularity and flow rather than
  heavy model inference.
