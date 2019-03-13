"""
Mateus H. Ittner - 12/03/19

Alarm Clock - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

---
https://docs.python.org/3/library/time.html

"""

import time

def particulartime(time):
	now = time.localtime(time.time())
	print(f"{now.tm_hour:02d}:{now.tm_min:02d}")
	print("\a")



while True: 
	alarm_type = input("[1] - Play an alarm at a particular time\n[2] - Play an alarm in X minutes.\n")
	if alarm_type == 1:
		while True:
			input("\nInform a time for the alarm:\n")
			hour = input("\nHour:")
			minutes = input("\nMinutes:")
			time = {}






