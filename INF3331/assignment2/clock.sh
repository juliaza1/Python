#!/bin/bash

bool=true
if [[ $# -gt 0 ]]; then
	flag=$1;
	if  [[ "$flag" = '--AMPM' ]]; then
		while $bool
		do
			clear
			date +%r
			sleep 1
		done
	else 
         echo "use flag '--AMPM' "
	fi
else 
	echo "should not be here"
	while $bool
	do 
		clear
    	date "+%T"
    	sleep 1
    done
fi


