https://www.youtube.com/watch?v=2Fp1N6dof0Y
https://queirozf.com/entries/python-3-subprocess-examples

async with subprocess:
    https://stackoverflow.com/a/636570/6173668


#########################################################################







Use run() instead of call() on Python v3.5+

If shell=True, the command string is interpreted as a raw shell command.

Using shell=True may expose you to code injection if you use user input to build the command string.

subprocess.call("ls -lha", shell=True)
# returns 0 (the return code)





import subprocess

# run() returns a CompletedProcess object if it was successful
# errors in the created process are raised here too
process = subprocess.run('ls -lha', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout

output
# total 20K
# drwxrwxr-x  3 felipe felipe 4,0K Nov  4 15:28 .
# drwxrwxr-x 39 felipe felipe 4,0K Nov  3 18:31 ..
# drwxrwxr-x  2 felipe felipe 4,0K Nov  3 19:32 .ipynb_checkpoints
# -rw-rw-r--  1 felipe felipe 5,5K Nov  4 15:28 main.ipynb





import subprocess

cp = subprocess.run(["ls","-lha"])

cp
# CompletedProcess(args=['ls', '-lha'], returncode=0)





Use check=True to force the Python method to throw an exception if the underlying process encounters errors:

import subprocess

subprocess.run(["ls","foo bar"], check=True)
# -------------------------------------------------------------------
# CalledProcessError                Traceback (most recent call last)
# ----> 1 subprocess.run(["ls","foo bar"], check=True)
# /usr/lib/python3.6/subprocess.py in run(input, timeout, check, *popenargs, **kwargs)
#     416         if check and retcode:
#     417             raise CalledProcessError(retcode, process.args,
# --> 418                                      output=stdout, stderr=stderr)
#     419     return CompletedProcess(process.args, retcode, stdout, stderr)
#     420 
# CalledProcessError: Command '['ls', 'foo bar']' returned non-zero exit status 2.





run() example: using shell=True 
As in the call() example, shell=True, the command string is interpreted as a raw shell command.

Again, Using shell=True may expose you to code injection if you use user input to build the command string.

import subprocess

cp = subprocess.run(["ls -lha"],shell=True)

cp
# CompletedProcess(args=['ls -lha'], returncode=0)




import subprocess

cp = subprocess.run(["ls","foo bar"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

cp.output
# '' (empty string)
cp.stderr
# ls: cannot access 'foo bar': No such file or directory
cp.returncode
# 2




This causes the python program to block until the subprocess returns.

from subprocess import Popen

p = Popen(["ls","-lha"])
p.wait()
# 0





Popen example: Store the output and error messages in a string
import subprocess
from subprocess import Popen

p = Popen(["ls","-lha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

output, errors = p.communicate()

output
# total 20K
# drwxrwxr-x  3 felipe felipe 4,0K Nov  4 15:28 .
# drwxrwxr-x 39 felipe felipe 4,0K Nov  3 18:31 ..
# drwxrwxr-x  2 felipe felipe 4,0K Nov  3 19:32 .ipynb_checkpoints
# -rw-rw-r--  1 felipe felipe 5,5K Nov  4 15:28 main.ipynb

errors
# '' (empty string)





By default, calls to Popen() spawn a subprocess in the background and don't wait for it to terminate (unless you use wait() on the Popen object).

Pipe commands together
Use Popen:

from subprocess import Popen,PIPE

# this is equivalent to ls -lha | grep "foo bar"
p1 = Popen(["ls","-lha"], stdout=PIPE)
p2 = Popen(["grep", "foo bar"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()

output = p2.communicate()[0]






Wait for command to terminate, asynchronously
Use asyncio and await.

Method asyncio.create_subprocess_exec() works much the same way as Popen() but calling wait() and communicate() on the returned objects does not block the processor, so the Python interpreter can be used in other things while the external subprocess doesn't return.

Python 3.6+ is needed here

import asyncio

proc = await asyncio.create_subprocess_exec(
    'ls','-lha',
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE)


# if proc takes very long to complete, the CPUs are free to use cycles for 
# other processes
stdout, stderr = await proc.communicate()

proc.returncode
# 0

# must call decode because stdout is a bytes object
stdout.decode()
# total 24K
# drwxrwxr-x  3 felipe felipe 4,0K Nov  4 17:52 .
# drwxrwxr-x 39 felipe felipe 4,0K Nov  3 18:31 ..
# drwxrwxr-x  2 felipe felipe 4,0K Nov  3 19:32 .ipynb_checkpoints
# -rw-rw-r--  1 felipe felipe  11K Nov  4 17:52 main.ipynb

stderr.decode()
# ''  empty string 




Popen vs run() and call()
call() and run() are convenience functions and should be used for simpler cases.

Popen() is much more powerful and handles all cases, not just simple ones.