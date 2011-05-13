Tag Radio
=========

Tag Radio is an itty-bitty Last.fm radio tuner that uses RFID tags to start stations in the client.

Installation
------------

Requires PCSCD, Pyscard. Possibly other things.

Usage
-----

* Add tags to cards.dat, serial number first, then the lastfm:// station url.
* Run `./tagradio.py -r0`
* Touch a tag to the reader, and the last.fm client will start playing the associated station.

Getting card serial numbers
---------------------------

Touch an unknown card to the reader while tagradio is running, and it'll output the unknown serial number.
