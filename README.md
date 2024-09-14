# Todo App

A simple Todo application built using **Flask** with a RESTful API to manage tasks. This project is configured with **GitHub Actions** for Continuous Integration (CI), which automatically runs tests and checks for code quality using **pytest** and **flake8**.

## Features

- **Add a Todo:** Allows users to add a new todo item.
- **Get Todos:** Fetches the list of todo items.
- **API Routes:** Simple API built with Flask.

## Project Structure

```
.
├── app/
│   └── app.py          # Main Flask app with API routes
├── tests/
│   └── test_app.py     # Unit tests for the API
├── venv/               # Virtual environment (ignored in .gitignore)
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI workflow configuration
├── .gitignore          # Specifies files and folders to ignore in git
├── requirements.txt    # Project dependencies
└── README.md           # Project README
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Running the App

To run the Flask app locally:

```bash
python app/app.py
```

The API will be accessible at `http://localhost:5000`.

## API Endpoints

- **GET /todos:** Fetches the list of todos.
- **POST /todos:** Adds a new todo. Expects a JSON body with a `todo` field.

Example `POST` request:

```bash
curl -X POST http://localhost:5000/todos -H "Content-Type: application/json" -d '{"todo": "Buy groceries"}'
```

## Running Tests

To run the unit tests with `pytest`:

```bash
pytest
```

## Linting Code

This project uses `flake8` to maintain code quality. To run the linter:

```bash
flake8 app/ tests/
```

## Continuous Integration (CI)

This project uses **GitHub Actions** to automatically run tests and linting on every push and pull request. The CI configuration can be found in `.github/workflows/ci.yml`. The following actions are run:

- **Test suite** using `pytest`.
- **Linting** using `flake8`.

Merging into `main` is blocked unless all CI checks pass.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
