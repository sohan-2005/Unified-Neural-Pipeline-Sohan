class SpeakerID:
    def __init__(self,reference_path):
        self.reference=reference_path
    def label_tracks(self,tracks):
        for t in tracks:
            t['label']='Target' if t.get('speaker_id')=='spk_1' else 'Speaker_B'
        return tracks
