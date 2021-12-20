# wd - warpdir(1)
A bit like [mfaerevaag/wd](https://github.com/mfaerevaag/wd), warp to directories.

### Install
Move, link or copy `wd.py` to `~/bin/wd.py`.

Edit `~.bashrc/.zshrc`:
```
wd()  { 
    cd $(~/bin/wd.py $1) 
}
wdl() {
    cat ~/.wdrc 
}
```

### Usage
A _pathfile_ (`~/.wdrc`) consists of `key=value` pairs of `aliast=path` strings. 

For example, _projc1_ is the alias and _/src/projects/projectOne_ is the destination.
```
proj1=~/src/projects/projectOne
proj2=~/src/projects/projectTwo
```

The _pathfile_ alias is used to move to the destination:
```
$ wd proj1
$ pwd 
/src/projects/projectOne
```

### Extension

```
echo "alias=$(pwd)" >> ~/.wdrc
```

```
# ~/.bashrc||.zshrc
wadd(){
    echo "$1=$(pwd)" >> ~/.wdrc
}
```

```
# ~/.bashrc||.zshrc
wlink(){
    echo "$1=realpath($2)" >> ~.wdrc
}
```
