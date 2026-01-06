# 🐧 Day 4: Linux OS Automation with Python

**DevOps Focus:** Automating Linux system operations and command execution

---

## 📋 Learning Objectives

By the end of Day 4, you will:
- ✅ Execute Linux commands from Python using `subprocess`
- ✅ Handle command output, errors, and return codes
- ✅ Build system monitoring automation scripts
- ✅ Implement service status checking
- ✅ Create disk usage monitoring with alerts
- ✅ Combine OS automation with file handling

---

## 🎯 Topics Covered

### 1. OS Module Basics
- Getting current working directory
- Environment variables
- File system operations

### 2. Subprocess Module
- Running Linux commands with `subprocess.run()`
- Capturing command output
- Handling command failures
- Error management with try-catch

### 3. Real DevOps Automation
- Disk usage monitoring
- Service status checking
- Log file operations
- System health checks

---

## 🔧 Code Examples

### Basic OS Operations

```python
import os
import subprocess

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Basic command execution
print(subprocess.run(["ls", "-l"]))
```

### Capturing Command Output

```python
def check_disk():
    result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

check_disk()
```

### Error Handling in Commands

```python
def safe_list_logs(path):
    try:
        result = subprocess.run(
            ["ls", "-l", path],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")

safe_list_logs("/invalid/path")
```

### Service Status Monitoring

```python
def check_service_status(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e.stderr}"

status = check_service_status("ssh")
print(f"SSH Service Status: {status}")
```

### Advanced Disk Usage Alert System

```python
def disk_check():
    result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.splitlines()
    
    for line in lines[1:]:   # skip header
        parts = line.split()
        filesystem = parts[0]
        usage = int(parts[4].replace("%", ""))
        
        if usage >= 80:
            print(f"ALERT: {filesystem} usage is {usage}%")
        else:
            print(f"OK: {filesystem} usage is {usage}%")

disk_check()
```

---

## 📁 Files in This Directory

- **`day04.py`** - Complete OS automation examples and DevOps patterns
- **`README.md`** - This documentation

---

## 🚀 DevOps Use Cases Practiced

1. **System Monitoring**
   - Disk usage alerts
   - Service health checks
   - System resource monitoring

2. **Command Automation**
   - Safe command execution
   - Output parsing and processing
   - Error handling and recovery

3. **Infrastructure Management**
   - Server status checking
   - Log file operations
   - System administration tasks

---

## 💡 DevOps Best Practices Learned

- ✅ **Use `subprocess.run()`** - Never use `os.system()` in production
- ✅ **Always capture output** - Use `capture_output=True, text=True`
- ✅ **Handle errors gracefully** - Use try-except with `subprocess.CalledProcessError`
- ✅ **Parse command output** - Process results for meaningful alerts
- ✅ **Combine with file operations** - Read server lists, write reports
- ✅ **Set proper return codes** - Use `check=True` for error detection

---

## 🎯 Practice Exercises

### Exercise 1: System Uptime Monitor
Write a function that runs `uptime` command and prints formatted output.

### Exercise 2: Server Ping Checker
Read server names from a file, ping each server, and handle failures gracefully.

### Exercise 3: Disk Usage Alert (Interview Level)
Create a function that checks disk usage using `df -h` and prints alerts if usage > 80%.

---

## ⚠️ DevOps Interview Insights

**❌ Avoid in Interviews:**
- `os.system()` - Deprecated and insecure
- Ignoring command errors
- Not capturing output

**✅ Always Include:**
- `subprocess.run()` with proper parameters
- Output capture and processing
- Error handling with try-except
- Return code checking

---

## 🔍 Interview Questions (2-3 Years Level)

1. **Q:** Why use `subprocess.run()` instead of `os.system()`?
   **A:** `subprocess.run()` provides better security, output capture, error handling, and return code management.

2. **Q:** How do you capture both stdout and stderr?
   **A:** Use `capture_output=True` or specify `stdout=subprocess.PIPE, stderr=subprocess.PIPE`.

3. **Q:** What does `check=True` parameter do?
   **A:** Raises `CalledProcessError` if command returns non-zero exit code, enabling automatic error detection.

4. **Q:** How to handle command timeouts?
   **A:** Use `timeout` parameter in `subprocess.run()` to prevent hanging commands.

5. **Q:** Best way to parse command output?
   **A:** Use `text=True` for string output, then `splitlines()` and `split()` for structured parsing.

---

## 🔧 Key Subprocess Parameters

```python
subprocess.run(
    ["command", "arg1", "arg2"],
    capture_output=True,    # Capture stdout/stderr
    text=True,             # Return strings not bytes
    check=True,            # Raise exception on failure
    timeout=30             # Prevent hanging
)
```

---

## ➡️ Next Steps

**Day 5 Preview:** Environment Variables & Configuration Management
- Reading environment variables
- Configuration file handling
- Secrets management
- Environment-based deployments

---

## 🏃♂️ Quick Start

```bash
# Run the examples
python day04.py

# Test individual functions
python -c "from day04 import check_disk; check_disk()"
```

**Ready to automate Linux operations! 🐧🚀**