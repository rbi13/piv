#!/bin/bash

INPUT=$*
STRINGNUM=0
ary=($INPUT)
LANG="en"

# ping -c 1 "translate.google.com"
# if [ $? != 0 ] 
# then 
# 	exit 1
# fi

GOOGLE="http://translate.google"
VOICE=".co.uk"
# if [ $1 != "-l" -a $2 == "us" ]
# then
# 	INPUT="${*:3}"
# 	VOICE=".com"
# else
# 	VOICE=".co.uk"
# fi


for key in "${!ary[@]}"
do
SHORTTMP[$STRINGNUM]="${SHORTTMP[$STRINGNUM]} ${ary[$key]}"
LENGTH=$(echo ${#SHORTTMP[$STRINGNUM]})
#echo "word:$key, ${ary[$key]}"
#echo "adding to: $STRINGNUM"
if [[ "$LENGTH" -lt "100" ]]; then
#echo starting new line
SHORT[$STRINGNUM]=${SHORTTMP[$STRINGNUM]}
else
STRINGNUM=$(($STRINGNUM+1))
SHORTTMP[$STRINGNUM]="${ary[$key]}"
SHORT[$STRINGNUM]="${ary[$key]}"
fi
done
for key in "${!SHORT[@]}"
do
#echo "line: $key is: ${SHORT[$key]}"
# echo "Playing line: $(($key+1)) of $(($STRINGNUM+1))"
mpg123 -q $GOOGLE$VOICE"/translate_tts?tl="$LANG"&q=${SHORT[$key]}"
done

exit 0