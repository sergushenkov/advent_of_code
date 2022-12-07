input = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

with open('input.txt', 'r') as file:
    input = file.read()
pwd = ['/']
all_dir = dict()

for bash in input.split('$ '):
    bash = bash.strip()
    if bash == '':
        continue
    elif bash[:2] == 'cd':
        if bash[3:] == '/':
            pwd = ['/']
            all_dir['/'] = [None]
        elif bash[3:] == '..':
            last = pwd.pop()
            if last in all_dir[''.join(pwd)] and all_dir[''.join(pwd) + last][0]:
                all_dir[''.join(pwd)].remove(last)
                all_dir[''.join(pwd)].append(all_dir[''.join(pwd) + last][0])
                dir_flag = True
                for item in all_dir[''.join(pwd)][1:]:
                    if type(item) == type('abc'):
                        dir_flag = False
                        break
                if dir_flag and all_dir[''.join(pwd)][0] is None:
                    all_dir[''.join(pwd)][0] = sum(all_dir[''.join(pwd)][1:])
        else:
            pwd.append(bash[3:])
    else:  # ls
        dir_flag = True
        for line in bash[3:].split('\n'):
            size, name = line.split(' ')
            if size == 'dir':
                dir_flag = False
                if (''.join(pwd) + name) not in all_dir:
                    all_dir[''.join(pwd) + name] = [None]
                all_dir[''.join(pwd)].append(name)
            else:
                all_dir[''.join(pwd)].append(int(size))
        if dir_flag and all_dir[''.join(pwd)][0] is None:
            all_dir[''.join(pwd)][0] = sum(all_dir[''.join(pwd)][1:])
while len(pwd) > 1:
    last = pwd.pop()
    if last in all_dir[''.join(pwd)] and all_dir[''.join(pwd) + last][0]:
        all_dir[''.join(pwd)].remove(last)
        all_dir[''.join(pwd)].append(all_dir[''.join(pwd) + last][0])
        dir_flag = True
        for item in all_dir[''.join(pwd)][1:]:
            if type(item) == type('abc'):
                dir_flag = False
                break
        if dir_flag and all_dir[''.join(pwd)][0] is None:
            all_dir[''.join(pwd)][0] = sum(all_dir[''.join(pwd)][1:])
result = 0
for dir in all_dir:
    if all_dir[dir][0] < 100_000:
        result += all_dir[dir][0]
print(result)
