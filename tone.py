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
    def sine(freq, duration = 1 , speaker = None):
        samples = int(round(duration * sample_rate))

        buffer = np.zeros((samples, 2), dtype = np.int16)
        amplitude = 2 ** (bits - 1) - 1

#we are looping over the samples and assigning the sine wave to the buffer
        for sample in range(samples):
            t = float(sample) / sample_rate
            sine = sine_x(amplitude, freq, t)

#This is where I'm assigning the speaker to the tone
            if speaker == 'r':
                buffer[sample][1] = sine
            if speaker == 'l':
                buffer[sample][0] = sine

            else:
                buffer[sample][0] = sine
                buffer[sample][1] = sine

#this is where the tone is played
        sound = pg.sndarray.make_sound(buffer)
        sound.play(loops = 1, maxtime = int(duration * 1000))
        time.sleep(duration)