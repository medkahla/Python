const arr1 = ["a", "b", "a", "c", "B", "a", "c", "b"]

function makeFrequencyTable(arr){
    obj = {};
    for (var i = 0; i < arr.length; i++) {
        if (obj.hasOwnProperty(arr[i])) {
            obj[arr[i]] += 1;
        }
        else{
            obj[arr[i]] = 1;
        }
    }
    return obj
}

console.log(makeFrequencyTable(arr1));