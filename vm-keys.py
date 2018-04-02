#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call,check_output,PIPE
from os import getcwd
from sys import exit

# Check if ssh-agent is installed
binary = call(["which", "ssh-agent"], stdout=PIPE,stderr=PIPE)
if binary == 1:
    print("SSH Agent not installed, please install the ssh-agent package")
    exit(1)

def add_keys():
    """Function loops through vagrant box names and adds
    the keys from the private key paths stored by vagrant"""
    for vm in check_output("vagrant status | grep running | awk '{ print $1 }'", shell=True).splitlines():
        KEY_FILE=getcwd()+'/.vagrant/machines/%s/virtualbox/private_key' % vm.decode('utf-8')
        check_output("ssh-add {}".format(KEY_FILE), shell=True) 

# Check to see if ssh-agent is running, and if not start it.
agent = call(["pgrep", "ssh-agent"], stdout=PIPE,stderr=PIPE)
if agent == 0:
    print("SSH Agent is running")
    add_keys()
else:
    if agent == 1:
        print("Starting SSH Agent")
        check_output("ssh-agent", shell=True)
        add_keys()
