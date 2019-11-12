#!/usr/bin/env python3
import sys
import sys
from cpu import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Set the file to run as a parameter")
    else:
        file_to_run = sys.argv[1]
        program = []
        with open(file_to_run, 'r') as reader:
            for line in reader.readlines():
                try:
                    program.append(int(line.split(' ')[0], 2))
                except:
                    pass
            cpu = CPU()
            cpu.load(program)
            cpu.run()
