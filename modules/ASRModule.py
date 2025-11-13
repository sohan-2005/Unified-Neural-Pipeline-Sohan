class ASRModule:
    def transcribe_tracks(self,tracks):
        out=[]
        for t in tracks:
            out.append({'speaker':t['label'],'start':0.0,'end':3.0,'text':'example text','confidence':0.9})
        return out
    