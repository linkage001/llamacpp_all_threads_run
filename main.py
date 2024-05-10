import os
import subprocess
import threading


# Function to execute the ping command and print its output
def run_cmd(cmd:str):
    # Start the ping process
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Print the PID of the process
    print(f"The PID of the ping process is: {process.pid}")
    print(os.sched_getaffinity(process.pid)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15} 304 predicted, 319 cached, 45ms per token, 22.29 tokens per second
    print(os.sched_setaffinity(process.pid, {0,1,2,3,4,5,6,7,8,9,10,11}))
    print(os.sched_getaffinity(process.pid)) 
    # t 6  267 predicted, 280 cached, 43ms per token, 23.44 tokens per second
    # t 12 400 predicted, 415 cached, 41ms per token, 24.64 tokens per second

    # Read the output line by line and print it
    for line in process.stdout:
        print(line.strip())


cmd = "/home/username/llama.cpp_main/./server -m /home/username/llama.cpp_main/models/Phi-3-mini-4k-instruct-q4.gguf -t 12 -c 8100 -ngl 0 -ctk f16"

# Create a thread that runs the ping function
ping_thread = threading.Thread(target=run_cmd, args=(cmd,))

# Start the thread
ping_thread.start()
