from tone import Tone
from note import Note   

#Tone.sine(440, duration = .1)

Note.Play_chord([Note('C4', 1), Note('A4', 1)])
Note.Play_chord([Note('C4', 1), Note('G4', 1)])
Note('C4', 1).play()
Note.Play_chord([Note('C5', 1), Note('A5', 1)])
Note.Play_chord([Note('C5', 1), Note('G5', 1)])
Note('C5', 1).play()