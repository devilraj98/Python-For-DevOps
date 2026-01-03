# Day 01: Python Basics for DevOps

## Overview
This day covers fundamental Python concepts essential for DevOps automation, including variables, data types, conditional statements, and basic operations.

## Topics Covered

### 1. Python Basics
- First Python program
- Comments (single-line and multi-line)
- Code structure and syntax

### 2. Variables and Data Types
- Variable declaration and assignment
- Data types:
  - **String** (`str`) - Text data
  - **Integer** (`int`) - Whole numbers
  - **Float** (`float`) - Decimal numbers
  - **Boolean** (`bool`) - True/False values

### 3. Variable Naming Rules
- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot use reserved keywords
- No spaces or special characters
- Should be descriptive and meaningful

### 4. Basic Operations
- **Arithmetic Operations:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Modulus (`%`)
  - Exponentiation (`**`)
  - Floor Division (`//`)

### 5. User Input and Output
- `input()` function for user input
- `print()` function for output
- `type()` function to check data types

### 6. Conditional Statements
- **If statement** - Single condition
- **If-Else statement** - Two conditions
- **If-Elif-Else statement** - Multiple conditions
- **Nested If statements** - Conditions within conditions

### 7. Logical Operators
- `and` - Both conditions must be true
- `or` - At least one condition must be true
- `not` - Negates the condition

## DevOps Use Cases Demonstrated

### Server Monitoring Example
```python
cpu_usage = 85

if cpu_usage > 80:
   print("Scale up the servers")
else:
   print("Server is stable as of now")
```

### Memory Usage Classification
```python
memory_usage = 70   
if memory_usage > 80:
    print("High memory usage")
elif memory_usage > 50:
    print("Moderate memory usage")
else:
    print("Low memory usage")
```

### Disk Space Monitoring
```python
disk_space = 90 
if disk_space > 80:
    print("Disk space is high.")
    if disk_space > 90:
        print("Warning: Disk space is critically low!")
    else:
        print("Disk space is moderate.")
```

### Infrastructure Status Check
```python
is_server_up = True 
is_database_connected = False
if is_server_up and is_database_connected:
    print("Server and database are operational.")
elif is_server_up or is_database_connected:
    print("Either server or database is operational.")  
else:
    print("Both server and database are down.")
```

## Practical Exercises

### Exercise 1: Environment Deployment Check
Write a script that:
- Takes environment name as input
- Prints "Production deployment" if env is "prod"
- Otherwise prints "Non-production deployment"

### Exercise 2: CPU Usage Monitor
Write a script that:
- Takes CPU usage as input
- Prints "High CPU usage" if usage > 75%
- Prints "Moderate CPU usage" if usage is between 50% and 75%
- Prints "Low CPU usage" if usage < 50%

## Key Learning Outcomes
- Understanding Python syntax and structure
- Working with different data types
- Implementing conditional logic for automation
- Creating basic monitoring and alerting scripts
- Foundation for DevOps automation tasks

## Files
- `hello..py` - Main Python file with all examples and exercises

## Next Steps
Day 02 will cover loops and data structures (lists, tuples, dictionaries) which are essential for handling multiple servers, configurations, and automation tasks in DevOps.