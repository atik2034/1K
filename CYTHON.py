#------------- IMPORT ------------#
from os import system as c
import marshal
import base64
import zlib
try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('clear')
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#---------------- LOGO -----------#
print ("jone my teligerm channel ")
logo=''' 
 ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖    ▗▖  ▗▖ ▗▄▄▖
▐▌ ▐▌ █    █  ▐▌▗▞▘     ▝▚▞▘ ▐▌   
▐▛▀▜▌ █    █  ▐▛▚▖       ▐▌  ▐▌   
▐▌ ▐▌ █  ▗▄█▄▖▐▌ ▐▌    ▗▞▘▝▚▖▝▚▄▄▖                                                                                            
'''
#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
    print(40*'-')
    print(' FB PAGE : XYLON ')
    print(' GITHUB  : XYLON')
    print ('Teligerm :https://t.me/KGF_TERMUX_TEAM')
    print(40*'-')
#----------- MAIN FUNCTION ------------#
def main():
    clear()
    print(' [A] FACEBOOK HACK ')
    print(' [B] FREE FIRE HACK ')
    print(' [C] FREE FIRE ID UNBAN ')
    print(' [D] TIK TOK HACK ')
    print(' [E] IMO HACK ')
    print(' [F] WIFI PASSWORD HACK ')
    print(' [G] WIFI MAC BYPASS ')
    print(' [H] GMAIL HACKING ')
    print(' [0] EXIT TERMINAL ')
    print(40*'-')
    option=input(' [?] CHOICE MENU : ')
    if option in ['a','A']:
        marshal_enc()
    elif option in ['b','B']:
        base64_enc()
    elif option in ['c','C']:
        zlib_enc()
    elif option in ['d','D']:
        cython_executable()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    file=input(' ENTER YOUR PROFILE LINK : ')
    filex=input('This tool is paid, and its price is 1k Taka.')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write(run_code)
    out_put.close()
    print(40*'-')
    print(' [✓✓]This tool is paid, and its price is 1k Taka.')
    print(' [✓✓]  This tool is paid, and its price is 1k Taka.√'+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    input_file=input(' ENTER UID PATH : ')
    output_file=input(' This tool is paid, and its price is 1k Taka.: ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√:/')
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√: '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    src=input(' ENTER BAN UID : ')
    exit('  :/')
    save_file=input(' This tool is paid, and its price is 1k Taka.√>>: ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√:/')
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√: '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
    clear()
    file=input(' ENTER SOURCE FILE PATH : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√:")')
    save=file[:-3]
    print(' [✓✓] This tool is paid, and its price is 1k Taka.√√: '+save)
#----------------- END --------------#
main()