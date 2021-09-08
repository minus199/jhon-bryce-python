import os
import subprocess
import sys
from datetime import datetime
from subprocess import Popen, PIPE

from time import sleep


def wait_for_user(disable = False):
    if not disable:
        input("Hit enter to continue...")


print("Running - python ./hello.py")
status = os.system('python ./hello.py')
print("Child exited with status", status)

# On windows, we need to make sure to specify shell=True or when we want to pass the entire command as one string(instead of list)
# Only if we dont have other choices - creates security risks https://docs.python.org/3/library/subprocess.html#security-considerations
#
# Executing shell commands that incorporate unsanitized input from an untrusted source makes a program vulnerable to shell injection,
# a serious security flaw which can result in arbitrary command execution.
# For this reason, the use of shell=True is strongly discouraged in cases where the command string is constructed from external input.
#
# Try it with a windows path i.e. C:\>folder\file
proc = Popen('python ./hello.py', shell=True)
proc.wait()
print("Child with shell exited with", proc.returncode)

# instead of opening a new shell, we use the python executable directly
proc = Popen([sys.executable, './hello.py'])
proc.wait()
print("Child with executable exited with", proc.returncode)
wait_for_user()

start = datetime.now()

# using bash, find all git directories
cmd = ["find", os.environ['HOME'], '-maxdepth', '3', '-name', '.git']
print(f"Running cmd {' '.join(cmd)}", datetime.now() - start)
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
# the current process is idle, but the subprocess is running in the background. By the time `sleep` finishes, the result will be ready
# notice how long it takes the process to finish if we commen the next line
sleep(10)
(out, err) = p.communicate()

if out:
    file_list = out.decode("utf-8").split('\n')
    print('Found files:\n', '\n'.join(file_list))

if err:
    print('Errors: ', err.decode("utf-8"))

print('Took: ', datetime.now() - start)
wait_for_user()

"""
subprocess.run was added in Python 3.5 as a simplification over subprocess.Popen 
when we just want to execute a command and wait until it finishes, but we don't want to do anything else meanwhile. 

For other cases, we still need to use subprocess.Popen.

The main difference is that subprocess.run executes a command and waits for it to finish, 
while with subprocess.Popen you can continue doing your stuff while the process finishes and then just repeatedly call subprocess.communicate 
yourself to pass and receive data to your process.
"""
completed_proc_without_capture = subprocess.run(["ls", "-l"])  # doesn't capture output
completed_proc_with_capture = subprocess.run(["ls", "-l", "./"], capture_output=True)
output = completed_proc_with_capture.stdout.decode('utf-8').split('\n')

"""
If check is True and the exit code was non-zero, it raises a CalledProcessError. 
The CalledProcessError object will have:
    the return code in the returncode attribute
    output & stderr attributes if those streams were captured.
"""
# todo: uncomment the following line
# subprocess.run("exit 1", shell=True, check=True)
# Traceback (most recent call last):
# subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1
wait_for_user()

# streaming/piping the data -- meaning, we do not need to store the entire result in mem
# `ps` command returns a list of active processes. simillar to Task Manager on windows, only for the CLI
print('Piping between subproces - running the command - ps aux')
proc = os.popen('ps aux')  # another way of doing Popen, but shorter
for index, line in enumerate(proc):
    # splitting each line of the output, stripping empty spaces
    # assigning each column in the output into a variable using destructuring
    (user, pid, cpu_prec, mem, vsz, rss, tty, stat, start, time, cmd, *cols) = [part.strip() for part in line.split(" ") if part]
    short_cmd = cmd[-30:]  # get the last 30 chars of the string `cmd`
    # picking which columns we want to print, and "    centering them    "
    row = [p.center(30) for p in [short_cmd, user, pid, cpu_prec, mem]]
    output = '|'.join(row)
    print(f'{index + 1}\t|', output, '\n')
    if index == 20:  # print only the top rows, just to make the output shorter for our exam
        break
wait_for_user()

print("running the command - ps aux | awk '{print $3}' without loading everything into memory")
# Similar to above, but only printing and using Popen instead of os.popen
# notice ohw we pass a list as cmd and we read directly from the proc's stdout
p = Popen(['ps', 'aux'], stdout=PIPE, stderr=PIPE)
p2 = Popen(['awk', '''{print $3}'''], stdin=p.stdout, stdout=PIPE)  # weird chars so using multiline string
p.stdout.close()
# again, only print the top rows for the sake of the example
cpu_usages = [float(line.strip()) for index, line in enumerate(p2.stdout) if index > 0]
cpu_usage = sum(cpu_usages) / len(cpu_usages)
print("Current CPU usage is: {0:.0f}%".format(cpu_usage * 100))
wait_for_user()

# Similar to above, just using context managers that will make sure the subproc exits automatically when finished using it
print("Using context managers - Running the command - dmesg | grep hda")
with Popen(['grep', 'hda'], stdin=PIPE) as grep, Popen(['dmesg'], stdout=grep.stdin):
    (result, err) = grep.communicate()
    if result:
        print(result.decode("utf-8"))
wait_for_user()


def grep(phrase):
    print(f"Running cmd - {' '.join(cmd)}")
    user_input = input(f"Enter a string to search {phrase} in it:\t").encode()
    with Popen(cmd, stdin=PIPE, stdout=PIPE) as proc:
        (matches, err) = proc.communicate(user_input)
    return f"\nMatch: {matches.decode('utf-8') if len(matches) else 'None'}\n"


print("Write data to process")
cmd = ["grep", "foo", "-"]
print(grep("foo"))
print(grep("foo"))
