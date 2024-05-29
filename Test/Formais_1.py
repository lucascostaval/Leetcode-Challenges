# 3;A;{C};{1,2,3,&};A,1,A;A,&,B;B,2,B;B,&,C;C,3,C  <- input
# 3;{ABC};{{ABC},{BC},{C}};{1,2,3};{ABC},1,{ABC};{ABC},2,{BC};{ABC},3,{C};{BC},2,{BC};{BC},3,{C};{C},3,{C}  <- output

from typing import List, Dict, Set, Tuple

class QueueNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head: QueueNode = None
        self.tail: QueueNode = None
        self.length: int = 0

    def add(self, x: str | Tuple) -> None:
        new_node = QueueNode(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self) -> str:
        if self.length == 0: return None
        if self.length == 1:
            removed = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return removed.val
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.val

    def is_empty(self) -> bool:
        return self.length == 0
    
    def __len__(self) -> int:
        return self.length

class NondeterministicFiniteAutomata:
    def __init__(self, number_of_states: int, states: List[str], input_symbols: List[str], 
                 transition_function: Dict[Tuple[str, str], List[str]], initial_state: str, final_states: List[str]) -> None:
        self.number_of_states: int = number_of_states
        self.states: List[str] = states
        self.input_symbols: List[str] = input_symbols
        self.transition_function: Dict[Tuple[str, str], List[str]] = transition_function
        self.initial_state: str = initial_state
        self.final_states: List[str] = final_states
        self.epsilon_closure: Dict[str, List[str]] = {}

        self.calculate_epsilon_closure()

    def calculate_epsilon_closure(self) -> Dict[str, Set[str]]:
        for state in self.states:
            queue = Queue()
            queue.add(state)
            visited = set()
            lst: List[str] = []
            while not queue.is_empty():
                node = queue.pop()
                visited.add(node)
                lst.append(node)
                if (node, "&") in self.transition_function:
                    for reached in self.transition_function[(node, "&")]:
                        if reached not in visited: queue.add(reached)
            self.epsilon_closure[state] = lst

class DeterministicFiniteAutomata:
    def __init__(self, number_of_states: int, states: List[str], input_symbols: List[str], 
                 transition_function: Dict[Tuple[str, str], str], initial_state: str, final_states: List[str]) -> None:
        self.number_of_states: int = number_of_states
        self.states: List[str] = states
        self.input_symbols: List[str] = input_symbols
        self.transition_function: Dict[Tuple[str, str], str] = transition_function
        self.initial_state: str = initial_state
        self.final_states: List[str] = final_states

    def print_with_order(self, order: List[Tuple[str, str]]):
        number_of_states = str(self.number_of_states)
        initial_state = self.initial_state
        final_states = "{"+",".join(self.final_states)+"}"
        input_symbols_list = self.input_symbols
        input_symbols_list.sort()
        input_symbols = "{"+",".join(input_symbols_list)+"}"
        result_string = f"{number_of_states};{initial_state};{final_states};{input_symbols};"
        lst = []
        print(order)
        for (state, symbol) in order:
            val = self.transition_function[(state, symbol)]
            if val != r"{}": lst.append(f"{state},{symbol},{val};")
        result_string = result_string+"".join(lst)
        result_string = result_string[:len(result_string)-1]
        return result_string

    def __str__(self) -> str:
        number_of_states = str(self.number_of_states)
        initial_state = self.initial_state
        final_states = "{"+",".join(self.final_states)+"}"
        input_symbols_list = self.input_symbols
        input_symbols_list.sort()
        input_symbols = "{"+",".join(input_symbols_list)+"}"
        print(number_of_states, initial_state, final_states, input_symbols)
        result_string = f"{number_of_states};{initial_state};{final_states};{input_symbols};"
        key_lst = list(self.transition_function.keys())
        key_lst.sort()
        lst = []
        for key in key_lst:
            val = self.transition_function[(key[0], key[1])]
            if val != r"{}": lst.append(f"{key[0]},{key[1]},{val};")
        result_string = result_string+"".join(lst)
        return result_string



class Main:
    def main(self) -> None:
        inp = "4;P;{S};{0,1};P,0,P;P,0,Q;P,1,P;Q,0,R;Q,1,R;R,0,S;S,0,S;S,1,S"
        input_af = inp.split(";")
        number_of_states_input = input_af[0]
        initial_state_input = input_af[1]
        final_states_input = input_af[2]
        input_symbols_input = input_af[3]

        number_of_states = int(number_of_states_input)
        states: List[str] = []
        input_symbols: List[str] = []
        input_symbols_input = input_symbols_input[1:len(input_symbols_input)-1].split(",")
        for symbol in input_symbols_input: 
            if symbol != "&": input_symbols.append(symbol)
        transition_function: Dict[Tuple[str, str], List[str]] = {}
        initial_state: str = initial_state_input
        final_states: List[str] = []
        final_states_input = final_states_input[1:len(final_states_input)-1].split(",")
        for state in final_states_input: final_states.append(state)

        visited: Set[str] = set()
        for i in range(4, len(input_af)):
            transition = input_af[i].split(",")
            state_1 = transition[0]
            input_symbol = transition[1]
            state_2 = transition[2]
            if state_1 not in visited: 
                states.append(state_1)
                visited.add(state_1)
            if state_2 not in visited:
                states.append(state_2)
                visited.add(state_2)
            if (state_1, input_symbol) in transition_function: transition_function[(state_1, input_symbol)].append(state_2)
            else: transition_function[(state_1, input_symbol)] = [(state_2)]

        finite_automata = NondeterministicFiniteAutomata(number_of_states, states, input_symbols, transition_function, 
                                                         initial_state, final_states)
        
        new_initial_state_helper: List[str] = finite_automata.epsilon_closure[finite_automata.initial_state]
        new_transition_function: Dict[Tuple[str, str], str] = {}
        new_initial_state_helper.sort()
        new_initial_state_helper = tuple(new_initial_state_helper)
        new_initial_state = "".join(new_initial_state_helper)
        new_initial_state = "{"+new_initial_state+"}"
        new_final_states: List[str] = []
        queue = Queue()
        queue.add(new_initial_state_helper)
        visited = set()
        new_states = []
        order: List[Tuple[str, str]] = []
        while not queue.is_empty():
            node_helper = queue.pop()
            visited.add(node_helper)
            node = "".join(node_helper)
            node = "{"+node+"}"
            for symbol in finite_automata.input_symbols:
                new_state = []
                inner_visited = set()
                for state in node_helper:
                    if (state, symbol) in finite_automata.transition_function:
                        states = finite_automata.transition_function[(state, symbol)]
                        for s in states:
                            for inner_s in finite_automata.epsilon_closure[s]: 
                                if inner_s not in inner_visited: 
                                    new_state.append(inner_s)
                                    inner_visited.add(inner_s)
                new_state.sort()
                new_state = tuple(new_state)
                new_state_helper = new_state
                new_state = "".join(new_state)
                new_state = "{"+new_state+"}"
                new_transition_function[(node, symbol)] = new_state
                order.append((node, symbol))
                if new_state_helper not in visited and new_state != ():
                    queue.add(new_state_helper)
                    visited.add(new_state_helper)
            is_final_state: bool = False
            for n in node_helper:
                if n in finite_automata.final_states: is_final_state = True
            if is_final_state: new_final_states.append(node)
            new_states.append(node)
        
        new_number_of_states: int = len(new_states)
        new_input_symbols = input_symbols

        resulting_finite_automata = DeterministicFiniteAutomata(new_number_of_states, new_states, new_input_symbols,
                                                                new_transition_function, new_initial_state, new_final_states)
        r = resulting_finite_automata.print_with_order(order)
        print(r)
        

def run() -> None:
    mainObj = Main()
    mainObj.main()

if __name__ == "__main__":
    run()