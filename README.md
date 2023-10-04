# terminal-pomodoro

A customizable Pomodoro Timer CLI tool designed to enhance productivity by segmenting tasks into work and rest intervals. The tool is equipped with intuitive progress bars and alert options.

Prerequisites:

* Linux Operating System
* Python3

Installation:

Clone the repository or directly download the files:

    git clone https://github.com/1darshanpatil/terminal-pomodoro

Change to the extracted directory:

    
    cd terminal-pomodoro


Grant execute permission to the shell script. This `pydeb.sh` is a shell script specifically crafted to generate Debian packages from Python files.
   
   ⚠️ Note: Always review the content of shell scripts before executing them, especially those obtained from the internet.
   
    chmod +x pydeb.sh

Execute the shell script with `pomodoro.py`:
   
    ./pydeb.sh pomodoro.py

Install the generated Debian package:
   
    sudo dpkg -i pomodoro.deb

Resolve dependencies, if any:
   
    sudo apt-get install -f
