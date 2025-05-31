# Datasaver
datasaver - reduces the MTU(that is the MSS value plus header) randomly, to minimize the data consumed by scavenging websites, and further prolong datausage on your Linux OSx...
Just like the datasaver toggle button on every android devices, it does same economizing your cost metric as you surf the internet.
F#ck NCC tariff. My data last long than their hair dye.

    ░█████╗░░██████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░░██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔════╝
    ██║░░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝╚█████╗░
    ██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗░╚═══██╗
    ╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝██████╔╝
    ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░
    *********************************************************************
    * Copyright of ostronics(fg_daemon) 2025                            *
    * 'What a wonderful world' :)   zagzag.drank337@passinbox.com       *
    * Baba Blue, Look they shaking hands now :) \)                      *
    *********************************************************************

        
 Usage: 
	
 sudo python3 parrotLinuxv2.py on # To power on the datasaver 
 
 sudo python3 parrotLinuxv2.py off # To power off the datasaver

#Synopsis:   
# Added the netck.py (Network check)function -	checks to see if you have a WiFi/Ethernet connection before initiating the datasaver to the interface
  #
    sudo python3 parrotLinuxv2.py -h
  or
  
  #
    sudo python3 parrotLinux2.py --help
  or
  
  #
    sudo python3 parrotLinuxv2.py help
  #
    sudo python3 parrotLinuxv2.py on     
  
  To turn on the datsaver(excluding the loopback interface), which randomly changes the MTU value for all Network interfaces(wloX or tunX) in range (1000-1399), and
 
  #
    sudo python3 parrotLinuxv2.py off   
  To turn off the datasaver and return it to the normal MTU size(1500)

Date:   2025-04-13 - updated 2025-05-31

#:  Version:    3

#:  Author: ostronics {fg_daemon}

#:  This project is open for collaboration, for implementation on Windows OS PC: just as the datasaver button is on the scroll bar on Android mobile devices.
