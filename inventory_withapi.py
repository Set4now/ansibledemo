#!/usr/bin/env python
import os
import sys
import argparse
import json

import urllib
url="http://localhost:80"
data=urllib.urlopen(url)
#print data.read()

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
           #self.inventory = self.fetch_inventory()
           #self.fetch_inventory()
           self.inventory = self.api_data()
       elif self.args.host:
           temp_inventory = self.fetch_inventory()
           self.inventory = temp_inventory["_meta"]["hostvars"][self.args.host]
           #self.inventory = self.empty_inventory()
           #self.empty_inventory()
       else:
          usage()
          sys.exit()
       #return json.dumps(self.inventory)
       #print self.inventory

    def show_inventory(self):
       print json.dumps(self.inventory, indent=4)

    def empty_inventory(self):
       return {}
     
     
    def api_data(self):
       return data.read()
     
    
    def fetch_inventory(self):
        return {
                     "centos": {
                            "hosts": ["dockermaster"],
                            "vars": {
                                     "ansible_ssh_port": "22"
                             }
                      },
                      "_meta": {
                               "hostvars": {
                                        "dockermaster": {
                                                "ansible_become" : "yes",
                                                "ansible_become_method" : "sudo"
                                                },
                                        "ubuntu-node": {
                                                "ansible_user": "root"
                                                },
                                        "Sumans-MacBook-Air.local": {
                                                "ansible_connection" : "local",
                                                "ansible_become" : "yes",
                                                "ansible_become_method" : "sudo"
                                                }
                                           }
                                },

                     "all": {
                         "children" : ["ungrouped"]
                            },
                    "ungrouped": {
                             "hosts": ["Sumans-MacBook-Air.local"]
                                 }
               }

    def read_arg(self):
        parser=argparse.ArgumentParser(description="Checking arguments")
        parser.add_argument('--list', action = 'store_true', help= "This will fetch the entire inventory")
        parser.add_argument('--host', action = 'store_true', help= "This wil fetch host variables if any")
        self.args = parser.parse_args()

DI=DynamicInventory()
DI.show_inventory()
