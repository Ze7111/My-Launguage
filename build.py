from backend.core.readBC import rbc

with open('code.re', 'r') as f:
    rbc(f.readlines())
    f.close()