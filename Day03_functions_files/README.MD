# 🐍 Day 3: Functions, File Handling & Exception Management

**DevOps Focus:** Building reusable automation scripts with proper error handling

---

## 📋 Learning Objectives

By the end of Day 3, you will:
- ✅ Write reusable functions for DevOps automation
- ✅ Handle files (read/write/append) for configuration and logs
- ✅ Implement proper exception handling in scripts
- ✅ Combine functions + file handling + error management
- ✅ Build production-ready DevOps automation patterns

---

## 🎯 Topics Covered

### 1. Functions in Python
- Basic function definition and calling
- Functions with parameters
- Nested functions
- Functions with return values
- Real DevOps patterns with functions

### 2. File Handling
- Opening and closing files
- Reading files (entire content, partial, line by line)
- Writing and appending to files
- Using `with` statement for automatic file management

### 3. Exception Handling
- `try`, `except`, `finally` blocks
- Handling specific exceptions (FileNotFoundError)
- Generic exception handling
- Exception handling in file operations

---

## 🔧 Code Examples

### Functions for DevOps Automation

```python
# Basic deployment function
def deploy():
    print("Deploying application...")

# Function with parameters
def deploy_app(app_name):
    print("Deploying application:", app_name)

# CPU monitoring function
def is_cpu_alert(server, cpu):
    if cpu >= 75:
        print(server, "CPU is Overloaded")
    elif cpu > 50 and cpu < 75:
        print(server, "CPU is normal")
    else:
        print(server, "CPU is safe")

# Function with return value
def get_cpu_status(cpu):
    if cpu >= 75:
        return "Overloaded"
    elif cpu > 50 and cpu < 75:
        return "Normal"
    else:
        return "Safe"
```

### File Operations for DevOps

```python
# Reading server list from file
with open("servers.txt", 'r') as file:
    for line in file:
        print(line.strip())

# Writing server reports
with open("output.txt", 'w') as file:
    file.write("Server Report\n")
    file.write("==============\n")
    file.write("web-01: CPU Usage - 75%\n")

# Appending new data
with open("output.txt", 'a') as file:
    file.write("cache-01: CPU Usage - 55%\n")
```

### Exception Handling in DevOps Scripts

```python
try:
    file = open("servers.txt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Unexpected Error:", e)
finally:
    file.close()
```

### Complete DevOps Pattern

```python
def check_disk(server, usage):
    try:
        if usage > 75:
            print("ALERT:", server, "Disk usage high")
        elif usage > 50 and usage <= 75:
            print(server, "Disk usage normal")
        else:
            print("Disk is Normal")
    except Exception as e:
        print("Unexpected error:", e)

servers = [
    {"name": "web-01", "disk": 80},
    {"name": "db-01", "disk": 45},
    {"name": "cache-01", "disk": 60}
]

for server in servers:
    check_disk(server['name'], server['disk'])
```

---

## 📁 Files in This Directory

- **`day03.py`** - Functions examples and DevOps patterns
- **`filehandling.py`** - Complete file operations and exception handling
- **`servers.txt`** - Sample server list for reading operations
- **`output.txt`** - Generated report file from write operations
- **`README.MD`** - This documentation

---

## 🚀 DevOps Use Cases Practiced

1. **Server Monitoring Functions**
   - CPU usage alerts
   - Disk space monitoring
   - Reusable monitoring logic

2. **Configuration File Management**
   - Reading server inventories
   - Writing deployment reports
   - Appending log entries

3. **Error-Resilient Scripts**
   - Handling missing files
   - Graceful error recovery
   - Proper resource cleanup

---

## 💡 DevOps Best Practices Learned

- ✅ **Always use functions** - Make code reusable and modular
- ✅ **Never trust input** - Always handle potential errors
- ✅ **Read data from files** - Don't hardcode server lists or configs
- ✅ **One function = one responsibility** - Keep functions focused
- ✅ **Use `with` statement** - Automatic file handling and cleanup
- ✅ **Handle exceptions gracefully** - Scripts should never crash unexpectedly

---

## 🎯 Practice Exercises

### Exercise 1: Server Health Check Function
Write a function that takes server name and multiple metrics (CPU, memory, disk) and returns overall health status.

### Exercise 2: Log File Parser
Create a function that reads a log file and counts error occurrences.

### Exercise 3: Configuration Backup
Write a script that reads config files and creates timestamped backups.

---

## 🔍 Interview Questions (1-2 Years Level)

1. **Q:** What's the difference between `read()`, `readline()`, and `readlines()`?
   **A:** `read()` reads entire file, `readline()` reads one line, `readlines()` reads all lines into a list.

2. **Q:** Why use `with` statement for file handling?
   **A:** Automatically handles file closing even if exceptions occur, ensures proper resource management.

3. **Q:** How do you handle multiple exception types?
   **A:** Use multiple `except` blocks or catch general `Exception` as fallback.

4. **Q:** What happens if you don't close a file?
   **A:** Resource leak, file may remain locked, potential data loss.

5. **Q:** How to append to a file without overwriting?
   **A:** Use `'a'` mode instead of `'w'` mode when opening the file.

---

## ➡️ Next Steps

**Day 4 Preview:** OS Automation (os, subprocess)
- Running system commands from Python
- Process management
- Environment variables
- System monitoring automation

---

## 🏃‍♂️ Quick Start

```bash
# Run the examples
python day03.py
python filehandling.py

# Check generated files
type output.txt
type servers.txt
```

**Ready to automate with functions and files! 🚀**