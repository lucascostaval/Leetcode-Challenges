# 8;P;{S,U,V,X};{0,1};P,0,Q;P,1,P;Q,0,T;Q,1,R;R,0,U;R,1,P;S,0,U;S,1,S;T,0,X;T,1,R;U,0,X;U,1,V;V,0,U;V,1,S;X,0,X;X,1,V
# 5;P;{S};{0,1};P,0,Q;P,1,P;Q,0,T;Q,1,R;R,0,S;R,1,P;S,0,S;S,1,S;T,0,S;T,1,R

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

    def add(self, x: str) -> None:
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
    def __init__(self, number_of_states: int, states: Set[str], input_symbols: Set[str], 
                 transition_function: Dict[Tuple[str, str], Set[str]], initial_state: str, final_states: Set[str]) -> None:
        self.number_of_states: int = number_of_states
        self.states: Set[str] = states
        self.input_symbols: Set[str] = input_symbols
        self.transition_function: Dict[Tuple[str, str], Set[str]] = transition_function
        self.initial_state: str = initial_state
        self.final_states: Set[str] = final_states
        self.epsilon_closure: Dict[str, Set[str]] = {}

        self.calculate_epsilon_closure()

    def calculate_epsilon_closure(self) -> Dict[str, Set[str]]:
        for state in self.states:
            queue = Queue()
            queue.add(state)
            visited = set()
            while not queue.is_empty():
                node = queue.pop()
                visited.add(node)
                if (node, "&") in self.transition_function:
                    for reached in self.transition_function[(node, "&")]:
                        if reached not in visited: queue.add(reached)
            self.epsilon_closure[state] = visited

class DeterministicFiniteAutomata:
    def __init__(self, number_of_states: int, states: Set[str], input_symbols: Set[str], 
                 transition_function: Dict[Tuple[str, str], str], initial_state: str, final_states: Set[str]) -> None:
        self.number_of_states: int = number_of_states
        self.states: Set[str] = states
        self.input_symbols: Set[str] = input_symbols
        self.transition_function: Dict[Tuple[str, str], str] = transition_function
        self.initial_state: str = initial_state
        self.final_states: Set[str] = final_states

    def minimize(self) -> None:
        def remove_unreachable_states() -> None:
            queue = Queue()
            queue.add(self.initial_state)
            visited = set()
            while not queue.is_empty():
                state = queue.pop()
                visited.add(state)
                for symbol in self.input_symbols:
                    if (state, symbol) in self.transition_function:
                        for s in self.transition_function[(state, symbol)]:
                            if s not in visited: queue.add(s)
            removed_states = self.states.difference(visited)
            self.states = {state for state in self.states if state in visited}
            self.final_states = {state for state in self.final_states if state in visited}
            self.transition_function = {(state, symbol): v for (state, symbol), v in self.transition_function.items() if state in visited}
            self.number_of_states = len(self.states)
            
            #debugging
            #print(removed_states)

        def remove_dead_states() -> None:
            visited = set()
            result = set()
            for state in self.final_states: 
                result.add(state)
                visited.add(state)
            done: bool = False
            while not done:
                done = True
                for (state, symbol) in self.transition_function.keys():
                    if state not in visited and self.transition_function[(state, symbol)] in result:
                        visited.add(state)
                        result.add(state)
                        done = False
            removed_states = self.states.difference(visited) #debugging
            self.states = {state for state in self.states if state in visited}
            self.final_states = {state for state in self.final_states if state in visited}
            self.transition_function = {(state, symbol): v for (state, symbol), v in self.transition_function.items()
                                        if state in visited and v in visited}
            self.number_of_states = len(self.states)

            #debugging
            #print(removed_states)

            #print("After removing dead states:")
            #print(self.transition_function)

        def agroup_equivalent_states() -> None:
            rejected = self.states.difference(self.final_states)
            accepted = self.final_states
            group = {}
            for state in rejected: group[state] = 0 
            for state in accepted: group[state] = 1
            groups = 2
            done: bool = False
            input_symbol_list = list(self.input_symbols)
            input_symbol_list.sort()
            state_list = list(self.states)
            state_list.sort()
            #print("ITERATIONS STARTING")
            while not done:
                #print(group)
                #print("\n")
                group_helper = {}
                for state in state_list:
                    lst_identifier = []
                    for symbol in input_symbol_list:
                        if (state, symbol) in self.transition_function:
                            out_state = self.transition_function[(state, symbol)]
                            lst_identifier.append(group[out_state])
                    tuple_identifier = tuple(lst_identifier)
                    if tuple_identifier in group_helper: group_helper[tuple_identifier].append(state)
                    else: group_helper[tuple_identifier] = [state]
                group = {}
                lst_helper = list(group_helper.keys())
                lst_helper.sort()
                groups_after = 0
                for k in lst_helper:
                    for state in group_helper[k]:
                        group[state] = groups_after
                    groups_after += 1
                    group_helper[k].sort()
                done = groups == groups_after
                groups = groups_after
                
            self.number_of_states = len(group_helper)
            self.states = set()
            removed_states = set()
            removed_to_notremoved = {}
            for value in group_helper.values():
                self.states.add(value[0])
                for i in range(1, len(value)): 
                    removed_states.add(value[i])
                    removed_to_notremoved[value[i]] = value[0]

            self.final_states = {state for state in self.final_states if state not in removed_states}
            self.transition_function = {(state, symbol): v for (state, symbol), v in self.transition_function.items() if state not in removed_states}
            for (state, symbol), v in self.transition_function.items():
                if v in removed_states:
                    self.transition_function[(state, symbol)] = removed_to_notremoved[v]

        remove_unreachable_states()
        remove_dead_states()
        agroup_equivalent_states()

    def __str__(self) -> str:
        number_of_states = str(self.number_of_states)
        initial_state = self.initial_state
        final_states_list = list(self.final_states)
        final_states_list.sort()
        final_states = "{"+",".join(final_states_list)+"}"
        input_symbols_list = list(self.input_symbols)
        input_symbols_list.sort()
        input_symbols = "{"+",".join(input_symbols_list)+"}"

        result_string = f"{number_of_states};{initial_state};{final_states};{input_symbols};"
        key_lst = list(self.transition_function.keys())
        key_lst.sort()
        lst = []
        for key in key_lst:
            val = self.transition_function[(key[0], key[1])]
            if val != r"{}": lst.append(f"{key[0]},{key[1]},{val};")
        result_string = result_string+"".join(lst)
        result_string = result_string[0:len(result_string)-1]
        return result_string

class Main:
    def main(self) -> None:
        input_af = input().split(";")
        number_of_states_input = input_af[0]
        initial_state_input = input_af[1]
        final_states_input = input_af[2]
        input_symbols_input = input_af[3]

        number_of_states = int(number_of_states_input)
        states: Set[str] = set()
        input_symbols: Set[str] = set()
        input_symbols_input = input_symbols_input[1:len(input_symbols_input)-1].split(",")
        for symbol in input_symbols_input: 
            if symbol != "&": input_symbols.add(symbol)
        transition_function: Dict[Tuple[str, str], str] = {}
        initial_state: str = initial_state_input
        final_states: Set[str] = set()
        final_states_input = final_states_input[1:len(final_states_input)-1].split(",")
        for state in final_states_input: final_states.add(state)

        for i in range(4, len(input_af)):
            transition = input_af[i].split(",")
            state_1 = transition[0]
            input_symbol = transition[1]
            state_2 = transition[2]
            states.add(state_1)
            states.add(state_2)
            transition_function[(state_1, input_symbol)] = state_2

        finite_automata = DeterministicFiniteAutomata(number_of_states, states, input_symbols, transition_function, initial_state,
                                                      final_states)
        
        finite_automata.minimize()
        print(finite_automata)

def run() -> None:
    mainObj = Main()
    mainObj.main()

if __name__ == "__main__":
    run()