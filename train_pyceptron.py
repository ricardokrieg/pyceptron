#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import numpy
from random import random
import Tkinter as tkinter
import threading
import csv

class TrainPyceptron(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

		self.w = None
		self.x = None
		self.n = 0.01
		self.epoch = 0
		self.max_epochs = 1000
		self.n_lines = 0
		self.n_ins = 0

		self.load_x('in.csv')
		self.init_w()

		print 'w:', self.w
		print 'x:', self.x
		print 'd:', self.d
		print 'n:', self.n
	# __init__

	def run(self):
		error = True
		while error:
			error = False

			print '============== epoca %02d ==============' % (self.epoch+1)
			for i, xi in enumerate(self.x):
				u = numpy.dot(xi, self.w)
				y = self.sinal(u)

				print self.w, u, y, self.d[i],

				if y != self.d[i]:
					error = True
					self.hebb(i, y)
				# if
					
				print error
			# for
			self.epoch += 1

			if self.epoch >= self.max_epochs:
				break
		# while

		f = open('pesos', 'w')
		w_str = str(self.w)[1:]
		w_str = w_str[:-1]
		w_str = w_str.replace('   ', ' ')
		w_str = w_str.replace('  ', ' ')
		f.write(w_str)
		f.close()

		if error:
			print 'ABORTED'
		print '+++++++++++++++'
		print 'Resultado:'
		print 'Epocas = %02d' % self.epoch
		print 'w = ', self.w
		print '+++++++++++++++'
	# run

	def degrau(self, u):
		return 1 if u >= 0 else 0
	# degrau

	def sinal(self, u):
		return 1.0 if u >= 0 else -1.0
	# sinal

	def hebb(self, i, y):
		self.w = self.w + self.n*(self.d[i] - y)*self.x[i]
	# hebb

	def init_w(self):
		self.w = numpy.zeros([self.n_ins-1])
		for i in range(0,self.n_ins-1):
			self.w.put([i], [round(random(),4)])
	# init_w

	def load_x(self, file_path):
		reader = csv.reader(open(file_path, 'r'), delimiter=';')
		for row in reader:
			self.n_lines += 1
			self.n_ins = 0
			for param in row:
				self.n_ins += 1
		# for

		reader = csv.reader(open(file_path, 'r'), delimiter=';')
		self.x = numpy.zeros([self.n_lines, self.n_ins-1])
		self.d = numpy.zeros([self.n_lines])

		current_line = 0
		for row in reader:
			for i, param in enumerate(row):
				if i == self.n_ins-1:
					self.d.put([current_line], [float(param)])
				else:
					self.x.put([current_line*self.n_ins+i-current_line], [float(param)])
			# for
			current_line += 1
		# for
	# load_x
# TrainPyceptron

def main():
	#window = tkinter.Tk()
	#window.title('Pyceptron - @ricardokrieg')
	#window.geometry('800x600')
	#window.configure(bg='black')

	train_pyceptron = TrainPyceptron()
	train_pyceptron.start()

	#window.mainloop();
# main

main()