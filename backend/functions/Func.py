from rich import console

print = console.Console().print

funcs = []

def create():
    pass

class list_functions():
    def cleanaddNameLine(line, line_no):
        try:
            global funcs
            ogline = line
            valid = False
            funcName= line.split('func')[1].split('(')[0].strip()
            optinal_parms = line.split('func')[1].split('(')[1].split(')')[0].strip()
            #print("line: ",funcName)
            m = str(ogline.replace(' ', ""))
            s = str(f"func{funcName}({optinal_parms})=[")

            if m.startswith(s):
                valid = True
                #print("valid")
            else:
                valid = False
                raise ValueError('Incorrect Syntax')
            
            if valid == True:
                funcs.append(funcName)
                #print(f"    File \"<create>\" Passed, FuncName {line_no + 1}, in <create>", style='green')
                #print(f"    Function Created: [blue]<{line}>[green]", style='green')
            #print(funcs)
            
        except ValueError:
            x = ogline.replace("\n", "")
            print(f"Traceback (Converted to ByteCode):", style = 'red')
            print(f'\tFile "<cleanAddNameLine>" Failed, line 283, in <base_libs.include>', style='red')
            print(f"\t[red]Incorrect Syntax : Failure in line [green]'{x}'[red] line no. [blue]{line_no}", style='red')
            print(f"Fix:", style= 'green')
            print(f"\tLine {line_no} should follow this formant, 'func <name of func>(<optinal inputs>, <more>, ...) = ['", style='green')