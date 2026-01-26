from taskB import checkValidityInput, checkValidityMatched, checkStability

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
    applicant_rankings = {}
    for applicant_id in applicants:
        applicant_rankings[applicant_id] = {}
        for rank, hospital_id in enumerate(applicants[applicant_id]):
            applicant_rankings[applicant_id][hospital_id] = rank
    free_hospitals = list(range(1, n + 1))

    while free_hospitals:
        # Find an unmatched hospital
        h = free_hospitals[-1]
        
        # h asks the next applicant on their preference list
        a = hospitals[h][next_proposal[h]]
        
        # Case 1: applicant a is currently unmatched
        if applicant_match[a] == None:
            hospital_match[h] = a
            applicant_match[a] = h
            free_hospitals.pop()
        
        # Case 2: Applicant a is has already been matched
        else:
            new_rank = applicant_rankings[a][h]
            cur_rank = applicant_rankings[a][applicant_match[a]]
            cur_h = applicant_match[a]
            # Check: if current hospital or new hospital is more preferred
            if new_rank < cur_rank:
                # Applicant a prefers new hospital h over current hospital cur_h
                hospital_match[cur_h] = None
                hospital_match[h] = a
                applicant_match[a] = h
                free_hospitals.pop()
                free_hospitals.append(cur_h)
                
        
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
    input_validity = checkValidityInput(input_1)
    if input_validity != "IsValid":
        print(input_validity)
        return

    hospitals, applicants, n = read_input(input_1)
    #algorithm
    result = gale_shapley(hospitals, applicants, n)
    
    #output
    write_output(output_1, result)
    for hospital_id in sorted(result.keys()):
        print(f"{hospital_id} {result[hospital_id]}")

    matched_validity = checkValidityMatched(input_1, output_1)
    if matched_validity != "IsValid":
        print(matched_validity)
        return

    stability = checkStability(input_1, output_1)
    if stability != "IsStable":
        print(stability)
        return

    print("VALID STABLE")

if __name__ == "__main__":
    main()
    