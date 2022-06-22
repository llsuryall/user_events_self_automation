#!/bin/python
from constants import mouse_cell_width,mouse_cell_height
from pynput import mouse

def on_mouse(x,y,button,pressed):
	x=int(x/mouse_cell_width)
	y=int(y/mouse_cell_height)
	event_log=open('data/event_log','a')
	prev=open('data/prev','w')
	pressed_type='1' if pressed else '0'
	button_type='L' if button==mouse.Button.left else 'R'
	prev.write(f"m,{x},{y},{button_type},{pressed_type}\n")
	event_log.write(f"m,{x},{y},{button_type},{pressed_type}\n")
	event_log.close()
	prev.close();

if __name__=='__main__':
	with mouse.Listener(on_click=on_mouse) as mouse_listener:
		mouse_listener.join()
