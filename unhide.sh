#!/bin/bash
for file in .a*
do
	new=""
	old=".a"
	fl2=${file//$old/$new}
	mv $file $fl2

done
