'''
Copyright (c) 2021, Saurabh Pujari
All rights reserved.

This source code is licensed under the BSD-style license found in the LICENSE file in the root directory of this source tree.
'''
from .elara import Elara
from cryptography.fernet import Fernet
from .elarautil import Util

def exe(path, commitdb=False):
    return Elara(path, commitdb)

def exe_secure(path, commitdb=False, key_path='edb.key'):
    Util.loadkey(key_path)
    return Elara(path, commitdb, key_path)