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
        if not roomservice:
            raise RuntimeError('Invalid proxy')

        token = argv[2]
        roomData = argv[3]
        p = log.progress("Trying to Push the Room...")
        time.sleep(1)
        try:
            roomservice.publish(token,roomData)
            p.status("Room sending...")
            time.sleep(1)
            p.success("Done")
        except IceGauntlet.Unauthorized:
            p.failure("Token not valid")
        except IceGauntlet.RoomAlreadyExists:
            p.failure("The room already exists")
        except IceGauntlet.InvalidRoom:
            p.failure("The room is not valid")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("usage: ./ClientPublish <proxy> <token> <roomdata>")
        sys.exit(1)
    sys.exit(Client().main(sys.argv))