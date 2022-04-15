"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s: str):
    return len(sorted(s.split(" "), key=lambda x: len(x))[0])
    
def main():
    print(find_short("bitcoin take over the world maybe who knows perhaps"))

if __name__ == "__main__":
    main()
