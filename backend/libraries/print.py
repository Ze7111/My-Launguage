from rich import console

print = console.Console().print

def var_name(line, ln, statements, colorbool):
    endBool = False
    endif = '\n'
    if colorbool is True:
        try:
            endif = line.split('end')[1].replace('"', '').replace(';', '').replace(' ', '').replace('\n', '').replace('=', '')
            color = line.split('color')[1].replace('"', '').replace(';', '').replace(' ', '').replace('\n', '').replace('=', '').split(',')[0]
            contnent = line.split("=>")[1].split(',')[0].replace('"', '').replace(';', '').replace(' ', '').replace('\n', '').replace('=', '')
            endBool = True
        except:
            color = line.split('color')[1].replace('"', '').replace(';', '').replace(' ', '').replace('\n', '').replace('=', '')
            contnent = line.split("=>")[1].split('"')[1].replace(';', '')
        
        if endBool == False: print(contnent, style=color); 
        elif endBool == True: print(contnent, style=color, end=endif)
        else: return
    
    if colorbool == False:
        contnent = line.split("=>")[1].split('"')[1].replace(';', '')
        print(contnent)
    