class Proposition:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return isinstance(other, Proposition) and self.name == other.name


class Negation:
    def __init__(self, proposition):
        self.proposition = proposition
    
    def __str__(self):
        return f"~{self.proposition}"
    
    def __hash__(self):
        return hash(self.proposition)
    
    def __eq__(self, other):
        return isinstance(other, Negation) and self.proposition == other.proposition


class Implication:
    def __init__(self, premise, conclusion):
        self.premise = premise
        self.conclusion = conclusion
    
    def __str__(self):
        return f"({self.premise} → {self.conclusion})"


def modus_ponens(p, implication, implication_truth):
    if implication_truth and p == implication.premise:
        return implication.conclusion
    return None


def resolution(clause1, clause2):
    resolvents = []
    for literal in clause1:
        if isinstance(literal, Negation) and literal.proposition in clause2:
            new_clause = (clause1 - {literal}) | (clause2 - {literal.proposition})
            resolvents.append(new_clause)
    return resolvents


def get_clauses(num_clauses):
    clauses = []
    for i in range(num_clauses):
        clause_input = input(f"Enter clause {i + 1} (e.g., a, b): ").split(',')
        clause = {Proposition(literal.strip()) if '~' not in literal else Negation(Proposition(literal.strip()[1:])) for literal in clause_input}
        clauses.append(clause)
    return clauses


def format_clause(clause):
    return '{' + ', '.join(str(literal) for literal in clause) + '}'


def main():
    while True:
        print("\nMenu:")
        print("1. Modus Ponens")
        print("2. Resolution")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            p= input('Enter the Clause with implies: ')
            premise, conclusion = p.split(' implies ')
            truth_of_premise = input(f"Is the premise '{premise}' true? (yes/no): ").strip().lower() == 'yes'

            if truth_of_premise:
                print(conclusion)
            else:
                print(f'{conclusion} not true')

        
        elif choice == '2':
            # Resolution
            num_clauses = int(input("Enter the number of clauses: "))
            clauses = get_clauses(num_clauses)
            
            resolved_clauses = list(clauses)  # Start with the initial clauses
            new_resolved = True
            while new_resolved:
                new_resolved = False
                new_clauses = []
                for i in range(len(resolved_clauses)):
                    for j in range(i + 1, len(resolved_clauses)):
                        clause1 = resolved_clauses[i]
                        clause2 = resolved_clauses[j]
                        resolvents = resolution(clause1, clause2)
                        for new_clause in resolvents:
                            if new_clause not in resolved_clauses:
                                new_clauses.append(new_clause)
                                resolved_clauses.append(new_clause)  # Keep track of new clauses
                                new_resolved = True
                                print(f"Resolving {format_clause(clause1)} and {format_clause(clause2)} gives {format_clause(new_clause)}.")
            
            # Display only the last resolved clause
            if resolved_clauses:
                last_clause = resolved_clauses[-1]
                print("Final resolved clause:")
                print(format_clause(last_clause))
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
