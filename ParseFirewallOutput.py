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
    def _remove_break(line):
        BREAK_LENGHT = 2
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
    def get_dport(columns):
        PRESENTATION = 'dpt:'
        shift_index_left = -1
        port_detail = columns[len(columns) + shift_index_left]
        try:
            second_word = port_detail.split(' ')[1]
            second_word = second_word.split(PRESENTATION)
            second_word = second_word[1]
        except IndexError as exception:
            print(exception)
            second_word = 'all'
        return second_word

    @staticmethod
    def _split_and_parse(line):
        columns = ParseFirewallOutput._remove_blank_spaces(line)
        dport = ParseFirewallOutput.get_dport(columns)
        columns = columns[0:len(columns) - 1] + [dport]
        return columns

