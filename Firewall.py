import os
from ParseFirewallOutput import ParseFirewallOutput

DEFAULT_TEXT = '--'


class CommandError(Exception):
    pass

class Firewall:
    def __init__(self):
        self._chain = ('INPUT', 'OUTPUT', 'FORWARD')
        self._target = ('ACCEPT', 'REJECT', 'DROP')
        self._protocol = ('TCP', 'UDP', 'ICMP')
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

    def _validate_args(self, chain, target, bottom=True, protocol=DEFAULT_TEXT, source=DEFAULT_TEXT, sport=0, destination=DEFAULT_TEXT, dport=0):
        print(chain, target, bottom, protocol, source, destination, sport, dport)

        protocol = protocol.upper()
        good_mandatory_args = chain in self._chain and target in self._target
        good_bottom_arg = isinstance(bottom, bool)
        good_protocol_arg = protocol == DEFAULT_TEXT or protocol in self._protocol
        good_dport_arg = isinstance(dport, int) and dport >= 0
        good_sport_arg = isinstance(sport, int) and sport >= 0
        good_port_arg = good_dport_arg and good_sport_arg

        good_optionnal_args = good_protocol_arg and good_port_arg and good_bottom_arg
        if not good_mandatory_args:
            raise CommandError('SOME BAD ARGUMENT PROVIDED AS chain, target, or option')
        if not good_optionnal_args:
            raise CommandError('SOME BAD ARGUMENT PROVIDED AS protocol, source port, destination port, source address, or destination address')

    def _format_priority(self, bottom, chain):
        bottom = int(bottom)
        command = ''
        option = self._option[bottom]
        command += option + chain
        return command

    def _format_protocol_and_port(self, protocol, sport, dport):
        if (dport != 0 or sport != 0) and protocol == DEFAULT_TEXT:
            raise CommandError('SPECIFYING A DPORT WITHOUT A PROTOCOL')
        command = ''
        if protocol != DEFAULT_TEXT:
            command += ' --protocol ' + protocol
        if sport != 0:
            command += ' --sport=' + str(sport)
        if dport != 0:
            command += ' --dport=' + str(dport)
        return command

    def _format_IPs(self, source, destination):
        command = ''
        if source != DEFAULT_TEXT:
            command += ' --source ' + source
        if destination != DEFAULT_TEXT:
            command += ' --destination ' + destination
        return command

    def _format_target(self, target):
        return ' --jump ' + target

    def create_rule(self, chain, target, bottom=True, protocol=DEFAULT_TEXT, source=DEFAULT_TEXT, sport=0, destination=DEFAULT_TEXT, dport=0):
        self._validate_args(chain, target, bottom=bottom, protocol=protocol, source=source, sport=sport, destination=destination, dport=dport)
        command = 'iptables -t filter '
        command += self._format_priority(bottom, chain)
        command += self._format_protocol_and_port(protocol, sport, dport)
        command += self._format_IPs(source, destination)
        command += self._format_target(target)
        print(command)
        return_value = os.system(command + self._redirect_to_output_file)
        if return_value != 0:
            raise CommandError('THIS COMMAND IS INCORRECT')
    
    def delete_rule(self, chain, num):
        if chain not in self._chain:
            raise CommandError('INVALID CHAIN')
        command = 'iptables -D ' + chain + ' ' + str(num)
        return_value = os.system(command)
        if return_value != 0:
            raise CommandError('NUMBER DOES NOT APPEAR IN THE RULES TABLE')
