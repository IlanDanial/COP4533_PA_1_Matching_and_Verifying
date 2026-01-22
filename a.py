


# while (some hospital is free and hasn’t been matched/assigned to every applicant) {
# Choose such a hospital h
# a = 1st applicant on h's list to whom h has not been
# matched
# if (a is free)
# assign h and a
# else if (a prefers h to her/his current assignment h')
# assign a and h, and h’ has a slot free
# else
# a rejects h
# }

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

def main():
    #input
    hospitals, applicants, n = read_input("example.in")
    #algorithm
    result = gale_shapley(hospitals, applicants, n)
    #output
    for hospital_id in sorted(result.keys()):
        print(f"{hospital_id} {result[hospital_id]}")

if __name__ == "__main__":
    