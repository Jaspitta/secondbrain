# Functions to check and run Turing machines. They use constructs not taught in M269.

from typing import Hashable
from algoesup import check_table

RIGHT = 1
LEFT = -1
STAY = 0


def check_tm(tm: dict, in_symbols: set, out_symbols: set, max_states: int = 0) -> None:
    """Check if Turing machine `tm` is well defined, printing appropriate messages.

    Preconditions: `max_states` >= 0

    Check that:
    - `tm` is a dictionary with keys (state, symbol) and values (symbol, movement, state)
    - each state is a string, each movement is -1, 0 or 1, each symbol is hashable
    - there is a state named 'start'
    - there are no more than `max_states` (if `max_states` > 0)
    - each input symbol is read by some transition
    - each output symbol is either an input symbol or written by some transition
    - each non-blank symbol read is an input symbol or was written by a transition that doesn't read it
    - each non-blank symbol written is an output symbol or is read by a transition that doesn't write it
    """
    if not isinstance(tm, dict):
        print("ERROR: the transition table is not a dictionary")
        return
    from_states = set()
    to_states = set()
    transitions = dict()  # symbol -> (read transitions, write transitions)
    RT, WT = 0, 1
    errors = []

    transition = 0
    for key, value in tm.items():
        transition += 1
        if not isinstance(key, tuple) or len(key) != 2:
            errors.append(f"ERROR in {key}: not a tuple (state, symbol)")
        elif not isinstance(key[0], str):
            errors.append(f"ERROR in {key}: {key[0]} is not a state name (string)")
        elif not isinstance(key[1], Hashable):
            errors.append(f"ERROR in {key}: {key[1]} is not a hashable symbol")
        else:
            (state, symbol) = key
            from_states.add(state)
            if symbol not in transitions:
                transitions[symbol] = (set(), set())
            transitions[symbol][RT].add(transition)
        if not isinstance(value, tuple) or len(value) != 3:
            errors.append(f"ERROR in {value}: not a tuple (symbol, movement, state)")
        elif not isinstance(value[0], Hashable):
            errors.append(f"ERROR in {value}: {value[0]} is not a hashable symbol")
        elif value[1] not in (LEFT, STAY, RIGHT):
            errors.append(f"ERROR in {value}: {value[1]} is not STAY, LEFT or RIGHT")
        elif not isinstance(value[2], str):
            errors.append(f"ERROR in {value}: {value[2]} is not a state name (string)")
        else:
            (symbol, _, state) = value
            to_states.add(state)
            if symbol not in transitions:
                transitions[symbol] = (set(), set())
            transitions[symbol][WT].add(transition)

    if "start" not in from_states:
        errors.append("ERROR: no state named 'start'")
    unreachable = from_states - to_states - {"start"}
    if unreachable:
        errors.append(f"ERROR: no transitions to states {unreachable}")

    # each input symbol must be read by some transition
    not_in = set()
    for symbol in in_symbols:
        if symbol not in transitions or not transitions[symbol][RT]:
            not_in.add(symbol)
    if not_in:
        errors.append(f"ERROR: no transitions read input symbols {not_in}")

    # each output symbol that isn't an input symbol must be written by some transition
    not_out = set()
    for symbol in out_symbols - in_symbols:
        if symbol not in transitions or not transitions[symbol][WT]:
            not_out.add(symbol)
    if not_out:
        errors.append(f"ERROR: no transitions write output symbols {not_out}")

    not_written = set()
    not_read = set()
    for symbol, (read, written) in transitions.items():
        # all symbols read must be on the tape (blank or input symbol) or written by transitions that don't read them
        if symbol is not None and symbol not in in_symbols and read >= written:
            not_written.add(symbol)
        # all symbols written must be blank, input, output symbols or read by transitions that don't write them
        if symbol not in (out_symbols | in_symbols | {None}) and written >= read:
            not_read.add(symbol)
    if not_written:
        errors.append(
            f"ERROR: symbols {not_written} are read but no other transitions write them"
        )
    if not_read:
        errors.append(
            f"WARNING: symbols {not_read} are written but no other transitions read them"
        )

    if max_states > 0:
        num_states = len(from_states | to_states)
        if num_states > max_states:
            errors.append(
                f"WARNING: the machine should have at most {max_states} states but has {num_states}"
            )

    for error in errors:
        print(error)
    if errors == []:
        print("OK: the transition table passed the automatic checks")


def run_tm(tm: dict, tape: list, debug: bool = False, max_steps: int = 100) -> list:
    """Run Turing machine `tm` on the input `tape` and return the resulting output.

    Run the machine from state 'start' until it has done `max_steps` or it halts
    (no transition for current state and symbol). In both cases, return
    the list of symbols from the final position of the head onwards.
    If the head moves to the left of the start of the tape,
    stop the machine and return the empty list.

    If `debug` is True, print each configuration.

    Preconditions:
    - `check_tm` doesn't produce any error messages
    - `tape` is a list of hashable symbols, with None representing the blank symbol
    - `max_steps` > 0
    """
    head = 0
    in_tape = list(tape)
    if tape == []:
        tape = [None]
    symbol = tape[head]
    state = "start"
    step = 0
    if debug:
        print(step, state, tape[:head], symbol, tape[head + 1 :])
    while step < max_steps and (state, symbol) in tm:
        actions = tm[(state, symbol)]
        tape[head] = actions[0]  # write symbol (may be the same)
        head = head + actions[1]  # move left, right or stay
        state = actions[2]  # next state (may be the same)
        step = step + 1

        if head < 0:
            print("ERROR: head has moved left of the start position")
            return []
        elif head == len(tape):
            tape.append(None)  # extend tape when needed

        symbol = tape[head]
        if debug:
            print(step, state, tape[:head], symbol, tape[head + 1 :])
    if step == max_steps:
        print(
            f"WARNING: maximal step {max_steps} reached; could be long input or infinite loop"
        )
    if in_tape != tape[: len(in_tape)]:
        print("WARNING: input has been modified")
    output = tape[head:]
    while output != [] and output[-1] == None:
        output.pop(-1)
    return output


def check_tm_tests(
    tests: list | tuple, in_symbols: set, out_symbols: set, max_tests: int = 0
) -> None:
    """Check the test table for a Turing machine, printing any error messages.

    Check that:
    - the table is a list or tuple
    - the table has at most `max_tests` tests (if `max_tests` > 0)
    - each test is a list or tuple with
        - a string (the test's description)
        - a list (the input tape) only with values from `in_symbols` or `None`
        - a Boolean (the value of the debug flag)
        - a list only with values from `out_symbols` or `None`

    Preconditions: `max_tests` >= 0
    """
    errors = check_table(tests, [list, bool, list], max=max_tests)
    if errors != []:
        in_symbols = in_symbols | {None}
        out_symbols = out_symbols | {None}
        for name, in_tape, debug, out_tape in tests:
            not_in = set(in_tape) - in_symbols
            if not_in != set():
                errors.append(f"test '{name}' has unknown input symbols {not_in}")
            not_out = set(out_tape) - out_symbols
            if not_out != set():
                errors.append(f"test '{name}' has unknown output symbols {not_out}")
    if errors != []:
        for error in errors:
            print(f"Error: {error}.")
    else:
        print("OK: the test table passed the automatic checks.")


def test_tm(tm: dict, tests: list | tuple, show_tests: bool = False) -> None:
    """Run Turing machine `tm` on `tests` and report any failed tests.

    If `show_tests` is True, print each test's name before it's executed.

    Preconditions:
    - `tm` is a valid transition table (use `check_tm` to validate)
    - `tests` is a valid test table (use `check_tm_tests` to validate)
    """
    passed = failed = 0
    for test in tests:
        name = test[0]
        inputs = test[1:-1]
        expected = test[-1]
        if show_tests:
            print(f"Running test {name}...")
        try:
            actual = run_tm(tm, *inputs)
            if actual != expected:
                print(name, "FAILED:", actual, "instead of", expected)
                failed += 1
            else:
                passed += 1
        except Exception as e:
            print(name, "FAILED:", e)
            failed += 1
    if passed + failed == 0:
        rate = 0
    else:
        rate = 100 * passed // (passed + failed)
    print(f"Tests finished: {passed} passed ({rate}%), {failed} failed.")
