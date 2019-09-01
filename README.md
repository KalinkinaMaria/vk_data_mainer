# VK group data mainer
 
## Requirements

- python 3.6 and high
- schedule [0.6.0]
- pytest [5.1.2]
- vk [2.0.2]
- peewee [3.9.6]


## Running

```shell
python vk_mainer.py --input groups.txt
```

## Run tesrt

```shell
python -m pytest tests/
```

## Input

Input file example


```shell
vk.com/rambler 
vk.com/ramblermail 
vk.com/horoscopesrambler 
vk.com/championat 
vk.com/championat.auto 
vk.com/championat_cybersport 
vk.com/livejournal 
vk.com/afisha
```


## Output

Output database file is in 'database/statistics.db'. Change it in setting.py
