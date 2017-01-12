#!/bin/bash
# read variables from command line, one by one:


while [ $# -gt 0 ] # $# = no. of command-line args. -gt = greater than -lt = lower than
do
	option=$1; # load command-line arg into option
	shift; #eat currently first command-line arg
	
	case "$option" in
		S)
			S=$1; 
			declare -i var; var=0
			for arg in $@; do
				if echo $arg | grep -qE ^\-?[0-9]+$; then #if integer
					var=var+arg
				else echo "non-integer input found"; exit;
				fi
			done
			echo "result: $var"
			exit;
			;; # ;; indicates end of case
		P)
			P=$1;
			declare -i var; var=1
			for arg in $@; do
				if echo $arg | grep -qE ^\-?[0-9]+$; then #if integer
					var=var*arg
				else echo "non-integer input found"; exit;
				fi
			done
			echo "result: $var"
			exit ;
			;; # ;; indicates end of case
		M)
			M=$1; 
			declare -i max; max=-2147483648 #setting a max value
			myArray=("$@")

			for n in "${myArray[@]}"; do #looping through array
				((n > max))	&& max=$n #comparing and setting bigger value into max
			done
			echo "result: $max"
			exit ;
			;; # ;; indicates end of case
		m)
			declare -i min; min=2147483648 #setting a min value
			myArray=("$@")

			for n in "${myArray[@]}"; do #looping through array
				((n < min))	&& min=$n #comparing and setting smaller value into min
			done
			echo "result: $min"
			exit ;
			;; # ;; indicates end of case
		*)
			echo "$0: invalid option \"$option\""; exit ;;
	esac
done