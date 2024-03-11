
with open('fastapi/r_logs.log', 'r') as file:
    d = file.readlines()
    
lst = [line for index, line in enumerate(d) if index%2!=0]
print(*lst)

def splitter(line: str):
    return [line.split(":")]


lst1 = map(splitter, lst)
