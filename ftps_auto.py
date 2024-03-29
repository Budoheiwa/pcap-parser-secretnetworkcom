#!/usr/bin/python3 

from scapy.all import *
import subprocess
import os
    
def start_ftps_server(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def exec_sniff_parse():
    subprocess.run(["sudo", "python3", "sniff-parse/sniff_parse_FTPS.py"])

if __name__ == "__main__":
    print("Code 1: Starting FTPS server")
    command = "sudo docker restart ftps-server"
    start_ftps_server(command)
    print("\r"+"#" * 50 + "\n")
    
    print("Code 2: Sniffing any FTPS packets with parse")
    exec_sniff_parse()
    print("#" * 50 + "\n")
    
    print("\r"+"Code 3: Uploading files to FTPS server")
    print("Files uploaded successfully.")
    print("\r"+"#" * 50 + "\n")
    
   
    
   
    
    
