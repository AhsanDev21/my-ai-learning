# Python Learning Journey

A structured Python learning project designed for developers transitioning from PHP/Laravel to Python.

## Project Structure

```
my-ai-learning/
├── day1_basics/
│   └── PythonBasics.py          # Variables, strings, lists, dictionaries, tuples
├── day2_functions/              # (coming soon)
├── day3_oop/                    # (coming soon)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── venv/                        # Virtual environment (auto-generated)
```

## Setup Instructions

### 1. Activate Virtual Environment
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Python Files

```bash
# Run Day 1 Basics
python day1_basics/PythonBasics.py

# Or from day1_basics folder:
cd day1_basics
python PythonBasics.py
cd ..
```

### 4. Deactivate Virtual Environment (when done)
```bash
deactivate
```

## Learning Path

### Week 1: Python Fundamentals
- **Day 1-2:** Python Basics (Variables, Strings, Lists, Dictionaries) ✅
  - `day1_basics/PythonBasics.py`

- **Day 3:** Functions & Loops (coming soon)

- **Day 4:** File Handling & CSV ✅
  - `day4_file_handling/file_handling.py` - Read/write CSV files, process data

- **Day 5:** Connect Python to MySQL ✅
  - `day5_mysql/mysql_basics.py` - Database connections, queries

- **Day 6:** Jupyter Notebooks ✅
  - `day6_jupyter/python_basics.ipynb` - Interactive analysis

- **Day 7:** Mini Project - Order Analysis ✅
  - `day7_mini_project/order_analysis.py` - Complete end-to-end project

### Week 2: Data Science (Pandas - MOST IMPORTANT!)
- **Day 8:** Pandas Basics ✅
  - `day8_pandas/pandas_basics.py` - DataFrames, loading data, statistics

- **Day 9:** Filtering & Selecting ✅
  - `day9_filtering/pandas_filtering.py` - Conditional selection (SQL WHERE)

- **Day 10:** GroupBy & Aggregations ✅
  - `day10_grouping/pandas_grouping.py` - Grouping, aggregations (SQL GROUP BY)

- **Day 11:** Data Cleaning ✅
  - `day11_cleaning/data_cleaning.py` - Handle missing data, duplicates, outliers

- **Day 12:** Data Visualization ✅
  - `day12_visualization/data_visualization.py` - Create charts with matplotlib

## Quick Reference: PHP → Python

| PHP | Python |
|-----|--------|
| `$var` | `var` (no $) |
| `echo` | `print()` |
| `array()` | `[]` |
| `["key" => "value"]` | `{"key": "value"}` |
| `foreach()` | `for ... in` |
| `count()` | `len()` |
| `array_push()` | `.append()` |
| `isset()` | `in` |
| `true/false` | `True/False` |
| `null` | `None` |
| `.` concat | `+` concat |

## Tips for Learning

1. **Run the code regularly** - Don't just read, execute and experiment
2. **Modify examples** - Change values and see what happens
3. **Use the terminal** - Get comfortable with command line Python
4. **Take notes** - Comment what you learn in the code
5. **Practice exercises** - Complete the TODO exercises in each file

## Next Steps

1. Run `day1_basics/PythonBasics.py` to see it in action
2. Modify the practice exercises
3. Create your own examples based on your WindshieldHub business
4. Wait for Day 2 - Functions & Loops

Happy Learning! 🐍
# my-ai-learning
