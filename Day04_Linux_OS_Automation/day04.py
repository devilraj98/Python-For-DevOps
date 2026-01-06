import os
import subprocess

#OS automation matters in DevOps because it allows for efficient management and configuration of operating systems across multiple servers. This automation helps in reducing manual errors, speeding up deployment processes, and ensuring consistency in system configurations. By automating tasks such as software installation, updates, and system monitoring, DevOps teams can focus more on development and less on repetitive administrative tasks.

#Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)


print(subprocess.run(["ls", "-l"]))

result = subprocess.run(
    ["df", "-h"],
    capture_output=True,
    text=True
)

#Real DevOps Script – Disk Check
#import subprocess

def check_disk():
    result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

check_disk()


#Running Commands with Arguments
def list_logs():
     result = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

list_logs()

#Handling Command Failures (MANDATORY)
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

#Service Status Check (Real DevOps Use Case)
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


#Combining OS + Files + Functions


def check_status(file_name):
    with open("servers.txt", "r") as file:
        for server in file:
            print("Checking",server.strip())
            result = subprocess.run(
            ["systemctl", "status",service],
            capture_output = True,
            text = True
            )

check_status("servers.txt")

'''
Exercise 3 (Interview Level): Write a function that:
Checks disk usage using df -h
Prints alert if usage > 80%

'''



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

