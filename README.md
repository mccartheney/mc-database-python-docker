# mc-database-python-docker 

This project is a simple database management system (DBMS) implemented in Python. It allows users to perform various operations on tables stored in a database directory.

## Table of Contents

1. [Features](#features)
8. [TODO](#todo)
2. [Prerequisites](#prerequisites)
3. [Usage](#usage)
4. [Commands](#commands)
5. [File Structure](#file-structure)
6. [Contributors](#contributors)
7. [License](#license)

## Features <a name="features"></a>

- **Table Operations:** Create, delete, insert data into, and show tables.
- **Data Manipulation:** Select specific columns, remove specific data, and edit existing data in tables.
- **Database Initialization:** Initialize the database directory if it doesn't exist.
- **Docker Support:** Run the application inside a Docker container.


## TODO <a name="todo"></a>

- [ ] Implement error handling to gracefully handle unexpected inputs or errors during operations.
- [ ] Warn the user if a specified table or data does not exist before attempting to perform operations on it.
- [ ] Enhance search functionality to support range searches (e.g., `>`, `<`, `>=`, `<=`, etc.) for more flexible querying.
- [ ] Add support for searching multiple conditions simultaneously to filter data more effectively.
- [ ] Create a `setup.py` file to define package metadata and dependencies.
- [ ] Define package structure and organize project files accordingly.
- [ ] Write tests to ensure the correctness of package functionalities.
- [ ] Package the application using `setuptools`.
- [ ] Upload the package to PyPI for distribution.
- [ ] Update documentation and README with installation and usage instructions for the pip package.

## Prerequisites <a name="prerequisites"></a>

- Docker<br>
#### If want to run locally you need to have : 
- Python 3.x <br>
- `click` library (install via `pip install click`)
- `tabulate` library (install via `pip install tabulate`)

## Usage <a name="usage"></a>

1. **Initialize Database:** Run `python main.py` to initialize the database directory.
2. **Run with Docker:** Build the Docker image and start the container using `make run`.
3. **Commands:** See [Commands](#commands) section for detailed command usage.

## Commands <a name="commands"></a>

The following commands are available for interacting with the database:

- **SHOW TABLES:** Display all tables in the database.
  ```bash
  python main.py SHOW TABLES
  ```

- **DELETE table_name:** Delete the specified table.
  ```bash
  python main.py DELETE users
  ```

- **CREATE table keys:** Create a new table with the specified keys.
  ```bash
  python main.py CREATE users id,name,email
  ```

- **INSERT INTO table keys VALUE values:** Insert values into a table.
  ```bash
  python main.py INSERT INTO users id,name,email VALUES 1,John,Doe
  ```

- **SELECT column FROM table WHERE condition:** Select specific columns from a table based on a condition.
  ```bash
  python main.py SELECT name,email FROM users WHERE id=1
  ```

- **REMOVE FROM table WHERE condition:** Remove specific data from a table based on a condition.
  ```bash
  python main.py REMOVE FROM users WHERE id=1
  ```

- **REMOVE FROM table:** Remove all data from a table.
  ```bash
  python main.py REMOVE FROM users
  ```

- **EDIT table SET key=value WHERE condition:** Edit data in a table based on a condition.
  ```bash
  python main.py EDIT users SET name=John, email=john@example.com WHERE id=1
  ```

- **SHOW table:** Show all data in the specified table.
  ```bash
  python main.py SHOW users
  ```
## File Structure <a name="file-structure"></a>

- **`main.py`:** The main script for executing commands and interacting with the database.
- **`inicialize_database.py`:** Script for initializing the database directory.
- **`create_table.py`:** Script for creating a new table.
- **`delete_table.py`:** Script for deleting a table.
- **`insert_table.py`:** Script for inserting data into a table.
- **`show_tables.py`:** Script for showing all tables in the database.
- **`show_table.py`:** Script for showing all data in a specific table.
- **`select_column.py`:** Script for selecting specific columns from a table.
- **`remove_table_content.py`:** Script for removing all data from a table.
- **`remove_from.py`:** Script for removing specific data from a table.
- **`edit_table.py`:** Script for editing data in a table.
- **`Dockerfile`:** Dockerfile for building the Docker image.
- **`Makefile`:** Makefile for running Docker commands.

## Developers <a name="contributors"></a>

- Mccartheney Mendes [github](https://github.com/mccartheney) [linkedIn](https://www.linkedin.com/in/mccartheney-mendes-892709292/)

## License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

