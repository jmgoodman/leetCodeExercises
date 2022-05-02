// shit this won't work
// what about b.*bs
// we need a way to check for the start of the following sequence in the template
// and not just the current one!
class Solution {
public:
    bool isMatch(string s, string p) {
        int sRight = 0;
        int pLeft  = 0;
        bool isStillMatch = true;
        
        while (pLeft < p.length()){
            // check if we've exhausted the target
            if (sRight >= s.length()) {
                if (pLeft==p.length() and p[pLeft]=='*'){
                    return true;
                } else {
                    return false
                }
            }
            
            // check if we're looking ahead for an asterisk
            if (not isStillMatch){
                if (p[pLeft]!='*'){
                    return false;
                } else {
                    isStillMatch = true;
                }
            }
            
            // if an asterisk, rules for matching and incrementing our search of template & target
            if (p[pLeft]=='*'){
                if (s[sRight]==p[pLeft-1] or ){
                    sRight += 1;
                } else{
                    pLeft += 1;
                }
            }
            
            // otherwise, match strings literally
            if (s[sRight] != p[pLeft]){
                isStillMatch = false;
                pLeft += 1;
            } else {
                sRight += 1;
                pLeft += 1;
            }
        }
        
        // if we failed to resolve isStillMatch because the template ended prior to lookahead, call it false
        if (not isStillMatch){
            return false;
        } else {
            return True;
        }
            
    }
};