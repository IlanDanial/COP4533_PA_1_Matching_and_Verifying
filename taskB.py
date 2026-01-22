# Write a separate program (or a separate mode in the same program) that:
# (a) Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates
# (b) checks stability: confirms there is no blocking pair.

def checkValidity(inputFile, matchedFile):
    with open(inputFile, 'r') as f:
        n = int(f.readline().strip()) # 3
    
    # all hospitals unmatched [-1, -1, -1]
    hospitalsMatched = [-1] * n

    # all applicants unmatched [False, False, False]
    applicantsMatched = [False] * n

    # read example.out 
    # 1 2
    # 2 3
    # 3 1
    with open(matchedFile, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # "1 2" into ["1", "2"]
            split = line.split() 
            if len(split) < 2:
                return f"Error: Incorrect format for matching line '{line}'"
            
            # hospital = 1 - 1 = 0 
            hospital = int(split[0]) - 1 
            # applicant = 2 - 1 = 1
            applicant = int(split[1]) - 1

            # invalid hospital or applicant index
            if hospital < 0 or hospital >= n or applicant < 0 or applicant >= n:
                return f"Error: Incorrect hospital or applicant index in line '{line}'"

            # check if hospital isn't matched 
            if hospitalsMatched[hospital] != -1:
                return f"Invalid: Hospital {hospital + 1} matched more than once"
            
            # check if applicant isn't matched
            if applicantsMatched[applicant]:
                return f"Invalid: Applicant {applicant + 1} matched more than once"
            
            # mark hospital as matched to applicant
            hospitalsMatched[hospital] = applicant
            # mark applicant as matched
            applicantsMatched[applicant] = True

            #hospital  [1, -1, -1]
            #applicant [False, True, False]

    # check if all hospitals are matched
    for h in range(n):
        if hospitalsMatched[h] == -1:
            return f"Invalid: Hospital {h + 1} is unmatched"
        
    # check if all applicants are matched
    for a in range(n):
        if not applicantsMatched[a]:
            return f"Invalid: Applicant {a + 1} is unmatched"
        
    return "IsValid"


if __name__ == "__main__": 
    print (checkValidity("example.in", "example.out"))
