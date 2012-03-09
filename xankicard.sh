#!/bin/bash

PYTHON="`which python`"
SCRIPTS_DIR="/home/precious/programming/python/xankicard"
DECK="/home/precious/.anki/decks/test_deck.anki"

selection="`xsel | sed -r 's/(^\s+)|(\s+$)//g'`"
translation="`$PYTHON $SCRIPTS_DIR/translate.py \"$selection\" --html`"
if [ ! $? == 0 ] ; then
	notify-send -u critical "xankicard: an error occured"
	exit 1
fi
$PYTHON $SCRIPTS_DIR/addcard.py -f "$selection" -b "$translation" $DECK
