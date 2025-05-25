# FastAPI Project

This is a starter project using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Features

- FastAPI for building APIs
- Automatic interactive API docs (Swagger UI & ReDoc)
- Easy integration with databases and authentication
- Async support

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-fastapi-project.git
   cd your-fastapi-project
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```

## Running the Application

Start the FastAPI server with Uvicorn:

```sh
uvicorn main:app --reload
```

- Open your browser at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs.

## Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
└── ...
```

## License

This project is licensed under the MIT License.