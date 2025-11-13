import json,os
class JSONWriter:
    def __init__(self,output_dir='sample_outputs'):
        self.output_dir=output_dir
        os.makedirs(self.output_dir,exist_ok=True)
    def write(self,transcripts):
        out_path=os.path.join(self.output_dir,'diarization.json')
        with open(out_path,'w') as f:
            json.dump(transcripts,f,indent=2)
            