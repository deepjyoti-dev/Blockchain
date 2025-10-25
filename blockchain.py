# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 14:00:24 2025

@author: deepj
"""

# blockchain_full.py
import hashlib
import json
from time import time
from flask import Flask, jsonify, request

# -------------------------
# Block and Blockchain Classes
# -------------------------
class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Number of leading zeros required

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), time(), data, last_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        return new_block

# -------------------------
# Flask API
# -------------------------
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    block = blockchain.add_block(data)
    return jsonify({
        "message": "New block mined",
        "index": block.index,
        "hash": block.hash,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "nonce": block.nonce
    }), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "hash": block.hash,
            "previous_hash": block.previous_hash,
            "nonce": block.nonce
        })
    return jsonify(chain_data), 200

# -------------------------
# Run Flask Server
# -------------------------
if __name__ == '__main__':
    app.run(port=5000)
