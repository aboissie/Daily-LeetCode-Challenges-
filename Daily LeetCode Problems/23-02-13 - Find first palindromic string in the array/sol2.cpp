#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool checkPalindrome(string& word){
        int l = 0;
        int r = word.length() - 1;
        while(l < r){
            if(word[l] != word[r]) return false;
            l += 1;
            r -= 1;
        }
        return true;
    }

    string firstPalindrome(vector<string>& words) {
        for (int i = 0; i < words.size(); i++) {
            if (isPalindrome(words[i]))
                return words[i];
        }
        return "";
    }
};