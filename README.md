# PROJECT SHADOW
Project shadow is a simple command line based system navigation tool.
It has the ability to perform file explorer functions, google searches and has a terminal.
It also has it's own file system, in tne form of the `filesys` folder, that it can navigate independantly.

## Usage

To boot project shadow, you can use `./boot.sh` or on windows just open the file. You will need to have the latest version of [python](https://www.python.org/downloads/) installed,
and for full functionality, have nano installed on your system. For windows, follow [this tutorial](https://anto.online/tips-and-tools/install-nano-text-editor-on-windows/), 
and for linux, use `sudo apt install nano`. There are different prompts for each 'app'. They are as follows:
```
/~#   home
$~#   files
]~#   google
@~#   terminal
```

### Home Page

The homepage commands are as follows:
```
1         File explorer
2         Google Search
3         Terminal
g         Help
exit      Closes Shadow
clear     Clears screen
exit      Exits script
```
Any unlisted commands will return unrecognised.

### File explorer

The file explorer commands are as follows:
```
ls          lists all files
nano        open text editor
cd          change dir
rm/remove   remove files or dirs
add/touch   add a file
mkdir       add a dir
clear       clear screen
exit        goes back to home
```
Unless you are in root directory, if you use exit the system will exit with a file not found error.
This is normal. Make sure that you are in the root dir before exiting the file explorer

### Google search

When 2 is entered, it will come up with a different prompt from home. This function will only search for urls.
When a url is entered, it will open your primary browser and redirect to that url. There are no special commands 
or flags for this function

### Terminal

The terminal will work the same as a normal linux terminal, with limited functionality. The cd and sudo commands will not work, 
and exit will go back to the homepage. Clear works in the same way, except for the top of the 'app'.

### Misc

The system will run regardless of permission and file placement. All of the files must remain in the same folder for the system to work.
You can substitute the txt files for anything, as long as they are named the same. The load file and msg.txt come from [this repository](https://github.com/voidarclabs/py.loadscr),
and the amount of start prompts can be tweaked in the shadow.py file on [line 8](https://github.com/voidarclabs/py.shadow/blob/main/shadow.py#L8).

The whole system is a callable function, as are all the apps. They can be called by:
```
shadow.boot()      Boot the whole system
app.bootscr()      Load the bootscreen
app.home()         Load the homepage
app.files()        Load the file manager
app.google()       Load the search engine
app.terminal()     Load the terminal
load.msg()         Generate prompts
```
They are all standalone and should work without the rest of the system. NOTE: Upon exit, the function returns and ends the while loop. it does not call another function
When home calls a function, it does not return until it exits.