# Fun with Python Threads

David Cutting - https://davecutting.uk - d.cutting@qub.ac.uk

## Overview

Here are some sample files, examples and challenges for using python threads.

## examples Folder

Contains some (in order) examples of simple threading in python including spawing of multiple threads and daemon threads.

## number-guess Folder

Contains a simple number guessing game (guess.py) and then with a threaded countdown timer (guess-timer.py).

## chatter Folder

Contains a network chat program - you can send messages over the network (or to and from yourself).

To start this: ```python chat.py local_port remote_ip remote_port``` where ```local_port``` is the port on your machine to receive incoming messages, ```remote_ip``` is the remote IP address of the machine you want to chat to and ```remote_port``` is the port on which they are listening.

You can test this on a single machine using the IP address ```127.0.0.1``` (which means the local computer).

For example in two terminals you can run:

In terminal 1: ```python chat.py 8001 127.0.0.1 8002``` and in terminal 2: ```python chat.py 8002 127.0.0.1 8001``` - you can now send messages between terminals. You can run this on multiple computers using their network IP addresses to send messages.
