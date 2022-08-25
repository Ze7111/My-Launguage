from random import randint as r; from rich import console

print = console.Console().print
done_inputs = []
as_statements = []

def module_check(module, line_no, line):
    global print, done_inputs
    try:
        if module in done_inputs:
            print(f"Traceback (Converted to ByteCode):", style = 'red')
            print(f'\tFile "<module_check>" Failed, line 492, in <base_libs.include>', style='red')
            print(f"\t[red]Module Exists : [blue]<{module}>[red] already imported", style='red')
            print(f"Fix:", style= 'green')
            print(f"\tRemove Line {line_no} - {line}", style='green')
            return False
            
        if module == 'requests' and module not in done_inputs:
            import requests
            done_inputs.append(module)
            return True
        
        elif module == 'os' and module not in done_inputs:
            import os
            done_inputs.append(module)
            return True
        
        elif module == 'studio.ze' and module not in done_inputs:
            done_inputs.append(module)
            import rich
        
        else:
            raise ValueError('Module not found')
        
    except ValueError: 
        print(f'    File "<module_check>" Failed, line {line_no + 1}, in <base_libs>', style='red')
        print(f'Module Not Found - No module named <{module}>', end='', style='red')

def validate_syntax(module, ogline, line_no):
    m = str(ogline.replace(' ', ""))
    m = m.split('get')[0]
    m = m + 'get'
    s = str(f"library<{module}>get")
    x = ogline.replace("\n", "")
    if m.startswith(s):
        #print(f"Traceback: Works", style='red')
        return True
    else:
        print(f"Traceback (Converted to ByteCode):", style = 'red')
        print(f'\tFile "<validate_syntax>" Failed, line 48, in <base_libs.include>', style='red')
        print(f"\t[red]Incorrect Syntax : Failure in line [green]'{x}'[red] line no. [blue]{line_no}", style='red')
        print(f"Fix:", style= 'green')
        print(f"\tLine {line_no} should follow this formant, 'library <any lib> get <something> as var'", style='green')
        raise ValueError('Incorrect Syntax')

def get_as_statement(line):
    try:
        global as_statements
        get = line.split('get')[1]
        get = get.split('as')[0]
        get = get.replace(' ', "").replace('\n', "").replace('<', "").replace('>', "")
        line = line.split('as')[1]
        line = line.replace(' ', "").replace(';', "").replace('\n', "")
        statement = get + '=' + line
        as_statements.append(statement)
    except ValueError:
        return

    
    


def includeBase(line, line_no):
    global print, done_inputs, as_statements
    get_as_statement(line)
    ogline = line
    line_no += 1

    try:
        line = line.replace('libraries', "").replace(';', "").replace(' ', "")
        line = line.split('get')[0]
        module = line.replace('<', "").replace('>', "")
        module = module.replace('library', "")
        try:
            validate_syntax(module, ogline, line_no)
        except ValueError:
            m = False 
            raise ValueError('Incorrect Syntax')
        module_check(module, line_no, ogline)
        return as_statements
    
    except ValueError as e:
        if m == False:
            return
        module = 'noneType'
        print('Traceback (Converted to ByteCode):', style='red')
        module_check(module, line_no, line)