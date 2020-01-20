import sys # to get errors messages in except block

class Algorithm:
    # alphabet is any
    # scheme is iterable of tuples with len 3 - (word1, word2, stop_flag)
    # options is dict, read from many pairs or dict
    def __init__(self, alphabet = '', scheme = [], options = {}):
        self.alphabet = ''
        self.set_alphabet(alphabet)
        self.scheme = []
        self.set_scheme(scheme)
        self.options = Algorithm.get_base_options()
        self.change_options(options)
    
    def change_options(self, options):
        Algorithm.change_options_from_data(self.options, options)

    def set_alphabet(self, alphabet):
        if type(alphabet) != str:
            raise TypeError('wrong type of alphabet: ' + alphabet)
        if ' ' not in alphabet and '.' not in alphabet:
            self.alphabet = alphabet
        else:
            raise ValueError('invalid alphabet: ' + alphabet)

    def set_scheme(self, scheme):
        # TODO or not TODO verification of substitution_parts[1]
        self.scheme = scheme


    # TODO
    def plus_scheme(self, line):
        pass

    # TODO
    def dif_scheme(self, line):
        pass

    def apply_scheme_once(self, word):
        for substitution in self.scheme:
            i = word.find(substitution[0])
            if i >= 0:
                word = word[:i] + substitution[1] + word[i + len(substitution[0]):]
                return word, substitution[2]
        return word, True
    
    # line is a word
    def run_algorithm(self, word):

        if not Algorithm.is_in_alphabet(word, self.alphabet):
            raise ValueError('input word ' + word + ' not in alphabet ' + self.alphabet)

        stop_flag = False
        while not stop_flag:
            word, stop_flag = self.apply_scheme_once(word)

        return word



    @staticmethod
    def is_in_alphabet(word, alphabet):
        for char in word:
            if char not in alphabet:
                return False
        return True
    

    @staticmethod
    def get_substitution_parts(line, alphabet = ''):

        parts = line.split(' ')

        if parts[1]:
            if parts[1][0] == '.':
                parts[1] = parts[1][1:]
                parts.append(True)
            else:
                parts.append(False)
        else:
            parts.append(False)

        if len(parts) != 3:
            raise ValueError('invalid format of input substitution: ' + line)

        for i in range(2):
            parts[i] = parts[i].strip(' ').rstrip(' ')

        if alphabet and not(Algorithm.is_in_alphabet(parts[0], alphabet) and
        Algorithm.is_in_alphabet(parts[1], alphabet)):
            raise ValueError('invalid format of input substitution: ' + line)

        return tuple(parts)
        

    @staticmethod
    def get_option_parts(line, options = {}):
        # line = 'name: value'
        parts = line.split(':')
        if len(parts) != 2:
            raise ValueError('invalid format of input options: ' + line)
        for i in range(2):
            parts[i] = parts[i].strip(' ').rstrip(' ')
        if options and parts[0] not in options:
            raise ValueError('options: ' + ' '.join(options) + '\ninvalid name of option: ' + parts[0])
        return tuple(parts)

    @staticmethod
    def get_base_options(options_path = "options.txt"):
        options = {}
        with open(options_path, 'r') as f_opt:
            line = f_opt.readline().rstrip('\n')
            while line:
                parts = Algorithm.get_option_parts(line)
                options[parts[0]] = parts[1]
                line = f_opt.readline().rstrip('\n')
        return options
    

    @staticmethod
    def change_options_from_pair(option_pair, options):
        # option_pair = (name, value)
        if option_pair[0] in options:
            # TODO or not TODO verification of option_pair[1]
            options[option_pair[0]] = option_pair[1]
        else:
            raise ValueError('invalid name of option: ' + option_pair[0])

    @staticmethod
    def change_options_from_file(input_path, options):
        with open(input_path, 'r') as f_opt:
            line = f_opt.readline().rstrip('\n')
            while line:
                Algorithm.change_options_from_pair(Algorithm.get_option_parts(line, options), options)
                line = f_opt.readline().rstrip('\n')
            return options, line

    
    @staticmethod
    def change_options_from_data(options, new_options):
        for option in new_options:
            try:
                if len(option) != 2:
                    raise ValueError('wrong format of option: ' + option)
                # if it`s a pair
                Algorithm.change_options_from_pair((option[0], option[1]), options)
            except IndexError:
                try:
                    # if it`s a dict-like obj
                    Algorithm.change_options_from_pair((option, options[option]), options)
                except KeyError:
                    raise ValueError('wrong format of input option ' + option + ' in options: ' + options)
    
    


def from_file(input_path = 'input.txt', output_path = 'output.txt'):

    alg = Algorithm('', [], {})
    commands = {
        'options': lambda line: Algorithm.change_options_from_pair(Algorithm.get_option_parts(line), alg.options),
        'alphabet': alg.set_alphabet,
        'scheme': lambda line: alg.scheme.append(Algorithm.get_substitution_parts(line)),
        # '+scheme': alg.plus_scheme,
        # '-scheme': alg.dif_scheme,
        'run': lambda line: f_out.write(alg.run_algorithm(line) + '\n')
        }
    
    errors = []

    with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
        input_type = ''
        line = f_in.readline().rstrip('\n')
        while line:

            if line in commands:
                input_type = line
                if input_type == 'scheme':
                    alg.scheme = []
            else:
                try:
                    commands[input_type](line)
                except:
                    f_out.write('wrong input\n')
                    errors.append(sys.exc_info()[1])

            line = f_in.readline().rstrip('\n')
    
    for error in errors:
        print(error)


# TODO verification of input
def from_data(options, alphabet, scheme, words):
    alg = Algorithm(alphabet, scheme, options)
    ans = ''
    for word in words:
        ans += alg.run_algorithm(word) + '\n'
    return ans