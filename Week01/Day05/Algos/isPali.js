const str1 = "racecar"
const str2 = "Dud"
const str3 = "ohox"
const str4 = ""
function isPalindrome(str){
    if (str == "") {
        return "Empty string!";
    }
    var strR = "";
    for (var i = str.length-1 ; i>=0 ; i--) {
        strR += str[i];
    }
    console.log(str);
    console.log(strR);
    if (str == strR) {
        return true;        
    }
    else{
        return false;
    }
}
console.log(isPalindrome(str1));
console.log(isPalindrome(str2));
console.log(isPalindrome(str3));
console.log(isPalindrome(str4));