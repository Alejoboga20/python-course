# Python Course

A personal Python learning repository with notes and runnable examples. The
current content focuses on Python basics and is organized so each topic can be
read independently and executed from the command line.

## Contents

- [01-basics](01-basics/) - introductory Python syntax and core concepts.
- [fastapi-fundamentals](fastapi-fundamentals/) - a small FastAPI app with
  CRUD-style blog post endpoints.

### Python Basics

The basics section currently covers:

- Variables and naming conventions
- Fundamental data types
- Numeric operations and common built-in functions
- String formatting, escaping, indexing, and slicing
- Conditional statements with `if`, `elif`, and `else`
- Logical operators: `and`, `or`, and `not`
- Short-circuit evaluation

Planned topics include loops, functions, decorators, and object-oriented
programming.

## Repository Structure

```text
.
├── README.md
├── 01-basics/
│   ├── README.md
│   ├── conditionals.py
│   ├── data-types.py
│   ├── logic-operators.py
│   └── variables.py
└── fastapi-fundamentals/
    ├── api-testing/
    ├── main.py
    └── requirements.txt
```

## Requirements

- Python 3.10 or newer

The Python basics examples do not require external dependencies. The FastAPI
project has its own dependencies listed in
`fastapi-fundamentals/requirements.txt`.

## Running Examples

From the repository root, run any example with Python:

```bash
python 01-basics/variables.py
python 01-basics/data-types.py
python 01-basics/conditionals.py
python 01-basics/logic-operators.py
```

Depending on your environment, you may need to use `python3` instead of
`python`.

## FastAPI Fundamentals Setup

The FastAPI project lives in `fastapi-fundamentals/`.

From the repository root, create and activate a virtual environment:

```bash
cd fastapi-fundamentals
python -m venv venv
source venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the development server:

```bash
fastapi dev main.py
```

You can also run it directly with Uvicorn:

```bash
uvicorn main:app --reload
```

Once the server is running, open:

- App root: <http://127.0.0.1:8000/>
- Interactive API docs: <http://127.0.0.1:8000/docs>
- Alternative API docs: <http://127.0.0.1:8000/redoc>

Useful endpoints include:

- `GET /`
- `GET /posts`
- `GET /posts/{post_id}`
- `POST /posts`
- `PUT /posts/{post_id}`
- `DELETE /posts/{post_id}`

When you are done working in the virtual environment, deactivate it:

```bash
deactivate
```

## Learning Path

1. Start with [01-basics/README.md](01-basics/README.md) for the overview.
2. Run `variables.py` to see variable assignment and string interpolation.
3. Run `data-types.py` to explore numbers, strings, type conversion, and
   slicing.
4. Run `conditionals.py` and `logic-operators.py` to practice control flow.
5. Set up `fastapi-fundamentals/` and run the API locally.
6. Modify the examples and rerun them to observe how Python behaves.

## Notes

This repository is a work in progress. New sections will be added as the course
expands beyond the basics.
