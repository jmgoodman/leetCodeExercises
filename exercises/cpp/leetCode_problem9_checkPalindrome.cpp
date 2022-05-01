int popFromLeft(int *x, int *pow10) {
    int pow10val = pow(10,*pow10);
    int res      = *x / pow10val;
    *x           = *x % pow10val;
    return res;
}

int popFromRight(int *x, int *pow10) {
    int res = *x % 10;
    *x      = *x / 10;
    return res;
}

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        } else if (x==0) {
            return true;
        }
        
        int pow10 = log10(x);
        
        // while more than 1 base 10 digit
        while (pow10 > 0) {
            int leftdig  = popFromLeft(&x,&pow10);
            int rightdig = popFromRight(&x,&pow10);
            pow10       -= 2;
            if (leftdig != rightdig) {
                return false;
            }
        }
        
        return true;
    }
};