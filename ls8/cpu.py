"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = []
        self.reg = [0] * 8
        self.pc = 0
        self.running = False

    def load(self, program):
        """Load a program into memory."""

        address = 0

        for instruction in program:
            self.ram.append(instruction)
            address += 1

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

        self.pc += 3

    def ldi(self, reg_a, reg_b):
        """LDI operation to store a variable in register."""

        self.reg[reg_a] = reg_b
        self.pc += 3

    def prn(self, reg_a):
        """Print operation."""

        print(self.reg[reg_a])
        self.pc += 2

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        ir = []
        self.running = True
        while self.running:
            ir.append(self.ram_read(self.pc))

            if ir[-1] == 0b10000010:  # LDI
                self.ldi(self.ram_read(self.pc + 1),
                         self.ram_read(self.pc + 2))

            elif ir[-1] == 0b01000111:  # PRN
                self.prn(self.ram_read(self.pc + 1))

            elif ir[-1] == 0b00000001:  # HLT
                self.running = False

            elif ir[-1] == 0b10100010:  # MUL
                self.alu("MUL", self.ram_read(self.pc + 1),
                         self.ram_read(self.pc + 2))
            else:
                raise Exception("Unknown instruction")
