enum State { whitespace, sign, digit, dead };

class StateMachine {
    State currentState;
    
    int result;
    bool isNegative;
    
    // no need to initialize your own hashmap of digit chars to ints
    // isdigit and char - '0' does that for you
    
    // to sign
    void toSign(char& ch) {
        isNegative = (ch == '-');
        currentState = sign;
    }
    
    // to digit
    void toDigit(int dig) {
        currentState = digit;
        addDigit(dig);
    }
    
    // to dead
    void toDead() {
        currentState = dead;
    }
    
    // add digit
    void addDigit(int& dig) {
        if ( (result > INT_MAX/10) or (result == INT_MAX/10 and dig>INT_MAX%10) ) {
            if (isNegative) {
                result = INT_MIN;
                isNegative = false;
            } else {
                result = INT_MAX;
            }
            toDead();
        } else {
            result *= 10;
            result += dig;
        }
    }
    
public:
    StateMachine() {
        currentState = whitespace;
        result       = 0;
        isNegative   = false;
    }
    
    void transition(char& ch) {
        if (currentState == whitespace) {
            if (ch == ' ') {
                return;
            } else if (ch == '-' or ch == '+') {
                toSign(ch);
            } else if (isdigit(ch)) {
                toDigit(ch - '0');
            } else {
                toDead();
            }
        } else if (currentState != dead) {
            if (isdigit(ch)) {
                toDigit(ch - '0');
            } else {
                toDead();
            }
        }
    }
    
    // getters of private properties
    int getInteger() {
        if (isNegative) {
            return -result;
        } else {
            return result;
        }
    }
    
    State getState() {
        return currentState;
    }
};

class Solution {
public:
    int myAtoi(string s) {
        StateMachine Q;
        
        for (int idx = 0; idx < strlen(s.c_str()) and Q.getState() != dead; idx++) {
            Q.transition(s[idx]);
        }
        
        return Q.getInteger();
    }
};      