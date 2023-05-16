const str1 = "creature";

function reverseString(string){
    var reversed = "";
    if (reversed == string){
        return reversed;
    }
    else{
        for (var i = string.length-1 ; i >= 0 ; i--) {
            reversed += string[i];
        }
        return reversed;
    }
        
}

console.log("Le revers de votre chaine",str1,"est",reverseString(str1));