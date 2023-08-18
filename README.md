SimpleFirewall
Project to develop a firewall for a school project. My major, General Computer Science (Informatique generale), combines Software and Database Engineering and System and Network Administration, and I am proud to be part of it. My teammate Scouda did the front-end and I did the back-end and the controller



How to use it ?
Clone the project:
git clone https://github.com/johannessram/SimpleFirewall.git
Run main.py using python3
python3 main.py
Create and Delete the rules you want XD


Explanation about the fields :
chain :
It is the possible direction of packets

option :
--I means insert at the beginning to give this rule the highest priority
--A means insert at the end
action :
It is how to handle the packet: ACCEPT , REJECT, DROP it

the rest is straightforward :
protocol, source port, destination port, source, destination are what they are



Note :
I encourage you to test it and read the code, i sincerely appreciate getting feedback and code reviews. Contact me here: johannessramiandrisoa@gmail.com
