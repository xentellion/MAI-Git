#!/bin/bash
function myfunc {
    for file in "$1"/*
    do
    if [ -d "$file" ]
    then
    myfunc $file
    elif [ -f "$file" ]
    then
    echo $(cat $file | tr [:alpha:] a) > "$file"
    fi
    done
}

dir="/mnt/c/Users/89822/Desktop/"
direct="$1"
dir="${dir}${direct}"
echo $num
myfunc $dir
