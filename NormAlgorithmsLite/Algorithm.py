import sys # to get errors messages in except block

class Algorithm:
    # alphabet is string
    # scheme is iterable of tuples with len 3 - (word1, word2, stop_flag)
    # options is dict, read from many pairs or dict
    def __init__(self, alphabet = '', scheme = [], options = {}):
        self.alphabet = ''
        self.set_alphabet(alphabet)
        self.scheme = []
        self.set_scheme(scheme)

    
    def set_alphabet(self, alphabet):

        if type(alphabet) != str:
            raise TypeError('wrong type of alphabet: ' + str(alphabet))

        # ' ' is splitting words, '.' is showing that substitution is final
        if ' ' in alphabet or '.' in alphabet:
            raise ValueError('wrong format of alphabet: ' + alphabet + '\n\'.\' or \' \' mustn`t be in alphabet')

        alphabet_set = set(alphabet)
        if len(alphabet) == len(alphabet_set):
            self.alphabet = alphabet
        else:
            print('Warning: alphabet has the same symbols: ' + alphabet)
            self.alphabet = ''
            for symbol in alphabet_set:
                self.alphabet += symbol

    def set_scheme(self, scheme):
        self.scheme = scheme


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
        i = 0
        while not stop_flag and i < 1000000:
            i += 1
            word, stop_flag = self.apply_scheme_once(word)
        
        if i == 1000000:
            stop_flag = input('Program maybe will working infinitily. Continue? (yes/no) ') == 'no'
        
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

        if parts[1] and parts[1][0] == '.':
            parts[1] = parts[1][1:]
            parts.append(True)
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
   


def from_file(input_path = 'input.txt', output_path = 'output.txt'):

    alg = Algorithm('', [], {})

    commands = {
        'alphabet': alg.set_alphabet,
        'scheme': lambda line: alg.scheme.append(Algorithm.get_substitution_parts(line)),
        'run': lambda line: f_out.write(alg.run_algorithm(line) + '\n')
        }
    
    errors = []

    with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
        input_type = ''

        line = f_in.readline()
        while line:
            line = line.rstrip('\n')

            if line in commands:
                input_type = line

                if input_type == 'alphabet':
                    alg.alphabet = ''
                    alg.scheme = []
                    
                if input_type == 'scheme':
                    alg.scheme = []
            else:
                try:
                    commands[input_type](line)
                except:
                    f_out.write('wrong input\n')
                    errors.append(sys.exc_info()[1])

            line = f_in.readline()
    
    for error in errors:
        print(error)