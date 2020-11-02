import subprocess,os,signal,time
import psutil, time

# subprocess.call(['gnome-terminal', '-x', 'python', 'script1.py'])
# subprocess.call(['gnome-terminal', '-x', 'python', 'script2.py'])

# proc1 = subprocess.Popen("gnome-terminal -- python script1.py",preexec_fn=os.setpgrp,shell=True)
subp = subprocess.Popen(['gnome-terminal', '--', 'python','script2.py'])

subp.communicate()


time.sleep(3)
subp.terminate()