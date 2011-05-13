#!/usr/bin/python
import sys,os,time,re,webbrowser

cardFile = 'cards.dat'

# We're binding against the local copy for stability
sys.path.append('RFIDIOt-0.1x')
import RFIDIOtconfig
card = RFIDIOtconfig.card

currentCard = ''
lastCard = ''
cards = {};

regex = re.compile('^(.*?)\s+(.*?)$')

file = open(cardFile)
for line in file:
    if regex.match(line):
        matches = regex.findall(line)
        cards[matches[0][0]] = matches[0][1]

while (True):

    if card.select():

        if currentCard != card.uid and card.uid != lastCard:
            currentCard = card.uid

            if currentCard in cards:
                station = cards[currentCard]
                print "Tuning %s" % station

                webbrowser.open(station)
                lastCard = currentCard

            else:
                print "Unknown card: %s" % card.uid

    else:
        currentCard = ''

    time.sleep(0.2)
