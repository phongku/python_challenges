import math

# An isotope has half-life T.
# Return the amount of a starting mass N0
# of the isotope that remains after time t,
def compute_Nt(N0, t, T):
    # Type your code here.
    Nt = N0 * math.e ** (-0.693 * t / T)
    return Nt

# Return the half-life of an isotope given that
# a mass N0 decays to Nt after time t
def compute_T(N0, Nt, t):
    # Type your code here.
    T = -0.693 * t / (math.log(Nt / N0))
    return T

if __name__ == '__main__':
    choice = input()

    if choice == 'N':                     # Calculate amount of material
        # TODO: Read N0, t, and T from one line of input and compute Nt
        N0, t, T = map(float, input().split(" "))
        Nt = compute_Nt(N0, t, T)
        
        print(f'Nt = {Nt:.4f}')
    elif choice == 'T':                    # Calculate half-life
        # TODO: Read N0, Nt, and t from one line of input and compute T
        N0, Nt, t = map(float, input().split(' '))
        T = compute_T(N0, Nt, t)
        
        print(f'T = {T:.4f}')
    else:
        print("invalid choice")
