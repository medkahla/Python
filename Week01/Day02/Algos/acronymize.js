const str1 = " objet oriented programing";
// expected OOP

function acronymize(str){
    var acro = "";
    if (acro == str) {
        return acro;        
    } else {
        // on test [0] if not " " on l'inject à acro w l i=1
        for (var i = 0; i < str.length; i++) {
            if(str[i-1] == " " && str[i] != " ")
            acro += str[i].toUpperCase(); 
        }
        return acro
    }
}

console.log(acronymize(str1));