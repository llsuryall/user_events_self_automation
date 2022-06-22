#!/bin/python
import constants
from pynput import keyboard

def complete_action():
	prev=open('data/prev','r')

def on_key_press(key):
	event_log=open('data/event_log','a')
	try:
		key_code=key.vk
	except AttributeError:
		key_code=key.value.vk
	if(key_code==92):
		print("Yeah")
		return
	prev=open('data/prev','w')
	prev.truncate()
	event_log.write(f"k,{key_code},1\n")
	prev.write(f"k,{key_code},1\n")
	event_log.close()
	prev.close()

def on_key_release(key):
	event_log=open('data/event_log','a')
	try:
		key_code=key.vk
	except AttributeError:
		key_code=key.value.vk
	if(key_code==92):
		print("Yeah")
		return
	prev=open('data/prev','w')
	prev.truncate()
	prev.write(f"k,{key_code},0\n")
	event_log.write(f"k,{key_code},0\n")
	event_log.close()
	prev.close()

if __name__=='__main__':
	with keyboard.Listener(on_press=on_key_press,on_release=on_key_release) as keyboard_listener:
		keyboard_listener.join()
