# Loops and Data Structures in Python for DevOps 

# why loops are used in devops automation
# Loops are used in DevOps automation to perform repetitive tasks efficiently, such as iterating over servers, processing logs, or managing configurations across multiple environments.

#for loop

for i in range(5):
    print("Iteration:", i)  #Output: Iteration: 0 to 4

#devops example of for loop
servers = ["server-01", "server-02", "server-03"]

for x in servers:
    print("servers listed is: ",x)

#real usage of for loop in devops
services = ["nginx", "mysql", "redis"]

for service in services:
    print("Service is: ",service)

#deployment script example
environments = ["dev", "staging", "prod"]
for env in environments:
    print("Deploying to:", env)


#while loop
count = 1
while count < 10:
    print("No is: ", count)
    count += 1  #Output: No is: 1 to 9

#break statement in loops
for server in servers:
    if server =="server-02":
        break

    print("Skipping maintenance for:", server)
        
#continue statement in loops

for server in servers:
    if server =="server-02":
        continue

    print("Performing maintenance on:", server)

#list data structure In Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:
'''
Can contain duplicate items
Mutable: items can be modified, replaced, or removed
Ordered: maintains the order in which items are added
Index-based: items are accessed using their position (starting from 0)
Can store mixed data types (integers, strings, booleans, even other lists) '''


servers = ["web-01", "web-02", "db-01"]
print("First server is:", servers[0])  #Output: First server is: web-01

for server in servers:
    print("Server in list:", server)

print("Total servers:", len(servers))  #Output: Total servers: 3

print("Adding a new server.")
servers.append("cache-01")

print("Updated server list:", servers)  #Output: Updated server list: ['web-01', 'web-02', 'db-01', 'cache-01']

print("Removing a server.")
servers.remove("web-02")

#tuple data structure  tuple is similar to a list, but it is immutable, meaning once it is created, its items cannot be changed, added, or removed. Tuples are defined using parentheses () instead of square brackets [].
databases = ("mysql", "postgres", "mongodb")

print("First database is:", databases[0])  #Output: First database is: mysql


#dictionary data structure A dictionary in Python is a built-in data structure that stores data in key-value pairs. Dictionaries are mutable, meaning you can change their contents after creation. They are defined using curly braces {}.

servers = [
    {"name": "app-01", "state": "Running", "cpu": 45},
    {"name": "app-02", "state": "stopped", "cpu": 0},
    {"name": "app-03", "state": "terminated", "cpu":80}

]

for server in servers:
    if server["state"] == "Running":
        print("server name is: " + server["name"], "server cpu is: " + str(server["cpu"])) #Output: server name is: app-01 server cpu is: 45

for server in servers:
    if server["cpu"] > 40:
       print("server : " + server["name"], "and server cpu is: " + str(server["cpu"]), "required autoscale")


# DevOps monitoring script
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


#exercise 3 Write a script that: Takes memory usage as input Prints:“High memory usage” if usage > 75% Prints:“Moderate memory usage” if usage is between 50% and 75% Prints:“Low memory usage” if usage < 50%

memory_usage = int(input("Enter memory usage percentage: "))

if memory_usage > 75:
    print("High memory usage")
elif memory_usage > 50 and memory_usage < 75:
    print("Moderate memory usage")
else:
    print("Low memory usage")


#devOps interview insights
#we will often get 
#JSON responses(list of dictionaries)
#we will have to loop through them
#we will have to apply conditional statements to filter out data


#Exercise 3 (Interview Level) Print only stopped servers
servers = [
    {"name": "api-1", "status": "running"},
    {"name": "api-2", "status": "stopped"}
]


for server in servers:
    if server["status"] == "stopped":
        print("stopped server is:",server)

