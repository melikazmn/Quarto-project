# Quarto Game Using Python and Socket.IO

## Project Overview
This project implements a **Quarto game** using **Socket.IO** and **Python**. It consists of two main parts: a **client** and a **server** that communicate using web sockets. The game is a board game where two players compete, and the project allows for remote multiplayer gameplay.

## Features
- Real-time multiplayer game using Socket.IO.
- Python-based server and client architecture.
- Classic Quarto game rules implemented.
- Efficient and responsive communication between client and server.
  

## Setup and Installation

### Prerequisites
- Python 3.x
- Virtualenv (optional)
- Git

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/Quarto-Game-SocketIO.git
    cd Quarto-Game-SocketIO
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install required dependencies for both client and server:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

1. Navigate to the `server` directory:
    ```bash
    cd server
    ```

2. Start the server:
    ```bash
    python server.py
    ```

### Running the Client

1. Navigate to the `client` directory:
    ```bash
    cd client
    ```

2. Start the client:
    ```bash
    python client.py
    ```

## How to Play
1. Start the server using the steps mentioned above.
2. Run the client and connect to the server.
3. The game will follow the rules of **Quarto**, where two players take turns.

## Project Structure
- `client/`: Contains all client-side code.
- `server/`: Contains all server-side code.

## Contributing
Feel free to contribute by forking the repository, making improvements, and submitting a pull request.
