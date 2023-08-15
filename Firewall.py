import os
from ParseFirewallOutput import ParseFirewallOutput

class CommandError(Exception):
    pass

class Firewall:
    def __init__(self):
        self._chain = ('INPUT', 'OUTPUT', 'FORWARD')
        self._target = ('ACCEPT', 'REJECT', 'DROP')
        self._protocol = ('TCP', 'UDP')
        self._option = ( ' --insert ', ' --append ')
        self._read_rules_command = 'iptables -L '
        self._redirect_to_output_file = '> output_file.txt'
        print('are you a network administrator?')

    def read_rules(self, chain):
        if chain not in self._chain:
            raise CommandError('PLEASE CHOOSE A VALID CHAIN: INPUT, OUTPUT, FORWARD')
        command = self._read_rules_command + chain + ' ' + self._redirect_to_output_file
        return_value = os.system(command)
        if return_value != 0:
            raise CommandError('THIS COMMAND IS INCORRECT')
        parsed = ParseFirewallOutput.parse()
        return parsed

    def create_rule(self, chain, target, bottom=True, protocol='', port=0):
        protocol = protocol.upper()
        command = 'iptables -t filter '
        good_mandatory_args = chain in self._chain and target in self._target
        good_optionnal_args = (protocol == '' or protocol in self._protocol) and (isinstance(port, int) and port >= 0) and isinstance(bottom, bool)
        if not good_mandatory_args or not good_optionnal_args:
            print(protocol == '' or protocol in self._protocol)
            print(isinstance(port, int) and port >= 0)
            print(port)
            raise CommandError('BAD CHAIN OR BAD target')
        
        bottom = int(bottom)
        option = self._option[bottom]
        command += option + chain
        if port != 0 and protocol =='':
            raise CommandError('SPECIFYING A PORT WITHOUT A PROTOCOL')
        elif port != 0 and protocol != '':
            command += ' --protocol ' + protocol + ' --dport=' + str(port)
        elif protocol != '':
            command += ' --protocol ' + protocol
        
        command += ' --jump ' + target
        return_value = os.system(command + self._redirect_to_output_file)
        if return_value != 0:
            raise CommandError('THIS COMMAND IS INCORRECT')
    
    def delete_rule(self, chain, num):
        if chain not in self._chain:
            raise CommandError('INVALID CHAIN')
        command = 'iptables -D ' + chain + ' ' + str(num)
        print(command)
        return_value = os.system(command)
        if return_value != 0:
            raise CommandError('NUMBER DOES NOT APPEAR IN THE RULES TABLE')
