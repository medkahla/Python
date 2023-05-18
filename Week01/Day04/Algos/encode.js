const str1 = "aaaabbcddd";

function encodeStr(str){
    if (str == "") {
        return str;
    }
    // for (var i = 0; i < str.length; i+counter-1) {
    //     var char = str[i];
    //     var counter = 1;
    //     while (char == str[counter]) {
    //         counter += 1;           
    //     }
    //     nstr += char+counter;
    //     console.log(nstr);
    // }
    var i=0;
    var nstr = "";
    while (i < str.length){
        var counter = 1;
        var char= str[i];
        if (char==str[i+1]) {
            for (var j = i; j < str.length; j++) {
                if (str[j]==str[j+1]) {
                    counter += 1;
                }  
            }
        }
        nstr += char+counter;
        console.log(nstr);
        i+= counter;
    }
    return nstr;
}

console.log(encodeStr(str1));