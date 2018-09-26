

def main():
    gen_A = 512
    gen_B = 191

    pairs = 0
    for round_num in range(40000000):
        if round_num%100000 == 0:
            print("At round ", round_num, ": ", pairs, " pairs", sep='')
        gen_A = (16807 * gen_A) % 2147483647
        gen_B = (48271 * gen_B) % 2147483647
        
        if(str(bin(gen_A))[-16:] == str(bin(gen_B))[-16:]):
            pairs+=1

    print(pairs)

main()