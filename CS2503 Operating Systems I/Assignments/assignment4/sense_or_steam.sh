#!/bin/bash

INFILE=sense.txt
PREVIOUS=0
PREVIOUS2=0
TREND="N"
PREVIOUS_TREND="N"

for LINE in $(cat "$INFILE")
do
        if [ "$LINE" -lt "$PREVIOUS" ]  && [ "$PREVIOUS" -lt "$PREVIOUS2" ]; then
                TREND="D"
        elif [ "$LINE" -gt "$PREVIOUS" ] && [ "$PREVIOUS" -gt "$PREVIOUS2" ]; then
                TREND="U"
        else
                TREND="N"
        fi

        if [ "$LINE" -ge "$PREVIOUS" ]; then
                if [ "$PREVIOUS_TREND" = "D" ]; then
                        TREND="E"
                fi
        fi

        if [ "$LINE" -le "$PREVIOUS" ]; then
                if [ "$PREVIOUS_TREND" = "U" ]; then
                        TREND="E"
                fi
        fi

        if [ "$PREVIOUS_TREND" = "E" ]; then
                if [ "$TREND" = "U" ]; then
                        TREND="RU"
                elif [ "$TREND" = "D" ]; then
                        TREND="RD"
                fi
        fi

        PREVIOUS_TREND=$TREND
        PREVIOUS2=$PREVIOUS
        PREVIOUS=$LINE

        printf "$LINE $TREND \n"
done


