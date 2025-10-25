⛓️ Python Blockchain with Flask API

A simple Proof-of-Work blockchain implementation in Python with a REST API using Flask.
Mine blocks, store JSON data, and interact with the blockchain through HTTP endpoints.

🚀 Features

Basic blockchain implementation in Python

Proof-of-Work mining with adjustable difficulty

Flask API for blockchain interaction

JSON-based endpoints:

POST /mine → Add a new block

GET /chain → Retrieve the full blockchain

Block Structure

Each block contains:

Field	Description
index	Position in the chain
timestamp	Time of block creation
data	Any JSON data (e.g., transactions)
previous_hash	Hash of the previous block
nonce	Number used for mining
hash	SHA-256 hash of the block
🛠️ Prerequisites

Python 3.8+

Flask library

Install Flask:

pip install flask

⚙️ Usage

Clone the repository:

git clone https://github.com/<your-username>/python-blockchain.git
cd python-blockchain


Run the Flask server:

python blockchain_full.py


Server runs at: http://127.0.0.1:5000

🏗️ Mine a New Block
curl -X POST http://127.0.0.1:5000/mine \
-H "Content-Type: application/json" \
-d '{"sender": "Alice", "receiver": "Bob", "amount": 50}'


Example Response:

{
  "message": "New block mined",
  "index": 1,
  "hash": "0000abcd1234...",
  "data": {"sender": "Alice", "receiver": "Bob", "amount": 50},
  "previous_hash": "0000xyz789...",
  "nonce": 3521
}

📜 View Full Blockchain
curl http://127.0.0.1:5000/chain


Example Response:

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

🔧 Project Structure
blockchain_full.py   # Main Python file
README.md            # Documentation

⚙️ Customization

Difficulty: Adjust Blockchain. difficulty in blockchain_full.py for easier or harder mining

Data: Store any JSON data in a block (e.g., transactions, messages, files metadata)

🏷️ Tags

#python #flask #blockchain #restapi #proof-of-work #cryptography #backend

🧑‍💻 Author

Deepjyoti Das
🔗 https://www.linkedin.com/in/deepjyotidas1

💻 GitHub
