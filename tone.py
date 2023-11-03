import pygame as pg
import numpy as np
import math
import time

pg.init()

bits = 16
sample_rate = 44100
pg.mixer.init(sample_rate, -bits)

#This is the function that creates the sine wave
def sine_x(amplitude, frequency, time):
    return int(round(amplitude * math.sin(2 * math.pi * frequency * time)))

#This is the class that creates the tone
class Tone:
    def sine(freq, duration=1, speaker=None):
        samples = int(round(duration * sample_rate))

        buffer = np.zeros((samples, 2), dtype=np.int16)
        amplitude = 2 ** (bits - 1) - 1

        # Create a linear ramp from 0 to 1 for the duration of the tone
        ramp_up = np.linspace(0, 1, samples)

        # Create a linear ramp from 1 to 0 for the last 10% of the tone
        ramp_down = np.linspace(1, 0, int(samples * 0.1))

        # Loop over the samples and assign the sine wave to the buffer
        for sample in range(samples):
            t = float(sample) / sample_rate
            sine = sine_x(amplitude * ramp_up[sample], freq, t)  # Multiply the amplitude by the ramp value

            # Apply the fade-out effect
            if sample >= samples - len(ramp_down):
                sine *= ramp_down[sample - (samples - len(ramp_down))]

            # Assign the speaker to the tone
            if speaker == 'r':
                buffer[sample][1] = sine
            elif speaker == 'l':
                buffer[sample][0] = sine
            else:
                buffer[sample][0] = sine
                buffer[sample][1] = sine


#this is where the tone is played
        sound = pg.sndarray.make_sound(buffer)
        sound.play(loops = 1, maxtime = int(duration * 1000))
        time.sleep(duration)