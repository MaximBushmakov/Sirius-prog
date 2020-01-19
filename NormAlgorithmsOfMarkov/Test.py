from Algorithm import Algorithm, from_data, from_file

# Algorithm.is_in_alphabet
tests = {'1': ['1', '111111', '', '2', '12'], '123': ['1111', '123123', '', '0123', '1230', '12032']}
tests_anses = {'1': [True, True, True, False, False], '123': [True, True, True, False, False, False]}
for test_alph in tests:
    for i in range(len(tests[test_alph])):
        assert Algorithm.is_in_alphabet(tests[test_alph][i], test_alph) == tests_anses[test_alph][i], (
            str(tests[test_alph][i]) + ' in ' + test_alph + ' not ' + str(tests_anses[test_alph][i]))

# Algorihtm.get_substitution_parts
alphabet = 'ab'
tests = ['ab ba', ' ', ' a', 'a ', 'a .a']
tests_anses = [('ab', 'ba', False), ('', '', False), ('', 'a', False), ('a', '', False), ('a', 'a', True)]
for i in range(len(tests)):
    assert Algorithm.get_substitution_parts(tests[i], alphabet) == tests_anses[i], (
        str(Algorithm.get_substitution_parts(tests[i], alphabet)) + ' != ' + str(tests_anses[i]))

# Algorihtm.get_option_parts
options = Algorithm.get_base_options()
tests = ['write intermediate: True', 'file with input: output.txt']
tests_anses = [('write intermediate', 'True'),  ('file with input', 'output.txt')]
for i in range(len(tests)):
    assert Algorithm.get_option_parts(tests[i], options) == tests_anses[i], (
        '\n' + str(Algorithm.get_option_parts(tests[i], options)) + '\n' + str(tests_anses[i]))

tests = ['write intermediate: True, file with input: input.txt', 'file without input: input.txt']
for test in tests:
    try:
        Algorithm.get_option_parts(test, options)
        print(test)
        raise AssertionError
    except ValueError:
        pass

# TODO REDO
#Algorithm.get_base_options
ans = {'write intermediate': 'False', 'file with input': 'input.txt', 'file with output': 'output.txt'}
assert Algorithm.get_base_options() == ans, str(Algorithm.get_base_options()) + '\n' + str(ans)

# Algorihtm.change_options_from_pair
options = {'write intermediate': 'True'}
tests = [('write intermediate', 'False'), ('write intermediate', 'False')]
for test in tests:
    Algorithm.change_options_from_pair(test, options)

# Algorihtm.change_options_from_file
options = {'write intermediate': 'True'}
tests = ['write intermediate: False\nwrite intermediate:True', '    write intermediate    :      False      ']
tests_anses = [{'write intermediate': 'True'}, {'write intermediate': 'False'}]
for i in range(len(tests)):
    test = tests[i]
    with open('test_options.txt', 'w') as f_out:
        f_out.write(test)
    Algorithm.change_options_from_file('test_options.txt', options)
    assert options == tests_anses[i], str(i) + ': ' + str(options) + ' != ' + str(tests_anses[i])

# TODO
# Algorithm.change_options_from_data

# TODO
# alg.change_options
# alg.set_alphabet
# alg.set_scheme

# TODO
# alg.plus_scheme
# alg.dif_scheme

# TODO
# alg.apply_scheme_once
# alg.run_algorithm

# TODO
# Algorithm initialization

# TODO
# from_file
# from_data


from_file()