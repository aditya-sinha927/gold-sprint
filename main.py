import hashlib
import os
from dataclasses import dataclass
from typing import List
from collections import OrderedDict
import json

@dataclass
class Block:
    blockHash: str
    size: int
    data: bytes

@dataclass
class FileMetaData:
    fileName: str
    blockHashes: list[str]

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        
    def get(self, block_hash: str) -> bytes:
        # Check if the block is in the cache
        if block_hash not in self.cache:
            return None

def chunk_and_hash (name: str) ->list:
    path =  name
    dataFile = open(path , 'rb')
    blockList = []

    while True:
        chunk = dataFile.read(4 * 1024 * 1024)
        if not chunk:#read returns empty byte string when end of file
            return blockList

        block_hash = hashlib.sha256(chunk).hexdigest()
        datablock = Block(block_hash,len(chunk),chunk)
        
        blockList.append(datablock)

def make_wal_Entry(blockList: List) -> None:
    path = "wal/engine.log"
    logFile = open(path, 'a')
    for i in blockList:
        logData = {"operation":"Write","size":i.size,"hashValue":i.blockHash}
        log_string = json.dumps(logData)
        logFile.write(log_string + "\n")
        logFile.flush()
        os.fsync(logFile.fileno())

def write_data (blockList: list) ->None :
    path = "data/"
    for i in blockList:
        fileName = path + i.blockHash
        if os.path.exists(fileName):
            continue
        file = open(fileName,"wb")
        file.write(i.data)
        