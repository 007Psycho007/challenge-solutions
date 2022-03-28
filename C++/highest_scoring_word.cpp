
/*
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
*/
#include <string>
#include <vector>
std::string highestScoringWord(const std::string str)
    {
    long score,highest_score;
    std::string tmp; 
    std::stringstream ss(str);
    std::vector<std::string> words;

    while(getline(ss, tmp, ' ')){
        words.push_back(tmp);
        }
    tmp = "";
    for (int i=0;i<(int)words.size();i++) {
        score = 0;
        for (int j=0;j<(int)words[i].length();j++) {
            // We can just use the ASCII Value of the Character and substract 96 to represent the score value since the 
            // ASCII value for the letters start 97 and adds 1 for each letter. 
            score+=words[i][j] - 96;
            }
    
        if (score > highest_score) {
            highest_score = score;
            tmp = words[i];
            }
        }
    return tmp;
    }