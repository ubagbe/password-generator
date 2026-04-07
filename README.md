# Development Guide: Password Generator (OOP + Git Workflow)

## 1. Objective (Detailed)

This project aims to help the developer learn real-world software development practices by building a CLI-based Password Generator system using Python.

### Key Learning Goals:

* Understand Object-Oriented Programming (OOP) principles such as encapsulation and separation of concerns
* Learn how to structure a project into models, services, and utilities
* Practice Git workflows including branching, commits, and feature-based development
* Implement clean and maintainable code

By the end of this project, the developer should be able to design modular systems and work in a feature-driven development environment similar to industry practices.

---

## 2. CLI User Experience (UX Flow)

### Main Menu Screen:

```
----------------------------------
 PASSWORD GENERATOR SYSTEM
----------------------------------
1. Generate Password
2. Check Password Strength
3. Exit
Enter your choice:
```

### Generate Password Flow:

```
Enter password length (8-32):
Include Uppercase? (y/n):
Include Lowercase? (y/n):
Include Numbers? (y/n):
Include Special Characters? (y/n):

Generated Password: Ab#12kLmP
```

### Strength Checker Flow:

```
Enter password:
Strength: Medium
```

### Error Examples:

* Invalid menu choice → `Please enter 1, 2, or 3`
* Invalid length → `Length must be between 8 and 32`
* Invalid input → `Enter y or n only`

---

## 3. Project Structure

```
project/
├── main.py
└── src/
    ├── services/
    │   ├── password_generator.py
    │   ├── strength_checker.py
    ├── utils/
    │   ├── input_handler.py
    │   ├── validator.py
    └── models/
        ├── password_config.py
```

---

## 4. Development Guidelines

* Do NOT write all logic in `main.py`
* Each class must have a single responsibility
* Reuse code via classes instead of duplication
* Follow clean naming conventions

---

## 5. Git Workflow

**Base Branch:** `develop`

Always create a new branch from the base branch and pull the latest changes before starting.

```bash
git checkout develop
git pull
git checkout -b feature/<name>

# implement changes

git add .
git commit -m "feat: description"
git push origin feature/<name>
```

---

## 6. Detailed Tasks

### Task 1: Project Setup

* Create folder structure
* Initialize git repository
* Create empty files

### Task 2: CLI Menu

**File:** `main.py`

* Create `Application` class
* Add `run()` method
* Implement menu loop and user input

### Task 3: InputHandler

**File:** `utils/input_handler.py`

* Create `InputHandler` class

**Methods:**

* `get_menu_choice()`
* `get_password_length()`
* `get_character_preferences()`
* `get_password_input()`

### Task 4: Validator

**File:** `utils/validator.py`

* Create `Validator` class
* Add validation methods
* Integrate validation into `InputHandler`

### Task 5: PasswordConfig

**File:** `models/password_config.py`

* Create `PasswordConfig` class
* Store user selections as attributes

### Task 6: PasswordGenerator

**File:** `services/password_generator.py`

* Create `PasswordGenerator` class

**Method:**

* `generate(config)`

* Implement password generation logic

### Task 7: Generator Integration

* Use `InputHandler` + `PasswordConfig` + `PasswordGenerator` in `main.py`

### Task 8: StrengthChecker

**File:** `services/strength_checker.py`

* Create `StrengthChecker` class

**Method:**

* `evaluate(password)`

### Task 9: Strength Integration

* Integrate strength checker into main flow

### Task 10: Refactor (Optional)

* Clean code
* Remove duplication
* Improve readability
