# Write a separate program (or a separate mode in the same program) that:
# (a) Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates
# (b) checks stability: confirms there is no blocking pair.

def checkValidityInput(inputFile):
    #read example.in
    # 3
    # 1 2 3
    # 2 3 1
    # 2 1 3
    # 2 1 3
    # 1 2 3
    # 1 2 3
    with open(inputFile, 'r') as f:
        firstLine = f.readline().strip() # 3
        if firstLine == "":
            return ("Error: Input file is empty")
        
        n = int(firstLine) # 3
        if n <= 0:
            return (f"Error: Number must be positive not {n}")
        
        # read hospital preferences
        hospitalsPrefs = []
        for i in range(n):
            # hospital1 reads "1 2 3"
            line = f.readline().strip()
            if line == "":
                return (f"Error: Incomplete hospital preferences at line {i + 2}")
            
            # hospital1 prefs = [1, 2, 3]
            prefs = [int(x) for x in line.split()]
            if len(prefs) != n:
                return (f"Error: Hospital {i + 1} preferences length is not {n}")
            
            if set(prefs) != set(range(1, n + 1)):
                return (f"Error: Hospital {i + 1} preferences must contain all applicants from 1 to {n}")

            hospitalsPrefs.append(prefs)

        # read applicant preferences
        applicantsPrefs = []
        # applicant1 reads "2 1 3"
        for i in range(n):
            line = f.readline().strip()
            if line == "":
                return (f"Error: Incomplete applicant preferences at line {i + 2 + n}")
            
            # applicant1 prefs = [2, 1, 3]
            prefs = [int(x) for x in line.split()]
            if len(prefs) != n:
                return (f"Error: Applicant {i + 1} preferences length is not {n}")
            
            if set(prefs) != set(range(1, n + 1)):
                return (f"Error: Applicant {i + 1} preferences must contain all hospitals from 1 to {n}")

            applicantsPrefs.append(prefs)
        
    return "IsValid"

def checkValidityMatched(inputFile, matchedFile):
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
                return f"Error: Hospital {hospital + 1} matched more than once"
            
            # check if applicant isn't matched
            if applicantsMatched[applicant]:
                return f"Error: Applicant {applicant + 1} matched more than once"
            
            # mark hospital as matched to applicant
            hospitalsMatched[hospital] = applicant
            # mark applicant as matched
            applicantsMatched[applicant] = True

            #hospital  [1, -1, -1]
            #applicant [False, True, False]

    # check if all hospitals are matched
    for h in range(n):
        if hospitalsMatched[h] == -1:
            return f"Error: Hospital {h + 1} is unmatched"
        
    # check if all applicants are matched
    for a in range(n):
        if not applicantsMatched[a]:
            return f"Error: Applicant {a + 1} is unmatched"
        
    return "IsValid"

# def checkStability(inputFile, matchedFile):

        

if __name__ == "__main__": 
    print("Input validity:", checkValidityInput("example.in"))
    print("Matched validity:", checkValidityMatched("example.in", "example.out"))
    #stability = checkStabilityMatched("example.in", "example.out")
    #if validity != "IsValid":
    #    print(validity)
    #elif stability != "IsStable":
    #    print(stability)
    #else:
    #    print("Matching is valid and stable.")