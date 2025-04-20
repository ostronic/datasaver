# datasaver
datasaver - reduces the MTU(that is the MSS value plus header) randomly, to minimize the data consumed by scavenging websites

    ░█████╗░░██████╗████████╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░░██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░██║██║██╔══██╗██╔════╝
    ██║░░██║╚█████╗░░░░██║░░░██████╔╝██║░░██║██╔██╗██║██║██║░░╚═╝╚█████╗░
    ██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║██║╚████║██║██║░░██╗░╚═══██╗
    ╚█████╔╝██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░╚███║██║╚█████╔╝██████╔╝
    ░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░╚════╝░╚═════╝░
    \n****************************************************************
    \n* Copyright of ostronics(fg_daemon) 2025                       *
    \n* Buy me a coffe(Mail):   zagzag.drank337@passinbox.com        *
    \n****************************************************************
        
 Usage: 
	
 sudo python3 parrotLinuxv2.py on # To power on the datasaver and choose a random MTU size range(1000-1400)
 
 sudo python3 parrotLinuxv2.py off # To power off the datasaver, and return the MTU size to 1500(default) value


#Synopsis:   
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
  To turn on the datsaver which randomly changes the MTU value for all Network interfaces(wloX or tunX) in range (1000-1399), and
  #
    sudo python3 parrotLinuxv2.py off   
  To turn off the datasaver and return it to the normal MTU size(1500)

Date:   2025-04-13

#:  Version:    2.0

#:  Author: ostronics {fg_daemon}

#:  Mail(Buy me a coffee):  zagzag.drank337@passinbox.com

#:  This project is open for collaboration, for implementation in PC just as the datasaver button is on the Android mobile devices.
#	NOTE: 	
	Comment out the tun0 field in the code, and do not use the data saver on VPN devices 'tunX' if you do not have strong internet connection.
