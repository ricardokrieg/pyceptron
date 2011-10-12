#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import numpy
import csv

n_ins = 0
n_lines = 0
x = None
w = None

def load_w(file_path):
	global n_ins
	global w

	w = numpy.zeros(n_ins)

	reader = csv.reader(open(file_path, 'r'), delimiter=' ')
	for row in reader:
		for i, param in enumerate(row):
			w.put([i], [param])
# load_w

def load_x(file_path):
	global n_lines
	global n_ins
	global x

	reader = csv.reader(open(file_path, 'r'), delimiter=';')
	for row in reader:
		n_lines += 1
		n_ins = 0
		for param in row:
			n_ins += 1
	
	reader = csv.reader(open(file_path, 'r'), delimiter=';')
	x = numpy.zeros([n_lines, n_ins])

	current_line = 0
	for row in reader:
		for i, param in enumerate(row):
			x.put([current_line*n_ins+i], [float(param)])
		current_line += 1
# load_x

def degrau(u):
	return 1 if u >= 0 else 0
# degrau

def sinal(u):
	return 1.0 if u >= 0 else -1.0
# sinal

def execute():
	global w
	global x

	print 'Entrada = ', x
	print 'Pesos = ', w

	for xi in x:
		u = numpy.dot(xi, w)
		y = sinal(u)

		print 'Saída = ', y
	# for
# execute

def main():
	global w
	global x

	load_x('in2.csv')
	load_w('pesos')

	#if len(sys.argv)-1 != AMOUNT_IN:
	#	print 'Este pyceptron espera %d entradas' % AMOUNT_IN
	#	exit()
	#else:
	#	x.put([0], [-1])
	#	for i, param in enumerate(sys.argv):
	#		if i > 0 : x.put([i], [param])

	execute()
# main

main()