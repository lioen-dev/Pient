import os
import configparser
import time
import sys
import random
import terminaltexteffects
from terminaltexteffects.effects.effect_middleout import MiddleOut
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.effects.effect_fireworks import Fireworks
from terminaltexteffects.effects.effect_slide import Slide
from terminaltexteffects.effects.effect_synthgrid import SynthGrid
from terminaltexteffects.effects.effect_errorcorrect import ErrorCorrect
from terminaltexteffects.utils.graphics import Color
import pip

end      = '\33[0m'
italic   = '\33[3m'
blink    = '\33[5m'
red    = '\33[31m'
green  = '\33[32m'
blue   = '\33[34m'
yellow = '\33[33m'
white  = '\33[37m'

config = configparser.ConfigParser()

def n():
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def MiddleOutEffect():
    effect = MiddleOut("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.final_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def PrintEffect():
    effect = Print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.final_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def FireworksEffect():
    effect = Fireworks("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.final_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    effect.effect_config.firework_volume = 0.15
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def SlideEffect():
    effect = Slide("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.final_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    effect.effect_config.merge = True
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def SynthGridEffect():
    effect = SynthGrid("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.text_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def ErrorCorrectEffect():
    effect = ErrorCorrect("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    effect.effect_config.final_gradient_stops = (Color("ffffff"), Color("ffffff"), Color("ffffff"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def printlogo():
    logo = random.randint(1,6)

    if logo == 1:
        MiddleOutEffect()
    elif logo == 2:
        PrintEffect()
    elif logo == 3:
        FireworksEffect()
    elif logo == 4:
        SlideEffect()
    elif logo == 5:
        SynthGridEffect()
    elif logo == 6:
        ErrorCorrectEffect()

def theme():
    configfile = "config.ini"
    if os.path.exists(configfile):
        clear()
        print(color + "Change Theme" + end)
        n()
        print(color + "1. Red" + end)
        print(color + "2. Green" + end)
        print(color + "3. Blue" + end)
        print(color + "4. Yellow" + end)
        print(color + "5. White" + end)
        print(color + "6. Back" + end)
        n()
        choice = input(color + "Enter your choice: " + end)
        try:
            choice = int(choice)
            if choice < 1 or choice > 6:
                raise ValueError
        except ValueError:
            theme()

        if choice == 1:
            config.read(configfile)
            if config.has_section("Theme"):
                config.set("Theme", "color", red)

            else:
                config["Theme"] = {"color": red}

            with open(configfile, "w") as configfile:
                config.write(configfile)
            os.startfile(sys.argv[0])
            sys.exit()

        elif choice == 2:
            config.read(configfile)
            if config.has_section("Theme"):
                config.set("Theme", "color", green)

            else:
                config["Theme"] = {"color": green}

            with open(configfile, "w") as configfile:
                config.write(configfile)
            os.startfile(sys.argv[0])
            sys.exit()

        elif choice == 3:
            config.read(configfile)
            if config.has_section("Theme"):
                config.set("Theme", "color", blue)

            else:
                config["Theme"] = {"color": blue}

            with open(configfile, "w") as configfile:
                config.write(configfile)
            os.startfile(sys.argv[0])
            sys.exit()

        elif choice == 4:
            config.read(configfile)
            if config.has_section("Theme"):
                config.set("Theme", "color", yellow)

            else:
                config["Theme"] = {"color": yellow}

            with open(configfile, "w") as configfile:
                config.write(configfile)
            os.startfile(sys.argv[0])
            sys.exit()

        elif choice == 5:
            config.read(configfile)
            if config.has_section("Theme"):
                config.set("Theme", "color", white)

            else:
                config["Theme"] = {"color": white}

            with open(configfile, "w") as configfile:
                config.write(configfile)
            os.startfile(sys.argv[0])
            sys.exit()

        elif choice == 6:
            settings()

def settings():
    clear()
    print(color + "Settings" + end)
    n()
    print(color + "1. Change Theme" + end)
    print(color + "2. Update pip" + end)
    print(color + "3. Update all packages" + end)
    print(color + "4. Change Startup Page" + end)
    print(color + "5. Show Random Startup Animation" + end)
    print(color + "6. Back" + end)
    n()
    choice = input(color + "Enter your choice: " + end)
    try:
        choice = int(choice)
        if choice < 1 or choice > 6:
            raise ValueError
    except ValueError:
        settings()

    if choice == 1:
        theme()

    elif choice == 2:
        clear()
        print(color + "Updating pip..." + end)
        os.system("pip install --upgrade pip")
        clear()
        n()
        print(color + "pip updated successfully!" + end)
        time.sleep(1)
        settings()

    elif choice == 3:
        clear()
        print(color + "Updating all packages..." + end)
        os.system("pip install pip-review")
        clear()
        os.system("pip-review --local --auto")
        clear()
        n()
        print(color + "All packages updated successfully!" + end)
        time.sleep(1)
        settings()

    elif choice == 4:
        config_file = "config.ini"
        if os.path.exists(config_file):
            clear()
            print(color + "Change Startup Page" + end)
            n()
            print(color + "1. Main Menu" + end)
            print(color + "2. List Packages" + end)
            print(color + "3. Settings" + end)
            print(color + "4. Back" + end)
            n()
            choice = input(color + "Enter your choice: " + end)
            try:
                choice = int(choice)
                if choice < 1 or choice > 4:
                    raise ValueError
            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 4.")
                time.sleep(1)
                settings()

            if choice == 1:
                config.read(config_file)
                if config.has_section("Startup"):
                    config.set("Startup", "page", "main")

                else:
                    config["Startup"] = {"page": "main"}

                with open(config_file, "w") as configfile:
                    config.write(configfile)
                    os.startfile(sys.argv[0])
                    sys.exit()

            elif choice == 2:
                config.read(config_file)
                if config.has_section("Startup"):
                    config.set("Startup", "page", "list")

                else:
                    config["Startup"] = {"page": "list"}

                with open(config_file, "w") as configfile:
                    config.write(configfile)
                    os.startfile(sys.argv[0])
                    sys.exit()

            elif choice == 3:
                config.read(config_file)
                if config.has_section("Startup"):
                    config.set("Startup", "page", "settings")

                else:
                    config["Startup"] = {"page": "settings"}

                with open(config_file, "w") as configfile:
                    config.write(configfile)
                    os.startfile(sys.argv[0])
                    sys.exit()

            elif choice == 4:
                settings()

            clear()
            n()
            print(color + "Startup page changed successfully!" + end)
            time.sleep(1)
            settings()

        else:
            open(config_file, "w") 

    elif choice == 5:
        clear()
        printlogo()
        clear()
        settings()

    elif choice == 6:
        clear()
        n()
        print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
        n()
        function()
           
def install():
    clear()
    print(color + "Install Package" + end)
    n()
    package = input(color + "Enter package name (type 'back' to exit) : " + end)
    if package == "back":
        clear()
        print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
        n()
        function()
        n()
    os.system(f"pip install {package} --user")
    clear()
    n()
    print(color + "Package installed successfully!" + end)
    time.sleep(1)
    clear()
    print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    n()
    function()
    n()

def remove():
    clear()
    print(color + "Remove Package" + end)
    n()
    package = input(color + "Enter package name (type 'back' to exit) : " + end)
    if package == "back":
        clear()
        print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
        n()
        function()
        n()
    os.system(f"pip uninstall {package}")
    clear()
    n()
    print(color + "Package removed successfully!" + end)
    time.sleep(1)
    clear()
    print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    n()
    function()
    n()

def listpackages():
    clear()
    print(color + "List Packages" + end)
    n()
    os.system("pip list")
    n()
    input(color + "Press Enter to continue..." + end)
    clear()
    print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
    n()
    function()
    n()

def function():
    print(color + "1. Install Package" + end)
    print(color + "2. Remove Package" + end)
    print(color + "3. List Packages" + end)
    print(color + "4. Settings" + end)
    print(color + "5. Exit" + end)
    n()
    choice = input(color + "Enter your choice: " + end)
    try:
        choice = int(choice)
        if choice < 1 or choice > 5:
            raise ValueError
    except ValueError:
        clear()
        print("8888888b.  d8b                   888                                       \n888   Y88b Y8P                   888            ))                         \n888    888                       888           (o>  //                     \n888   d88P 888  .d88b.  88888b.  888888        / \ <o)                     \n8888888P   888 d8P  Y8b 888  88b 888        ___\_v_())__                   \n888        888 88888888 888  888 888            || ||                      \n888        888 Y8b.     888  888 Y88b.          ||                         \n888        888  Y8888   888  888  Y888                                     \nThe first pip client. Made by barker.rowan@sugarsalem.com")
        n()
        function()
        n()

    if choice == 1:
        install()

    elif choice == 2:
        remove()

    elif choice == 3:
        listpackages()

    elif choice == 4:
        settings()

    elif choice == 5:
        clear()
        print(color + "Exiting pient... Have a great day!" + end)
        n()
        time.sleep(1)
        sys.exit()

def main():
    clear()
    printlogo()
    n()
    function()

clear()
print("Initializing...")

if not os.path.exists("config.ini"):
    open("config.ini", "w")

config.read("config.ini")
if not config.has_section("Startup"):
    config["Startup"] = {"page": "main"}
with open("config.ini", "w") as configfile:
    config.write(configfile)

if not config.has_section("Theme"):
    config["Theme"] = {"color": white}
with open("config.ini", "w") as configfile:
    config.write(configfile)

config.read("config.ini")
color = config["Theme"]["color"]

if ImportError:
    os.system("python -m ensurepip --upgrade")

if config["Startup"]["page"] == "main":
    main()

elif config["Startup"]["page"] == "list":
    listpackages()

elif config["Startup"]["page"] == "settings":
    settings()
