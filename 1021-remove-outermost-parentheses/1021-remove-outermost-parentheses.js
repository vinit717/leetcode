/**
 * @param {string} s
 * @return {string}
 */
var removeOuterParentheses = function(s) {
    let result = ''
    let level = 0
    
    for(const item of s) {
        if(item === ')') {
            level--
        }
        if(level >= 1) {
            result += item                
        }
        if(item === '(') {
            level++
        }
    }
    
    return result
    
};