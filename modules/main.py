import argparse
from NoiseReducer import NoiseReducer
from Separator import Separator
from SpeakerID import SpeakerID
from ASRModule import ASRModule
from Punctuation import Punctuation
from JSONWriter import JSONWriter

def run_pipeline(mixture_path,target_path,output_dir):
    denoiser=NoiseReducer()
    clean=denoiser.process(mixture_path)
    separator=Separator()
    tracks=separator.separate(clean)
    spkid=SpeakerID(target_path)
    labeled=spkid.label_tracks(tracks)
    asr=ASRModule()
    transcripts=asr.transcribe_tracks(labeled)
    punct=Punctuation()
    final=punct.apply(transcripts)
    writer=JSONWriter(output_dir)
    writer.write(final)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--mixture',required=True)
    p.add_argument('--target',required=True)
    p.add_argument('--output',default='sample_outputs')
    args=p.parse_args()
    run_pipeline(args.mixture,args.target,args.output)
