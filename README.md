# SimpleFirewall
Project to develop a firewall for a school project. My major, General Computer Science (Informatique générale), combines Software and Database Engineering and System and Network Administration, and I am proud to be part of it. My teammate [Antso](https://github.com/scoudaaa) did the front-end and I did the back-end and the controller
</br>
</br>
</br>

## How to use it ?
1. Clone the project:
```bash
git clone https://github.com/johannessram/SimpleFirewall.git
```

2. Make sure you have python3 installed. Visit [the official python website](https://www.python.org/downloads/).

3. You need to have `PyQt5` library installed as well. To make sure it is installed, run:
```bash
pip install PyQt5
pip install pyqt5-tools
```

4. Run `main.py` using python3
```bash
python3 main.py
```

5. Create and Delete the rules you want XD
</br>
</br>
</br>

## Explanation about the fields :
### **chain :**
It is the possible direction of packets

### **option :**
- <a style="color: pink">--I</a> means insert at the beginning to give this rule the highest priority
- <a style="color: pink">--A </a> means insert at the end

### **action :**
It is how to handle the packet: <a style="color: pink"> ACCEPT </a>, <a style="color: pink"> REJECT</a>, <a style="color: pink">DROP </a> it

### **the rest is straightforward :**
**protocol**, **source port**, **destination port**, **source**, **destination** are what they are
</br>
</br>
</br>

# Note :
I encourage you to test it and read the code, i sincerely appreciate getting feedback and code reviews. Contact me here: johannessram@gmail.com.
</br>
My teammate's GitHub username is: [scoudaaa](https://github.com/scoudaaa)
