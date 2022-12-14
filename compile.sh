#!/bin/sh




case "$1" in
    6)
	    gcc -O2 -Wall -o 6-signal 6-signal.c
	    ;;
	8)
	    gcc -O2 -Wall -o 8-forest 8-forest.c
	    ;;
	*) # surely I mean the newest one
	    gcc -O2 -Wall -o 8-forest 8-forest.c
	    ;;
esac
