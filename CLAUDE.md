# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python Learning Project** - a structured curriculum designed for developers transitioning from PHP/Laravel to Python. The project is organized by learning days/topics with hands-on examples and exercises.

**Target Learner:** PHP/Laravel developers learning Python
**Focus:** Core Python fundamentals with real-world WindshieldHub business examples

## Project Structure

```
my-ai-learning/
├── day1_basics/
│   └── PythonBasics.py              # Variables, strings, lists, dicts, tuples
├── day2_functions/                   # Functions, loops, comprehensions (planned)
├── day3_oop/                         # Classes, inheritance, OOP concepts (planned)
├── requirements.txt                  # Python dependencies (currently minimal)
├── README.md                         # User-facing setup & learning guide
├── CLAUDE.md                         # This file
└── venv/                             # Python virtual environment
```

## Running the Code

### Prerequisites
- Python 3.9+ (already in venv)
- Virtual environment already created at `./venv`

### Commands

**Activate virtual environment:**
```bash
source venv/bin/activate
```

**Run a Python file:**
```bash
python day1_basics/PythonBasics.py
python day2_functions/functions_loops.py  # When created
```

**Install dependencies (if added to requirements.txt):**
```bash
pip install -r requirements.txt
```

**Deactivate when done:**
```bash
deactivate
```

## Code Architecture & Patterns

### Learning File Structure
Each Python learning file follows this pattern:

1. **Comment header** - Indicates which day/topic and what's covered
2. **Conceptual mapping** - PHP/Laravel → Python comparisons (because the user knows PHP)
3. **Concept sections** - Each major concept in numbered sections with:
   - Explanation comments
   - Code examples
   - Output/results with `print()` statements
4. **Practice exercises** - TODO sections where user implements their own code
5. **Quick reference** - Summary table at end comparing PHP vs Python

**Example:** `day1_basics/PythonBasics.py` (lines 1-191)

### Business Context
Examples use **WindshieldHub** (user's windshield business):
- Order records (customer, service type, amount, status, location)
- Location data (Lahore, Karachi, Islamabad cities)
- Pakistani Rupees (Rs.) as currency
- Windshield replacement context

When adding new content, use similar real-world examples tied to this business domain.

## Development Guidelines

### When Adding New Learning Files
1. Create file in appropriate day folder: `dayN_topic/file.py`
2. Follow the structure pattern described above
3. Use PHP/Laravel comparisons as teaching tools
4. Include practice exercises with TODO comments
5. Add real WindshieldHub business examples
6. Keep code self-contained (no imports/dependencies initially)

### When Modifying Existing Files
- Preserve the conceptual mapping structure
- Keep comparisons to PHP/Laravel
- Maintain clear section comments
- Don't remove practice exercises - enhance them
- Test code by running it to ensure it executes

### Dependencies Philosophy
- **Day 1-3:** No external dependencies (pure Python)
- **Day 4+:** Introduce standard library modules (os, json, sqlite3, etc.)
- **Day 5+:** External packages (requests, flask, pandas, etc.) - add to requirements.txt

## Key Learning Concepts Covered

**Day 1-2 (PythonBasics.py):**
- Variables & types (int, str, float, bool)
- String manipulation (concatenation, methods, f-strings)
- Lists (indexing, methods like append, len)
- Dictionaries (key-value pairs, accessing, adding keys)
- Tuples (immutable sequences)
- Loops (for loops, iteration)
- Conditionals (if statements, membership checks with `in`)

**Planned coverage:**
- Day 2: Functions, default parameters, return values, loops with range(), list comprehensions
- Day 3: Classes, objects, methods, inheritance, encapsulation
- Day 4: File I/O, JSON, CSV, working with data
- Day 5: API concepts, basic Flask web framework

## Notes for Future Claude Instances

1. **User background:** PHP/Laravel developer - use this for comparisons and context
2. **Business context:** Always use WindshieldHub examples when possible
3. **Learning style:** Hands-on with code examples and practice exercises
4. **Quality focus:** Code must be executable - test all examples
5. **Progression:** Keep curriculum sequential (don't skip fundamentals)
6. **Documentation:** Every concept needs PHP→Python comparison

## Tips for Helping the User

- Encourage running the code and experimenting
- Suggest modifications to existing examples
- Help debug practice exercises they're working on
- Explain errors in terms of PHP/Laravel equivalents
- Connect new concepts back to real WindshieldHub business problems
- Guide them to understand "why" Python works differently, not just "how"
