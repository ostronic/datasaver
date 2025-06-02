# Datasaver
Datasaver - reduces the MTU(that is the MSS value plus header) randomly, to minimize the data consumed by scavenging websites, and further prolong datausage on your Linux OSx...
Just like the datasaver toggle button on every android devices, it does same economizing your bandwidth cost metric as you surf the internet.
Either you doing CTF, pentesting, watching Youtube videos, surfing Scavenging websites, or Mining crypto.

    ░█████╗░░██████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░░██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔════╝
    ██║░░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝╚█████╗░
    ██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗░╚═══██╗
    ╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝██████╔╝
    ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░
    *********************************************************************
    * Copyright of ostronics(fg_daemon) 2025                            *
    * 'What a wonderful world' :)   zagzag.drank337@passinbox.com       *
    *********************************************************************

        
#Usage:
  #
      cd datasaver/
  #
    sudo python3 datasaver.py <on|off|help>
  or
  #
    sudo python3 datasaver.py on     
  
  To turn on the datsaver(excluding the loopback interface), which randomly changes the MTU value for all Network interfaces(wloX or tunX) in range (1000-1400), and
  #
    sudo python3 datasaver.py off   
  To turn off the datasaver and return it to the normal MTU size(1500)

#:	Author: ostronics {fg_daemon}
#:	Mail:	ostronics@proton.me

#:  This project is open for collaboration, for implementation on Windows OS PC, Miners, and any devices that needs to ecnomize bandwidth why surfing the internet or making requests: Just as the datasaver button is on the scroll bar on Android mobile devices.
