function join(arr, separator){
    var narr = "";
    if(arr == ""){
        return narr;
    }   
    for (var i = 0; i < arr.length-1; i++) {
        narr += arr[i]+separator;
    }
    narr += arr[i];
    return narr;
}

const arr1 = [1,2,3,4,5,6,7,8];
const separator1 = "- ";
console.log(arr1);
console.log(join(arr1, separator1));