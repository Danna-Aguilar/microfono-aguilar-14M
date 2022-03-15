import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

#formato de audio
frecuencia_muestreo = 44100
canales = 1
profundidad_bits= 'float64'

duracion = 5.3 

grabacion = sd.rec(
    int(duracion * frecuencia_muestreo), #total de frames (mstras)
    samplerate= frecuencia_muestreo, # frecuencia de myestreo
    channels = 1,                    #cantidad de canales
    dtype= profundidad_bits )        # profunndidad de bits (tipo de dato)
    