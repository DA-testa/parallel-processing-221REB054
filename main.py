# python3

def parallel_processing(n, m, data):
    output = []
    thread = [0 for i in range(n)]

    for i in range(m):
    
        
        index = thread[0]
        moment = thread[0]
        for j in range(n):
            if thread[j] < moment:
                index = j
                moment = thread[index]

        thread[index] = thread[index] + data[i]

        # create the output pairs
        output.append((index, moment))

    return output

def main():
    firstline = list(map(int, input().split())) # first line - n and m
    n = firstline[0] # n - thread count 
    m = firstline[1]  # m - job count

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    for i,j in result:
        print(i, j)     # print out the results, each pair in it's own line

if __name__ == "__main__":
    main()
