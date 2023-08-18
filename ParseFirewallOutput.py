from abc import ABC

FILE_NAME = 'output_file.txt'

class ParseFirewallOutput(ABC):
    @staticmethod
    def parse():
        with open(FILE_NAME, 'r') as output_file:
            return ParseFirewallOutput._iterate(output_file)

    @staticmethod
    def _iterate(output_file):
        parsed_output = []
        for line in output_file:
            if ParseFirewallOutput._check_substring(line):
                new_item =  ParseFirewallOutput._split_and_parse(line)
                parsed_output.append(new_item)
        return parsed_output

    @staticmethod
    def _check_substring(line):
        PATTERNS = ('ACCEPT', 'REJECT', 'DROP')
        for pattern in PATTERNS:
            if line[0:len(pattern)] == pattern:
                return True
        return False

    @staticmethod
    def _split_and_parse(line):
        columns = ParseFirewallOutput._remove_blank_spaces(line)
        ports = ParseFirewallOutput._get_dport_sport(columns)
        LAST_ITEM_INDEX = len(columns) - 1
        columns = columns[:LAST_ITEM_INDEX] + list(ports.values())
        return columns

    @staticmethod
    def _remove_break(line):
        return line[0:-1]

    @staticmethod
    def _remove_blank_spaces(line):
        line = ParseFirewallOutput._remove_break(line)
        SEPARATOR = ' '
        splitted_columns_with_space = line.split(SEPARATOR)
        columns = [item for item in splitted_columns_with_space if item != '']
        COLUMN_NUMBER = 5
        columns = columns[:COLUMN_NUMBER] + [' '.join(columns[COLUMN_NUMBER:])]
        return columns

    @staticmethod
    def _get_dport_sport(columns):
        last_index = len(columns) -1
        port_detail = columns[last_index]
        port_detail = port_detail.split(' ')
        pack = {'sport': 'all', 'dport': 'all'}
        for word in port_detail:
            ParseFirewallOutput._parse_ports(pack, word)
        return pack

    @staticmethod
    def _parse_ports(pack, word):
        PRESENTATION_dpt = 'dpt:'
        PRESENTATION_spt = 'spt:'
        VALID_INDEX = 1
        if PRESENTATION_dpt in word:
            dport = word.split(PRESENTATION_dpt)
            pack['dport'] = dport[VALID_INDEX]
        elif PRESENTATION_spt in word:
            sport = word.split(PRESENTATION_spt)
            pack['sport'] = sport[VALID_INDEX]
