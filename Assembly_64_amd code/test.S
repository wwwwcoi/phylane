; filepath: hello.asm
; Simple "Hello, World!" for AMD64 (x86-64) Windows using MASM

.386
.model flat,stdcall
option casemap:none

include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\kernel32.lib

.data
    message db "Hello, World!", 0

.code
main PROC
    ; Get handle to stdout
    invoke  GetStdHandle, -11
    mov     rcx, rax                ; rcx = handle
    lea     rdx, message            ; rdx = pointer to message
    mov     r8d, 13                 ; r8d = length of message
    lea     r9, 0                   ; r9 = pointer to bytes written (optional)
    sub     rsp, 32                 ; shadow space
    call    WriteConsoleA
    add     rsp, 32

    invoke  ExitProcess, 0
main ENDP

END main
