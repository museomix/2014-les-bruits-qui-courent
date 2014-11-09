#!/usr/bin/env python

import serial
import re
from pygame import mixer
import pygame as pyg_
import ast, time

class Sound:
    def __init__(self, channel, sound):
        self.channel = mixer.Channel(channel)
        self.sound = mixer.Sound(open(sound))
        self.playing = False

    def play(self, loops=0):
        self.channel.play(self.sound, loops=loops)
        self.playing = True

    def stop(self):
        self.channel.stop()
        self.playing = False

    def pause(self):
        self.channel.pause()
        self.playing = False

    def unpause(self):
        self.channel.unpause()
        self.playing = True

class Serial:
    parser = re.compile(r"<(True|False):([0-9]+)>")
    def  __init__(self, serial_name):
        #self.ser = open("test.ser")
        self.ser = serial.Serial(serial_name, 9600)
        self.distances = []

    def get_distance(self):
        input_ = self.ser.readline()[:-1]
#        print input_
        match = self.parser.match(input_)
        if not match:
            return self.distances
    
        if len(self.distances) == 5:
            self.distances = self.distances[1:]
    
        _, distance = match.groups()
        self.distances.append(int(distance))
        return self.distances

    def __gt__(self, than):
        #print "gt"
        return all(d>than for d in self.distances)

    def __lt__(self, than):
#        print "lt"
        return all(d<than for d in self.distances)


if __name__ == "__main__":
    # INIT SOUNDS
    mixer.init(frequency=44100, channels=2)
    text = Sound(0, "/usr/share/vacarme/dialogue_horloge.wav")
    
    # INIT SERIAL
    ser = Serial('/dev/ttyACM0')
    
    text_pause = 0

    while True:
    
        distances = ser.get_distance()
    
        if ser<140 and not text.playing:
            print "start playing %d", time.time() - text_pause
            if time.time() - text_pause < 10:
                text.unpause()
            else:
                text.stop()
                text.play()
            
    
        if ser>150 and text.playing:
            print "stop text"
            text.pause()
            text_pause = time.time()

