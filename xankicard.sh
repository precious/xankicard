#!/bin/bash

PYTHON="`which python`"
SCRIPTS_DIR="/home/precious/programming/python/xankicard"
DECK="/home/precious/.anki/decks/test_deck.anki"

selection="`xsel`"
translation="`$PYTHON $SCRIPTS_DIR/translate.py \"$selection\" --html`"
$PYTHON $SCRIPTS_DIR/addcard.py -f "$selection" -b "$translation" $DECK
