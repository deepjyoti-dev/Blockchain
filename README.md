# Blockchain
Python Blockchain with Flask API

A simple Proof-of-Work blockchain implementation in Python with a REST API using Flask. This project allows you to mine blocks and view the full blockchain.

Features

Basic blockchain implementation in Python

Proof-of-Work mining with adjustable difficulty

Flask API to interact with the blockchain

JSON-based endpoints:

POST /mine → Add a new block

GET /chain → Retrieve the full blockchain

Each block contains:

index – Position of the block in the chain

timestamp – Time of block creation

data – Any JSON data

previous_hash – Hash of the previous block

nonce – Number used for mining

hash – SHA-256 hash of the block

Prerequisites

Python 3.8+

Flask library

Install Flask:

pip install flask

Usage

Clone the repository:

git clone https://github.com/<your-username>/python-blockchain.git
cd python-blockchain


Run the Flask server:

python blockchain_full.py


The server runs on http://127.0.0.1:5000.

Mine a new block:

curl -X POST http://127.0.0.1:5000/mine -H "Content-Type: application/json" -d '{"sender": "Alice", "receiver": "Bob", "amount": 50}'


Response:

{
  "message": "New block mined",
  "index": 1,
  "hash": "0000abcd1234...",
  "data": {"sender": "Alice", "receiver": "Bob", "amount": 50},
  "previous_hash": "0000xyz789...",
  "nonce": 3521
}


View the full blockchain:

curl http://127.0.0.1:5000/chain


Response:

[
  {
    "index": 0,
    "timestamp": 1697090400.123,
    "data": "Genesis Block",
    "hash": "0000abc...",
    "previous_hash": "0",
    "nonce": 0
  },
  {
    "index": 1,
    "timestamp": 1697090500.456,
    "data": {"sender": "Alice", "receiver": "Bob", "amount": 50},
    "hash": "0000def...",
    "previous_hash": "0000abc...",
    "nonce": 3521
  }
]

Project Structure
blockchain_full.py   # Main Python file
README.md            # Project documentation

Customization

Difficulty: Adjust Blockchain.difficulty in blockchain_full.py for easier or harder mining.

Data: You can store any JSON data in a block.
