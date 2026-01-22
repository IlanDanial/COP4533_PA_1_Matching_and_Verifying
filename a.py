def read_input(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read().split()
        if not data:
            return {}, {}, 0
        iterator = iter(data)
        n = int(next(iterator))
        
        hospitals = {}
        applicants = {}
        
        for i in range(1, n + 1):
            prefs = []
            for _ in range(n):
                prefs.append(int(next(iterator)))
            hospitals[i] = prefs
    
        for i in range(1, n + 1):
            prefs = []
            for _ in range(n):
                prefs.append(int(next(iterator)))
            applicants[i] = prefs
            
        return hospitals, applicants, n

    except FileNotFoundError:
        print(f"Error: File '{filename}' not in directory.")
        return {}, {}, 0
    except StopIteration:
        print("Error: Data mismatch.")
        return {}, {}, 0

def gale_shapley(hospitals, applicants, n):
    # Initialize
    hospital_match = {i: None for i in range(1, n+1)}
    applicant_match = {i: None for i in range(1, n+1)}
    next_proposal = {i: 0 for i in range(1, n+1)}
    matched_count = 0
    
    while matched_count < n:
        # Find an unmatched hospital
        h = None
        for hospital_id in hospitals:
            if hospital_match[hospital_id] == None:
                h = hospital_id
                break
        
        # h asks the next applicant on their preference list
        a = hospitals[h][next_proposal[h]]
        
        # Case 1: applicant a is currently unmatched
        if applicant_match[a] == None:
            hospital_match[h] = a
            applicant_match[a] = h
            matched_count += 1
        
        # Case 2: Applicant a is has already been matched
        else:
            cur_h = applicant_match[a]
            # Check: if current hospital or new hospital is more preferred
            if applicants[a].index(h) < applicants[a].index(cur_h):
                # Applicant a prefers new hospital h over current hospital cur_h
                hospital_match[cur_h] = None
                hospital_match[h] = a
                applicant_match[a] = h
        
        #  got to next applicant in the hospitals preference list
        next_proposal[h] += 1
    
    return hospital_match

def write_output(filename, result):

    with open(filename, 'w') as f:
        for hospital_id in sorted(result.keys()):
            f.write(f"{hospital_id} {result[hospital_id]}\n")


def main():
    #input
    input_1 = input("Give the input file name: ")
    output_1 = input("Give the output file name: ")

    hospitals, applicants, n = read_input(input_1)
    #algorithm
    result = gale_shapley(hospitals, applicants, n)
    
    #output
    write_output(output_1, result)
    for hospital_id in sorted(result.keys()):
        print(f"{hospital_id} {result[hospital_id]}")

if __name__ == "__main__":
    main()
    