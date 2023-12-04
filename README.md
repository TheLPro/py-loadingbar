# py-loadingbar
Lightweight loading UI module - coming to Pip
## Bar
### Settings
`Bar.color(c)` - Changes the color of the bar (uses termcolor colors)<br>
`Bar.bar(b)` - Changes the character of the bar<br>
`Bar.fill(f)` - Changes the character of the bar filler<br>
`Bar.speed(min, max, divider)` - Changes the speed of the bar loading<br>
`Bar.prefix(pf)` - Changes the prefix of the bar<br>
`Bar.suffix(sf)` - Changes the suffix of the bar<br>
`Bar.update(percent)` - Updates the bar to a set percent

### Defaults
```
c = "light_green"
b = "█"
d = "•"
s = random.randint(1, 5) / 100
pf = "Loading"
sf = "%"
```

## Stages
### Settings
`Stage.chars(chars[])` - Changes the stages
`Stage.color(c)` - Changes the color of the loader (uses termcolor colors)<br>
`Stage.speed(min, max, divider)` - Changes the speed of the loader<br>
`Stage.prefix(pf)` - Changes the prefix of the loaderr<br>
`Stage.update(percent)` - Updates the loader to a set percent

### Defaults
```
stages = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
c = "light_green"
s = 0.1
pf = "Loading"
```
