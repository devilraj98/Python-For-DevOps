#function in python

def deploy():
    print("Deploying application...")

deploy()

#function with parameters
def deploy_app(app_name):
    print("Deploying application:", app_name)

deploy_app("MyApp")


#nested function in python i.e inner function
def myfun():
    s = 'i love DevOps'

    def secondfun():
        print(s)
    secondfun()

myfun()

#functions with multiple parameters and input from user and conditional statements

def is_cpu_alert(server,cpu):
    if cpu >= 75:
        print(server, "CPU is Overloaded")
    elif cpu > 50 and cpu < 75:
        print(server, "CPU is normal")

    else:
        print(server, "CPU is safe")


is_cpu_alert(input("Enter server name:"), int(input("Enter CPU usage:")))



#Real DevOps Pattern – Function + Loop

servers = [
    {"name":"web-01", "cpu": 75},
    {"name":"db-01", "cpu": 30}

]

def check_cpu(servers):
    if servers["cpu"] >=75:
        print(servers, "CPU is Overloaded")
    elif servers["cpu"] > 50 and servers["cpu"] < 75:
        print(servers, "CPU is normal")

    else:
        print(servers, "CPU is safe")


check_cpu(servers[0])   # calling function for first dictionary in list


for server in servers:
    check_cpu(server)      # using loop to iterate over list of dictionaries

#function with return statement
def get_cpu_status(cpu):
    if cpu >= 75:
        return "Overloaded"
    elif cpu > 50 and cpu < 75:
        return "Normal"
    else:
        return "Safe"   
status = get_cpu_status(80)
print("CPU Status is:", status)


