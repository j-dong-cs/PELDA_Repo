#! /usr/bin/python
#
# Copyright 2014 All Rights Reserved
# Author: Robert Bezirganyan (robbez@uw.edu)


class LableGenerator:
    def __init__(self, matchQueue, totalRows, timeInterval):
        self.matchQueue = matchQueue
        self.totalRows = totalRows
        self.timeInterval = timeInterval
        self.counter = 0
        self.match = None
        self.nextLabel = 'NO'


    def generate(self):

        self.match = self.matchQueue.get()
        labels = [self.nextLabel] * self.totalRows

        for row in range(self.totalRows):
            if self.counter >= self.match[0] and self.counter <= self.match[1]:
                self.nextLabel = 'YES'
            else:
                self.nextLabel = 'NO'

            labels[row] = self.nextLabel

            self.counter += self.timeInterval
            if self.counter > self.match[1]:
                if not self.matchQueue.empty():
                    self.match = self.matchQueue.get()
                else:
                    break

        return labels