import argparse
import math_lib as ml 

def average(num_list):
    """
    Computes the average of a list of numbers given

    Arguments
    ---------
    num_list : list of ints/floats
    
    Returns
    -------
    average : float
    """
    run_sum = 0

    for value in num_list:
        run_sum = ml.add(run_sum, value)

    average = ml.div(run_sum, len(num_list))
    return(average)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-A',
                        '--average',
                        nargs = '+',
                        help = 'Compute the average of the arguments following this flag',
                        type = float,
                        required = True
                        )

    args = parser.parse_args()
    calc_average = average(args.average)
    str_list = [str(flt) for flt in args.average]
    print("Input List :", ', '.join(str_list))
    print("Average =", calc_average)



if __name__ == "__main__":
    main()