#!/usr/bin/env python

import sys
sys.path[0:0] = ['/usr/share/anki']

import ankiqt
import anki
from anki.stdmodels import BasicModel
import argparse

parser = argparse.ArgumentParser(description = 'Add card with specified front and back to the deck')
parser.add_argument('deck')
parser.add_argument('-f', '--front', dest='front', help='front of the card', required=True)
parser.add_argument('-b', '--back', dest='back', help='back of the card', required=True)
args = parser.parse_args()

deck = anki.deck.DeckStorage.Deck(args.deck,False,False)
deck.addModel(BasicModel())

# if set True then 2 cards will be created: Front->Back and Back->Front
deck.currentModel.cardModels[1].active = False

fact = deck.newFact()
fact['Front'] = unicode(args.front,'utf-8')
fact['Back'] = unicode(args.back,'utf-8')
fact.tags = u'selection'

# chech whether the card is already in the deck
factIds, cardIds = deck.findCardsMatchingFilters(
	[{'scope': 'fact','field': 'front','value': fact['Front'],'is_neg': False}])
if factIds:
	sys.exit(0)

deck.addFact(fact)
deck.save()
