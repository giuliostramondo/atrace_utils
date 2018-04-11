#!/bin/bash 

echo -n -e "\t"
for scheme in ReRo ReCo RoCo ReTr
	do echo -n -e "$scheme\t"
done
echo ""
for pattern in 10 20 30 33 40 50 60 66 70 80 90
	do echo -n -e "$pattern\t"
	for scheme in ReRo ReCo RoCo ReTr
		do schedulefilename=pattern_${pattern}percent_${scheme}.schedule
		if [ ! -f $schedulefilename ]; then
			schedulefilename=pattern_${pattern}percent_M_512_N_170_offset_2_${scheme}.schedule
		fi
		echo -n -e "`cat $schedulefilename | wc -l`\t"
	done
echo ""
done 
