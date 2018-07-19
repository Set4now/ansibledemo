#!/usr/bin/env python
import os
import sys
import argparse
import json

def usage():
 print "Either user --list or --host as a parameter"

#if len(sys.argv) != 2:
#  print usage()
#  sys.exit()


class DynamicInventory(object):


    def __init__(self):

       self.inventory = {}
       self.read_arg()
       
       if self.args.list:
           self.inventory = self.fetch_inventory()
           #self.fetch_inventory()
       elif self.args.host:
           self.inventory = self.empty_inventory()
           #self.empty_inventory()
       else:
          usage()
          sys.exit()
       #return json.dumps(self.inventory)
       #print self.inventory

    def show_inventory(self):
       return self.inventory

    def empty_inventory(self):
       return {}
def fetch_inventory(self):
        return {
                     "centos": {
                            "hosts": ["dockermaster"],
                            "vars": {
                                     "ansible_ssh_port": "22"
                             }
                      }
               }

    def read_arg(self):
        parser=argparse.ArgumentParser(description="Checking arguments")
        parser.add_argument('--list', action = 'store_true', help= "This will fetch the entire inventory")
        parser.add_argument('--host', action = 'store_true', help= "This wil fetch host variables if any")
        self.args = parser.parse_args()

DI=DynamicInventory()
print DI.show_inventory()
