#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Ice
Ice.loadSlice("Icegauntlet.ice")
import IceGauntlet
import os, hashlib, sys
import getpass
from pwn import *
import time,json

class Client(Ice.Application):

    def run(self,argv):
        proxy = self.communicator().stringToProxy(argv[1])
        roomservice = IceGauntlet.RoomServicePrx.checkedCast(proxy)
        if not authentication:
            raise RuntimeError('Invalid proxy')

        token = argv[2]
        roomName = argv[3]
        p = log.progress("Trying to Push the Room...")
        time.sleep(1)
        try:
            roomservice.remove(token,roomName)
            p.status("Room sending...")
            time.sleep(1)
            p.success("Done")
        except IceGauntlet.Unauthorized:
            p.failure("Token valid")
        except IceGauntlet.RoomNotExists:
            p.failure("The room not exists")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("usage: ./ClientRemove <proxy> <token> <roomname>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))