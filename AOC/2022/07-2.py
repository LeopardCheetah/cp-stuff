

cur_dir = ['a']

dirs = dict()
sizes = dict()


temp_dir = [] # should only contain sub dir names
temp_dir_size = 0

flag = False


line = input() # $ cd /

for _ in range(1031):
    line = input().strip()


    if line[0] != '$': 
        # add what you've learned to the temp dir 

        if line[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # is a directory.
            s = ''
            for e in cur_dir:
                s += e + ' '
            
            temp_dir.append(s + line.split()[1])
            continue 
        
        temp_dir_size += int(line.split()[0])
        continue 
    
    if flag:
        # we are exiting out of a ls command.
        flag = False 

        s = ''
        for e in cur_dir:
            s += e + ' '

        s = s[:len(s) - 1]

        sizes[s] = temp_dir_size 
        dirs[s] = temp_dir

        temp_dir = []
        temp_dir_size = 0
        
        # somethng figure out the directories.

    
    if line.split()[1] == 'ls':
        flag = True 
        # save dir information!
        # maybe.

        continue 

    # a cd was issued
    if line.split()[2] == '..':
        cur_dir.pop()
        continue 
    
    cur_dir.append(line.split()[2])
    continue 

print(cur_dir)
print(dirs)
print(sizes)
print()


# iterate over everything
final_sizes = [] # absolute dir sizes


def get_size(d):
    # use the dirs/sizes thing.

    _c = sizes[d]
    if d in dirs:
        # iterate.
        for _d in dirs[d]:
            _c += get_size(_d)
    
    return _c 

for d, subdirs in dirs.items():
    # d ~ directory name
    # subdirs ~ list of subdirectories that need to be indexed.
    final_sizes.append([d, get_size(d)])

print(final_sizes)
print()


c = final_sizes[0][1] - 40000000
m = c*1000
n = ''

for ls in final_sizes:
    if ls[1] > c and ls[1] < m:
        m = ls[1]
        n = ls[0]

print(m, n.split()[-1])