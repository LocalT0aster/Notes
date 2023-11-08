import os

import tiktoken

target_tokens = 3869
token_error = 0

path = 'result.txt'

sum = []
for (dirpath, dirnames, filenames) in os.walk('.'):
    for name in filenames:
        if (name == path):
            continue
        if name.endswith('.md'):
            with open(os.path.join(dirpath, name), 'r') as f:
                sum.append(f'<!--{os.path.join(dirpath, name)}-->\n{f.read()}')

sum = '\n'.join(sum).splitlines()

enc = tiktoken.encoding_for_model("gpt-4")
def tok_count(s):
    return len(enc.encode(s))

def in_range(v: int):
    return v >= target_tokens - token_error and v <= target_tokens + token_error

print(f'Current amount of tokens: {tok_count("".join(sum))}')

l = len(sum)
d = l // 2
e = l - d
while(True):
    s = '\n'.join(sum[:e])
    c = tok_count(s)
    if (in_range(c) or d < 2):
        print(f'Truncated to {c} tokens')
        sum = s
        break
    d //= 2
    e = e + d if c < target_tokens else e - d

with open(path, 'w') as f:
    f.write(sum)
    f.flush()