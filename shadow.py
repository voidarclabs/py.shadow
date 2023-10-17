import app
import load
import random
import click
import os

@click.group()
@click.pass_context
def shadow(ctx):
    pass

@shadow.command(help='Boot the system normally')
def boot():
    click.echo('Booting the system...')
    load.msg(random.randint(1, 5))
    app.bootscr()
    app.home()
    print("broken")
    return

@shadow.command(help='Boot straight to the homepage')
def fastboot():
    click.echo('Booting to home...')
    app.home()

@shadow.command(help='Boot to the file manager')
def files():
    click.echo('Booting to files...')
    app.files()

@shadow.command(help='Boot to email client')
@click.option('--newmail', is_flag=True, help='Erase email data and input new email')
@click.pass_context
def emails(ctx, newmail):
    if newmail == True:
        os.system('rm email.txt')
        app.email()
    else:
        app.email()

    
if __name__ == '__main__':
    shadow()



def boot():
    load.msg(random.randint(1, 5))
    app.bootscr()
    app.home()
    print("broken")
    return

