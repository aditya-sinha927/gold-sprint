Distributed Block Storage Engine
A lightweight, highly available distributed block storage prototype built entirely in Python.

Overview :
Traditional monolithic file systems fail at petabyte scale. 
This project implements a distributed approach by separating the Control Plane (metadata management) from the Data Plane (raw byte storage).
Large files are stripped into uniform 4MB chunks, cryptographically hashed for system-wide deduplication, and replicated across isolated storage nodes using a Quorum-based consensus model.

Core Features & Technical Implementation : 
Zero-Copy File Chunking --> Memory-safe ingestion pipeline that streams massive files in 4MB segments without exhausting system RAM.

Crash Recovery --> If a storage node loses power, an automated boot-sequence reconstructs the entire in-memory state (LRU Cache and Hash Maps) by sequentially replaying the Write-Ahead Log.

Data Deduplication --> Cryptographic hashing prevents identical 4MB sequences from ever being written to disk twice.

Automated Failover (Planned) --> Background leader-election protocol to promote a Follower to Primary if the network partition isolates a node.

Tech Stack :
Language --> Python 3.10+

Libraries: hashlib, os, json, dataclasses, collections.OrderedDict

Infrastructure (Phase 3): Docker, local Kubernetes (planed Minikube) for network partition simulations.

Refer to file quickstart.txt to see how you can use this project for yourself
Refer to file HighLevelDesign to see the HLD.
