#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from time import strftime
import math

root = tk.Tk()
root.title("Analog Clock with Digital Display")

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=400, height=400, bg='black')
canvas.pack()

# Create a function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    digital_display.config(text=string)

    canvas.delete("all")

    # Draw clock face
    canvas.create_oval(50, 50, 350, 350, width=4, outline='white')

    # Get the current time
    current_time = strftime('%H:%M:%S').split(':')
    hour, minute, second = map(int, current_time)

    # Draw hour hand
    hour_angle = math.radians(90 - (hour % 12 + minute / 60) * 360 / 12)
    hour_x = 200 + 50 * math.cos(hour_angle)
    hour_y = 200 - 50 * math.sin(hour_angle)
    canvas.create_line(200, 200, hour_x, hour_y, width=6, fill='green')

    # Draw minute hand
    minute_angle = math.radians(90 - (minute + second / 60) * 360 / 60)
    minute_x = 200 + 70 * math.cos(minute_angle)
    minute_y = 200 - 70 * math.sin(minute_angle)
    canvas.create_line(200, 200, minute_x, minute_y, width=4, fill='yellow')

    # Draw second hand
    second_angle = math.radians(90 - (second * 360 / 60))
    second_x = 200 + 80 * math.cos(second_angle)
    second_y = 200 - 80 * math.sin(second_angle)
    canvas.create_line(200, 200, second_x, second_y, width=2, fill='red')

    canvas.after(1000, time)

digital_display = tk.Label(root, font=("calibri", 20, "bold"), background="black", foreground="white")
digital_display.pack()
time()
root.mainloop()


# In[ ]:




