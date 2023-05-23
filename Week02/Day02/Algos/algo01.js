const str1 = "helloo";
const str2 = ""

function removeDup(str){
    if (str=="") {
        return "";        
    }
    var nstr = "";
    for (var i = 0; i < str.length; i++) {
        if (!(nstr.includes(str[i]))) {
            nstr += str[i];          
        }
   }
   return nstr;
}

console.log(removeDup(str1));