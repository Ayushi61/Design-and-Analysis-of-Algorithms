#!/bin/bash
arg1=$1
grep -oP '("[^"]*["]*)' ${arg1}.txt > ${arg1}_script.txt 
diff  ../${arg1}_dialogues.txt ${arg1}_script.txt > op_diff.txt



