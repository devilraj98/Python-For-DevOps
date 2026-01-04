#File handling in Python

#Opening a file
file = open("servers.txt", 'r')  # 'r' mode is for reading

print(file) #prints file object
print("Filename:",file.name) #prints file name
print("mode:", file.mode)    #prints file mode
print("is Closed", file.closed)  #prints if file is closed or not
file.close()   #closing the file
print("is Closed", file.closed)  #prints if file is closed or not


#Reading a file
print("\nReading file content:")
file = open("servers.txt", 'r') #reopening file in read mode
content = file.read()  #reads entire file content
print(content)  #prints file content

#Reading first n characters
file.seek(0)  #moving cursor to the beginning of the file
partial_content = file.read(20)  #reads first 20 characters
print("\nFirst 20 characters:")
print(partial_content)

#Reading line by line
file.seek(0)  #moving cursor to the beginning of the file   
print("\nReading line by line:")
line = file.readline()  #reads first line
while line:
    print(line.strip())  #prints line without extra newline
    line = file.readline()  #reads next line    
    #line = file.readline()  #reads next line

file.close()  #closing the file

#Using 'with' statement for file handling - automatically handles closing the file
print("\nUsing 'with' statement to read file:")
with open("servers.txt", 'r') as file:
    for line in file:
        print(line.strip())

#Writing to a file
print("\nWriting to a file:")
with open("output.txt", 'w') as file:  # 'w' mode is for writing
    file.write("Server Report\n")
    file.write("==============\n")
    file.write("web-01: CPU Usage - 75%\n")
    file.write("db-01: CPU Usage - 30%\n")

print("Data written to output.txt") 
print("output.txt")

#Reading the written file to verify
with open("output.txt", 'r') as file:
    content = file.read()
    print("\nContent of output.txt:")
    print(content)
        
#appending to a file - adding new data without overwriting existing data
with open("output.txt", 'a') as file:  # 'a' mode is for appending
    file.write("cache-01: CPU Usage - 55%\n")
    print("Data appended to output.txt")

#Reading the written file to verify again
with open("output.txt", 'r') as file:
    content = file.read()
    print("\nContent of output.txt:")
    print(content)
        

#Exception handling in file operations
print("\nException handling in file operations:")

try:
    file = open("servers.txt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("unexcpted Error", e)

finally:
    file.close()  #closing the file

#Combining Everything – Real DevOps Script

def check_disk(server,usage):
    try:
        if usage > 75:
            print("ALERT:", server, "Disk usage high")
        elif usage > 50 and usage <= 75:
            print( server, "Disk usage high")
        else:
            print("Disk is Normal")
    except Exception as e:
        print("unexpected error")


servers =[
    {"name":"web-01", "disk": 80},
    {"name":"db-01", "disk": 45},
    {"name":"cache-01", "disk": 60}
]

for server in servers:
    print(f"Checking disk for {server['name']}:")   
    check_disk(server['name'], server['disk'])
    print()

'''
servers = {
    "web-1": 70,
    "db-1": 90
}

for server, usage in servers.items():
    check_disk(server, usage)

'''
''' 
# DevOps Best Practices Learned Today
Always use functions
Never trust input (handle errors)
Read data from files, not hardcode
One function = one responsibility

'''


#Day 3 Exercises (Very Important)
'''Exercise 1: Write a function that:
Takes server name
Takes status (running / stopped)
Prints server health
'''
def server_health(server_name,server_status):
    if server_status == "running":
        print(server_name, "is working properly")
    else:
        print(server_name, "is not Working its stopped")    
servers = [
    {"name":"web-01","status":"running" },      
    {"name":"web-02","status":"stopped" }       

]

for server in servers:  
    server_health(server["name"],server["status"])  


'''Exercise 2: Write a function that: Read a file containing server names and print: Checking <server_name> '''

def check_server_from_file(servers):
    with open("servers.txt","r") as file:
        output = file.read()
        print(output)

servers = file.read()
check_server_from_file(servers)