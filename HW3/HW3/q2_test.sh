#!/bin/bash
arg1=$1
read -r -p "enter search string :" search
grep -o "$search" ../${arg1}_dialogues.txt | wc -l
