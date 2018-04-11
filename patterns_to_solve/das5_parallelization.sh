#!/bin/bash

for p in $(ls | grep atrace )
	do echo $p
	for scheme in ReRo ReCo RoCo ReTr
		do prun -np 1 ../schedule_atrace.py $p $scheme &
	done
done
