# Makefile for source rpm: anaconda
# $Id$
NAME := anaconda
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
