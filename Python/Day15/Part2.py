


def main():
    gen_A = 512
    gen_B = 191

    pairs = 0
    judge_A_values = []
    judge_B_values = []
    round_num = 0
    while(len(judge_A_values) < 5000000 or len(judge_B_values) < 5000000):
        if round_num%100000 == 0:
            print("At round ", round_num, ":\t", len(judge_A_values), "\tGen_A values\t",  len(judge_B_values), "\tGen_B values", sep='')
        gen_A = (16807 * gen_A) % 2147483647
        gen_B = (48271 * gen_B) % 2147483647
        if(gen_A%4 == 0):
            judge_A_values.append(gen_A)
        if(gen_B%8 == 0):
            judge_B_values.append(gen_B)
        round_num+=1
    
    for i in range(5000000):
        gen_A = judge_A_values[i]
        gen_B = judge_B_values[i]
        if(str(bin(gen_A))[-16:] == str(bin(gen_B))[-16:]):
            pairs+=1

    print(pairs)

main()