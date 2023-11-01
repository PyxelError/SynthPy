import threading as th

from utilities import NOTE_MAP
from tone import Tone

class Note:
    def __init__(self, note_string, duration=1):
        note = note_string[0].upper()
        self.note_string = note + note_string[1:]
        self.duration = duration
        self.frequency = NOTE_MAP[self.note_string]

    def play(self, speaker=None):
        Tone.sine(self.frequency, self.duration, speaker=speaker)

    @staticmethod
    def Play_chord(notes_list):
        note_threads = []

        for note in notes_list:
            note_thread = th.Thread(target=note.play)
            note_threads.append(note_thread)

        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()
