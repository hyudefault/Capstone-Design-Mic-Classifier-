import threading
import pyaudio
import os
import struct
import numpy as np
from scipy.fftpack import fft
import time
from bluetooth import *

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
#client_socket = BluetoothSocket(RFCOMM)
#client_socket.connect(("20:16:05:20:16:23", 1))

amplitude = [0, 0, 0, 0]

thread_num = -1

result = ["----", "----", "----", "----"]
direction_flag = ["", "", "", ""]

mic_object = pyaudio.PyAudio()

class mic(threading.Thread):

    DEVICE_INDEX_NUM = -1

    stream = ""

    thread_num = ""
    
    def __init__(self, __DEVICE_INDEX_NUM):

            threading.Thread.__init__(self)

	    self.DEVICE_INDEX_NUM = __DEVICE_INDEX_NUM

	    print("mic " + str(self.DEVICE_INDEX_NUM) + " init")

    def run(self):

	    global result

	    global mic_object

	    global thread_num

	    global CHUNK
	    global FORMAT
	    global CHANNELS
	    global RATE

	    global amplitude

	    self.stream = mic_object.open(
		format=FORMAT,
		channels=1,
		rate=RATE,
		input=True,
		output=False,
		frames_per_buffer=CHUNK,
		input_device_index = self.DEVICE_INDEX_NUM
	    )
	    print("mic " + str(self.DEVICE_INDEX_NUM) + " stream open")

	    x = np.arange(0, 2 * CHUNK, 2)
	    xf = np.linspace(0, RATE, CHUNK)
	    print('Stream started')
	    print('Current mic device : ' + str(self.DEVICE_INDEX_NUM))

	    while True:
		
		if(self.stream.get_read_available()):

			data = self.stream.read(CHUNK, exception_on_overflow=False)
			data_int = struct.unpack(str(2 * CHUNK) + 'B', data)
			yf = fft(data_int)
			if np.any(np.abs(yf[122:124]) / (128 * CHUNK) > 0.2):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[123]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    if np.any((np.abs(yf[123]) / (128 * CHUNK)) - (np.abs(yf[105]) / (128 * CHUNK)) > -0.2) and np.any((np.abs(yf[123]) / (128 * CHUNK)) - (np.abs(yf[105]) / (128 * CHUNK)) < -0.1):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn 153057")
				result[self.DEVICE_INDEX_NUM] = "horn 153057"

			elif np.any(np.abs(yf[118]) / (128 * CHUNK) > 0.6):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[118]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    print("mic" + str(self.DEVICE_INDEX_NUM) + " : 2500~2600")
			    if np.any((np.abs(yf[118]) / (128 * CHUNK)) - (np.abs(yf[103]) / (128 * CHUNK)) > 0.02) and np.any((np.abs(yf[118]) / (128 * CHUNK)) - (np.abs(yf[103]) / (128 * CHUNK)) < 0.6):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn 145577")
				result[self.DEVICE_INDEX_NUM] = "horn 145577"

			elif np.any(np.abs(yf[106]) / (128 * CHUNK) > 0.3):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[106]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    print("mic" + str(self.DEVICE_INDEX_NUM) + " : 2200~2300")
			    if np.any((np.abs(yf[106]) / (128 * CHUNK)) - (np.abs(yf[88]) / (128 * CHUNK)) > 0.01) and np.any((np.abs(yf[106]) / (128 * CHUNK)) - (np.abs(yf[88]) / (128 * CHUNK)) < 0.2):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn youtube1")
				result[self.DEVICE_INDEX_NUM] = "horn youtube1"

			elif np.any(np.abs(yf[107]) / (128 * CHUNK) > 0.3):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[107]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    print("mic" + str(self.DEVICE_INDEX_NUM) + " : 2200~2300")
			    if np.any((np.abs(yf[107]) / (128 * CHUNK)) - (np.abs(yf[88]) / (128 * CHUNK)) > 0.01) and np.any((np.abs(yf[107]) / (128 * CHUNK)) - (np.abs(yf[88]) / (128 * CHUNK)) < 0.2):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn youtube1")
				result[self.DEVICE_INDEX_NUM] = "horn youtube1"

			elif np.any(np.abs(yf[105]) / (128 * CHUNK) > 0.3):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[105]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3])) 
			    print("mic" + str(self.DEVICE_INDEX_NUM) + " : 2200~2300")
			    if np.any((np.abs(yf[105]) / (128 * CHUNK)) - (np.abs(yf[139]) / (128 * CHUNK)) > 0.05) and np.any((np.abs(yf[105]) / (128 * CHUNK)) - (np.abs(yf[139]) / (128 * CHUNK)) < 0.2):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn 58202")
				result[self.DEVICE_INDEX_NUM] = "horn 58202"

			elif np.any(np.abs(yf[124]) / (128 * CHUNK) > 0.3):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[124]) / (128 * CHUNK)
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3])) 
			    print("mic" + str(self.DEVICE_INDEX_NUM) + " : 2600~2700")
			    if np.any((np.abs(yf[124]) / (128 * CHUNK)) - (np.abs(yf[137]) / (128 * CHUNK)) > 0.1) and np.any((np.abs(yf[124]) / (128 * CHUNK)) - (np.abs(yf[137]) / (128 * CHUNK)) < 0.2):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : horn 54187")
				result[self.DEVICE_INDEX_NUM] = "horn 54187"

			elif np.any(np.abs(yf[33]) / (128 * CHUNK) > 0.4):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[33]) / (128 * CHUNK)  
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    if np.any((np.abs(yf[33]) / (128 * CHUNK)) - (np.abs(yf[66]) / (128 * CHUNK)) > 0.1) and np.any((np.abs(yf[33]) / (128 * CHUNK)) - (np.abs(yf[66]) / (128 * CHUNK)) < 0.6):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : siren 62878")
				result[self.DEVICE_INDEX_NUM] = "siren 62878"

			elif np.any(np.abs(yf[69]) / (128 * CHUNK) > 0.65):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[69]) / (128 * CHUNK)  
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    if np.any(np.abs(yf[138]) / (128 * CHUNK) > 0.02) and np.any(np.abs(yf[138]) / (128 * CHUNK) < 0.2):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : siren 98525")
				result[self.DEVICE_INDEX_NUM] = "siren 98525"

			elif np.any(np.abs(yf[80]) / (128 * CHUNK) > 0.6):
			    amplitude[self.DEVICE_INDEX_NUM] = np.abs(yf[80]) / (128 * CHUNK) 
			    print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
			    if np.any((np.abs(yf[80]) / (128 * CHUNK)) - (np.abs(yf[60]) / (128 * CHUNK)) > 0.2) and np.any((np.abs(yf[80]) / (128 * CHUNK)) - (np.abs(yf[60]) / (128 * CHUNK)) < 0.45):
				print("mic" + str(self.DEVICE_INDEX_NUM) + " : siren 94636")
				result[self.DEVICE_INDEX_NUM] = "siren 94636"
			else:
			    amplitude[self.DEVICE_INDEX_NUM] = 0
			    result[self.DEVICE_INDEX_NUM] = "----"


def checker():

    global result

    global direction_flag

    global amplitude

    while True:

        print("Amplitude [0] : " + str(amplitude[0]) + " Amplitude [1] : " + str(amplitude[1]) + " Amplitude [2] : " + str(amplitude[2]) + " Amplitude [3] : " + str(amplitude[3]))
        #if (result is not ""):
            #if (amplitude[0] > amplitude[1]) and (amplitude[0] > amplitude[2]): 
            #    direction_flag = 'behind' 
            #    print("RESULT : " + result[0] + " ("+ direction_flag +")")

            #if (amplitude[1] > amplitude[0]) and (amplitude[1] > amplitude[2]):
            #    direction_flag = 'left' 
            #    print("RESULT : " + result[1] + " ("+ direction_flag +")")

            #if (amplitude[2] > amplitude[0]) and (amplitude[2] > amplitude[1]):
            #    direction_flag = 'right' 
            #    print("RESULT : " + result[2] + " ("+ direction_flag +")")

        time.sleep(0.1)
	#if (result[0] is not "") or (result[1] is not "") or (result[2] is not "") or (result[3] is not ""):
        #     print(result[0] + " " + result[1] + " " + result[2] + " " + result[3])


mic_thread1 = mic(2)
mic_thread2 = mic(3)

mic_thread1.start()
mic_thread2.start()

checker_thread = threading.Thread(target=checker, args=())
checker_thread.start()

#mic_thread3 = threading.Thread(target=mic, args=(4, ))
#mic_thread3.start()

#LED_thread = threading.Thread(target=LED_control, args=())
#LED_thread.start()
#print("LED control thread started")
