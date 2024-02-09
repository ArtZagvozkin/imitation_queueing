#!/bin/python3
#Artem Zagvozkin

import time
import _thread
import queue
import random
from tkinter import *
from datetime import datetime


class Paint:
    def __init__(self, panel):

        # Canvas
        self.__myCanvas = Canvas(width=200, height=200, bg='white')
        panel.add(self.__myCanvas)

        ###draw q-schema###
        #Source
        self.__source = self.__add_channel(75, 200, 125, 250, "S")
        self.__s_to_q1 =  self.__add_line(125, 225, 200, 225, "last", 75)

        #PC1
        self.__q1 = self.__add_queue(185, 200, 265, 250)
        self.__q1_to_ch1 =  self.__add_line(265, 225, 315, 225, "last", 50)
        self.__ch1 =  self.__add_channel(315, 200, 365, 250, "C1")
        self.__ch1_to_ch2 = self.__add_line(365, 225, 415, 225, "last", 50)
        self.__ch2 =  self.__add_channel(415, 200, 465, 250, "C2")

        #PC2
        self.__q2 = self.__add_queue(185, 350, 265, 400)
        self.__q2_to_ch3 =  self.__add_line(265, 375, 315, 375, "last", 50)
        self.__ch3 = self.__add_channel(315, 350, 365, 400, "C3")
        self.__ch3_to_ch4 = self.__add_line(365, 375, 415, 375, "last", 50)
        self.__ch4 = self.__add_channel(415, 350, 465, 400, "C4")

        #PC1-PC2
        self.__pc1_to_pc2_1 = self.__add_line(340, 250, 340, 300, "first", 2)
        self.__pc1_to_pc2_2 = self.__add_line(340, 300, 160, 300, "none", 2)
        self.__pc1_to_pc2_3 = self.__add_line(160, 300, 160, 375, "none", 2)
        self.__pc1_to_pc2_4 = self.__add_line(160, 375, 200, 375, "last", 2)

        #out
        self.__out_1 = self.__add_line(465, 225, 515, 225, "none", 50)
        self.__out_2 = self.__add_line(465, 375, 515, 375, "none", 50)
        self.__out_3 = self.__add_line(515, 225, 515, 300, "none", 75)
        self.__out_4 = self.__add_line(515, 375, 515, 300, "none", 75)
        self.__out_5 = self.__add_line(515, 300, 565, 300, "last", 50)


    def anim_source(self, duration, speed):
        _thread.start_new_thread(self.__anim_channel, (duration, speed, self.__source, ))

    def source_reset(self):
        _thread.start_new_thread(self.__reset_obj, (self.__source, ))


    def anim_s_to_q1(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [self.__s_to_q1], ))


    def anim_queue_1(self, duration, speed):
        _thread.start_new_thread(self.__anim_queue, (duration, speed, self.__q1, ))

    def queue_1_reset(self):
        _thread.start_new_thread(self.__reset_obj, (self.__q1, ))


    def anim_q1_to_ch1(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [self.__q1_to_ch1], ))


    def anim_channel_1(self, duration, speed):
        _thread.start_new_thread(self.__anim_channel, (duration, speed, self.__ch1, ))

    def reset_channel_1(self):
        _thread.start_new_thread(self.__reset_obj, (self.__ch1, ))


    def anim_ch1_to_ch2(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [self.__ch1_to_ch2], ))


    def anim_ch2_to_out(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [
                                                        self.__out_1,
                                                        self.__out_3,
                                                        self.__out_5
                                                        ], ))


    def anim_queue_2(self, duration, speed):
        _thread.start_new_thread(self.__anim_queue, (duration, speed, self.__q2, ))

    def queue_2_reset(self):
        _thread.start_new_thread(self.__reset_obj, (self.__q2, ))


    def anim_q2_to_ch2(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [self.__q2_to_ch3], ))


    def anim_channel_2(self, duration, speed):
        _thread.start_new_thread(self.__anim_channel, (duration, speed, self.__ch2, ))

    def reset_channel_2(self):
        _thread.start_new_thread(self.__reset_obj, (self.__ch2, ))


    def anim_channel_3(self, duration, speed):
        _thread.start_new_thread(self.__anim_channel, (duration, speed, self.__ch3, ))

    def reset_channel_3(self):
        _thread.start_new_thread(self.__reset_obj, (self.__ch3, ))

    def anim_ch3_to_ch4(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [self.__ch3_to_ch4], ))

    def anim_channel_4(self, duration, speed):
        _thread.start_new_thread(self.__anim_channel, (duration, speed, self.__ch4, ))

    def reset_channel_4(self):
        _thread.start_new_thread(self.__reset_obj, (self.__ch4, ))


    def anim_ch4_to_out(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed, [
                                                        self.__out_2,
                                                        self.__out_4,
                                                        self.__out_5
                                                        ], ))


    def anim_pc1_to_pc2(self, duration, speed):
        _thread.start_new_thread(self.__anim_line, (duration, speed,
                                                        [self.__pc1_to_pc2_1,
                                                        self.__pc1_to_pc2_2,
                                                        self.__pc1_to_pc2_3,
                                                        self.__pc1_to_pc2_4
                                                        ], ))


    def __anim_channel(self, duration, speed, channel):
        num_of_iter = 100

        #animate channel
        for i in range(num_of_iter-3):
            self.__myCanvas.itemconfig(channel, start=90, extent=(1+i)*-3.71, fill="#00db6a")
            time.sleep(duration/num_of_iter/speed)


    def __anim_queue(self, duration, speed, queue):
        num_of_iter = 100

        #get step
        x1, y1, x2, y2 =  self.__myCanvas.coords(queue)
        value = x2 - x1
        step = value / num_of_iter

        #animate queue
        self.__myCanvas.itemconfig(queue, fill="#00db6a")
        self.__myCanvas.coords(queue, x1, y1, 0, y2)
        for i in range(num_of_iter):
            self.__myCanvas.coords(queue, x1, y1, x1+step*(i+1), y2)
            time.sleep(duration/num_of_iter/speed)

        # self.__myCanvas.itemconfig(queue, fill="")
        self.__myCanvas.coords(queue, x1, y1, x2, y2)


    def __anim_line(self, duration, speed, lines):
        num_of_iter = 100


        length_full = 0
        for line in lines:
            x1, y1, x2, y2 =  self.__myCanvas.coords(line)
            length_full += int(((x1-x2)**2 + (y1-y2)**2)**0.5)


        for line in lines:
            x1, y1, x2, y2 =  self.__myCanvas.coords(line)
            length = ((x1-x2)**2 + (y1-y2)**2)**0.5
            step_x = (x2-x1)/length
            step_y = (y2-y1)/length

            progress = self.__myCanvas.create_oval(x1-4, y1-4, x1+4, y1+4, fill="#00db6a", outline="")
            for i in range(int(length)):
                self.__myCanvas.coords(progress, x1-4 + step_x*i, y1-4 + step_y*i, x1+4 + step_x*i, y1+4 + step_y*i)
                time.sleep(duration/length_full/speed)

            self.__myCanvas.delete(progress)

    def __reset_obj(self, obj):
        self.__myCanvas.itemconfig(obj, fill="")


    def __add_channel(self, x1, y1, x2, y2, text1):
        channel = self.__myCanvas.create_arc((x1, y1, x2, y2), outline="")
        self.__myCanvas.create_oval((x1, y1, x2, y2), outline="black")
        self.__myCanvas.create_text((x1+x2)/2, (y1+y2)/2, text=text1)

        return channel


    def __add_queue(self, x1, y1, x2, y2):
        step = (x2-x1)/5

        queue = self.__myCanvas.create_rectangle((x1+step, y1, x2, y2), fill="", outline="")

        self.__myCanvas.create_line(x1, y1, x2, y1)
        self.__myCanvas.create_line(x1, y2, x2, y2)

        self.__myCanvas.create_line(x1+step, y1, x1+step, y2)
        self.__myCanvas.create_line(x1+step*2, y1, x1+step*2, y2)
        self.__myCanvas.create_line(x1+step*3, y1, x1+step*3, y2)
        self.__myCanvas.create_line(x1+step*4, y1, x1+step*4, y2)
        self.__myCanvas.create_line(x1+step*5, y1, x1+step*5, y2)

        return queue


    def __add_line(self, x1, y1, x2, y2, type_arrow, dash_pattern):
        return self.__myCanvas.create_line(x1, y1, x2, y2, arrow=type_arrow, dash=(dash_pattern))


    def main_loop(self):
        self.__window.mainloop()

def press_btn():
    paint.anim_source(2, 1)
    paint.anim_s_to_q1(2, 1)
    paint.anim_queue_1(2, 1)
    paint.anim_q1_to_ch1(2, 1)
    paint.anim_channel_1(2, 1)
    paint.anim_ch2_to_out(2, 1)

    paint.anim_queue_2(2, 1)
    paint.anim_q2_to_ch2(2, 1)
    paint.anim_channel_3(2, 1)
    paint.anim_ch2_to_out(2, 1)

    paint.anim_pc1_to_pc2(2, 1)




window = Tk()
window.title("Модель обработки запросов")
window.geometry('800x600')
window.resizable(width=False, height=False)
basePnl = PanedWindow(orient=VERTICAL)
basePnl.pack(fill=BOTH, expand=1)

btn = Button(text="Старт", width=15, command=press_btn)
basePnl.add(btn)

paint = Paint(basePnl)

stat_ch1, stat_ch2, stat_ch3, stat_ch4, stat_q1, stat_q2 = (True, True, True, True, False, False)
que_1 = queue.Queue()
que_2 = queue.Queue()

speed = 10


def start_source(id_rec, max):
    paint.anim_source(30, speed)
    time.sleep(30/speed)
    paint.source_reset()

    _thread.start_new_thread(start_s_to_q1, (id_rec, ))

    start_source(id_rec+1, 0)


def start_s_to_q1(id_rec):
    global stat_q1

    paint.anim_s_to_q1(2, speed)
    time.sleep(2/speed)

    que_1.put(id_rec)
    print("queue 1: ", que_1.qsize())

    if stat_q1 == False:
        stat_q1 = True
        _thread.start_new_thread(start_queue_1, ())


def start_queue_1():
    global que_1, stat_q1, stat_ch1

    if stat_q1 == False:
        return

    if que_1.qsize() == 0:
        return

    cur_time = 17 + random.randint(1, 6)
    paint.anim_queue_1(cur_time, speed)
    time.sleep(cur_time/speed)

    id_rec = que_1.get()
    print("queue 1: ", que_1.qsize())

    #wait channel 1
    while not(stat_ch1):
        time.sleep(0.0001)
    paint.queue_1_reset()
    _thread.start_new_thread(start_q1_to_ch1, (id_rec, ))

    if que_1.qsize() == 0:
        stat_q1 = False

    start_queue_1()


def start_q1_to_ch1(id_rec):
    paint.anim_q1_to_ch1(2, speed)
    time.sleep(2/speed)
    _thread.start_new_thread(start_channel_1, (id_rec, ))


def start_channel_1(id_rec):
    global stat_ch1
    stat_ch1 = False

    paint.anim_channel_1(1, speed)
    time.sleep(1/speed)

    if id_rec % 2 == 0:
        while not(stat_ch2):
            time.sleep(0.0001)
        paint.reset_channel_1()
        stat_ch1 = True
        _thread.start_new_thread(start_ch1_to_ch2, (id_rec, ))
    else:
        paint.reset_channel_1()
        stat_ch1 = True
        _thread.start_new_thread(anim_pc1_to_pc2, (id_rec, ))


def start_ch1_to_ch2(id_rec):
    paint.anim_ch1_to_ch2(2, speed)
    time.sleep(2/speed)

    start_channel_2(id_rec)


def start_channel_2(id_rec):
    global stat_ch2
    stat_ch2 = False

    cur_time = 18 + random.randint(1, 4)
    paint.anim_channel_2(cur_time, speed)
    time.sleep(cur_time/speed)
    paint.reset_channel_2()
    stat_ch2 = True

    _thread.start_new_thread(start_ch2_to_out, (id_rec, ))


def start_ch2_to_out(id_rec):
    paint.anim_ch2_to_out(2, speed)
    time.sleep(2/speed)


def anim_pc1_to_pc2(id_rec):
    global que_2, stat_q2

    paint.anim_pc1_to_pc2(2, speed)
    time.sleep(2/speed)

    que_2.put(id_rec)
    print("queue 2: ", que_2.qsize())

    if stat_q2 == False:
        stat_q2 = True
        _thread.start_new_thread(start_queue_2, ())


def start_queue_2():
    global que_2, stat_q2, stat_ch3

    if stat_q2 == False:
        return

    if que_2.qsize() == 0:
        return

    cur_time = 17 + random.randint(1, 6)
    paint.anim_queue_2(cur_time, speed)
    time.sleep(cur_time/speed)

    id_rec = que_2.get()
    print("queue 2: ", que_2.qsize())

    #wait channel 2
    while not(stat_ch3):
        time.sleep(0.0001)
    _thread.start_new_thread(start__q2_to_ch3, (id_rec, ))

    if que_2.qsize() == 0:
        stat_q2 = False

    start_queue_2()


def start__q2_to_ch3(id_rec):
    paint.anim_q2_to_ch2(2, speed)
    time.sleep(2/speed)
    _thread.start_new_thread(start_channel_3, (id_rec, ))


def start_channel_3(id_rec):
    global stat_ch3
    stat_ch3 = False

    paint.anim_channel_3(1, speed)
    time.sleep(1/speed)

    #wait channel 4
    while not(stat_ch4):
        time.sleep(0.0001)

    paint.reset_channel_3()
    stat_ch3 = True

    _thread.start_new_thread(start_ch3_to_ср4, (id_rec, ))


def start_ch3_to_ср4(id_rec):
    paint.anim_ch3_to_ch4(2, speed)
    time.sleep(2/speed)

    start_channel_4(id_rec)

def start_channel_4(id_rec):
    global stat_ch4
    stat_ch4 = False

    cur_time = 18 + random.randint(1, 4)
    paint.anim_channel_4(cur_time, speed)
    time.sleep(cur_time/speed)

    paint.reset_channel_4()
    stat_ch4 = True

    _thread.start_new_thread(start_ch4_to_out, (id_rec, ))


def start_ch4_to_out(id_rec):
    paint.anim_ch4_to_out(2, speed)
    time.sleep(2/speed)



_thread.start_new_thread(start_source, (1, 0, ))



window.mainloop()

