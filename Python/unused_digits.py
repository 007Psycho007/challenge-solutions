
def unused_digits(*l):
    nums = [i for i in range(0,10)]

    for i in l:
        for c in str(i):
            if int(c) in nums:
                nums.remove(int(c))
    return "".join([str(i) for i in nums])
def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    print(unused_digits(12, 34, 56, 78)) 

if __name__ == "__main__":
    main()
