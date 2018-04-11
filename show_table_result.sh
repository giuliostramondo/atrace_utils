#!/bin/bash 

echo -n "   ";for scheme in ReRo ReCo RoCo ReTr;do echo -n "$scheme  ";done;echo "";for pattern in 10 30 50 70;do echo -n "$pattern ";for scheme in ReRo ReCo RoCo ReTr;do echo -n "`cat pattern_${pattern}percent_${scheme}.schedule | wc -l`  ";done;echo "";done 
