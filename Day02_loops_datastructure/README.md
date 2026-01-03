# Day 02: Loops and Data Structures in Python for DevOps

## Overview
This day focuses on loops and data structures essential for DevOps automation, including iterating over servers, processing configurations, and managing data collections.

## Why Loops in DevOps?
Loops are crucial in DevOps automation for:
- Iterating over multiple servers
- Processing log files
- Managing configurations across environments
- Performing repetitive tasks efficiently
- Batch operations on infrastructure

## Topics Covered

### 1. For Loops
Basic iteration and server management examples.

#### Basic For Loop
```python
for i in range(5):
    print("Iteration:", i)  # Output: Iteration: 0 to 4
```

#### DevOps Server Management
```python
servers = ["server-01", "server-02", "server-03"]
for server in servers:
    print("Server listed is:", server)
```

#### Service Management
```python
services = ["nginx", "mysql", "redis"]
for service in services:
    print("Service is:", service)
```

#### Multi-Environment Deployment
```python
environments = ["dev", "staging", "prod"]
for env in environments:
    print("Deploying to:", env)
```

### 2. While Loops
Conditional iteration for monitoring and waiting scenarios.

```python
count = 1
while count < 10:
    print("No is:", count)
    count += 1  # Output: No is: 1 to 9
```

### 3. Loop Control Statements

#### Break Statement
Stop loop execution when condition is met:
```python
for server in servers:
    if server == "server-02":
        break
    print("Skipping maintenance for:", server)
```

#### Continue Statement
Skip current iteration and continue with next:
```python
for server in servers:
    if server == "server-02":
        continue
    print("Performing maintenance on:", server)
```

## Data Structures

### 1. Lists
**Characteristics:**
- Ordered collection of items
- Mutable (can be modified)
- Can contain duplicates
- Index-based access (starting from 0)
- Can store mixed data types

#### Basic List Operations
```python
servers = ["web-01", "web-02", "db-01"]
print("First server is:", servers[0])  # Output: First server is: web-01
print("Total servers:", len(servers))   # Output: Total servers: 3

# Adding and removing items
servers.append("cache-01")
servers.remove("web-02")
```

### 2. Tuples
**Characteristics:**
- Immutable (cannot be changed after creation)
- Ordered collection
- Defined using parentheses ()

```python
databases = ("mysql", "postgres", "mongodb")
print("First database is:", databases[0])  # Output: First database is: mysql
```

### 3. Dictionaries
**Characteristics:**
- Key-value pairs
- Mutable
- Defined using curly braces {}
- Keys must be unique

#### Server Monitoring with Dictionaries
```python
servers = [
    {"name": "app-01", "state": "Running", "cpu": 45},
    {"name": "app-02", "state": "stopped", "cpu": 0},
    {"name": "app-03", "state": "terminated", "cpu": 80}
]

# Filter running servers
for server in servers:
    if server["state"] == "Running":
        print("Server name is:", server["name"], "Server CPU is:", server["cpu"])

# Check for high CPU usage
for server in servers:
    if server["cpu"] > 40:
        print("Server:", server["name"], "CPU:", server["cpu"], "requires autoscale")
```

## DevOps Monitoring Examples

### CPU Monitoring Script
```python
servers = [
    {"name": "web-1", "cpu": 45},
    {"name": "web-2", "cpu": 85},
    {"name": "db-1", "cpu": 92}
]

for server in servers:
    if server["cpu"] > 80:
        print("ALERT:", server["name"], "CPU high")
    else:
        print(server["name"], "CPU normal")
```

### Memory Usage Classification
```python
memory_usage = int(input("Enter memory usage percentage: "))

if memory_usage > 75:
    print("High memory usage")
elif memory_usage > 50 and memory_usage < 75:
    print("Moderate memory usage")
else:
    print("Low memory usage")
```

## DevOps Interview Insights

### Common Scenarios
- **JSON Responses:** Often receive list of dictionaries from APIs
- **Data Processing:** Need to loop through server data
- **Filtering:** Apply conditional statements to filter specific data
- **Automation:** Process multiple resources simultaneously

### Interview-Level Exercise
Filter and display only stopped servers:
```python
servers = [
    {"name": "api-1", "status": "running"},
    {"name": "api-2", "status": "stopped"}
]

for server in servers:
    if server["status"] == "stopped":
        print("Stopped server is:", server)
```

## Practical Exercises

### Exercise 1: Server Status Check
Create a script that iterates through a list of servers and prints their status.

### Exercise 2: Environment Deployment
Write a loop that deploys applications to multiple environments.

### Exercise 3: Resource Monitoring
Implement a monitoring script that checks CPU, memory, and disk usage across multiple servers.

## Key Learning Outcomes
- Master for and while loops for automation
- Understand when to use break and continue
- Work with lists for managing collections of servers/services
- Use tuples for immutable configuration data
- Leverage dictionaries for structured server data
- Process JSON-like data structures common in DevOps
- Build monitoring and alerting scripts
- Handle multiple resources efficiently

## Files
- `day02.py` - Main Python file with all examples and exercises

## Real-World Applications
- Server provisioning scripts
- Configuration management
- Log processing and analysis
- Monitoring and alerting systems
- Deployment automation
- Infrastructure inventory management

## Next Steps
Day 03 will cover functions, modules, and error handling - essential for building robust DevOps automation scripts.