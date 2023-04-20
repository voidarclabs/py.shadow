import app
import load
import random



def boot():
    load.msg(random.randint(1, 5))
    app.bootscr()
    app.home()
    print("broken")
    return
        
boot()