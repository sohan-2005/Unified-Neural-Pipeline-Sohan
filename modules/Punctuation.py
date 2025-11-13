class Punctuation:
    def apply(self,transcripts):
        for t in transcripts:
            t['text']=t['text'].capitalize()+'.'
        return transcripts
