// we will create a function which will check if a word is palindrome or not 
//we will create a for loop which will loop through the given string 
// inside the for loop we will test if the first and the last caractere of the string are the same 
//if the two caratcters are not the same the function will exit and return false 


chaine="racecar"
chaine2="wided"
function palindrome(str){

    for (var i=0;i<Math.floor(str.length/2);i++){
        if (str[i]!=str[str.length-1-i])
            return false
    }
    return true

}

console.log (palindrome("helleh"))



function palindrome2(str){
ch2=str.split('').reverse().join('');
if (ch2==str)
    return true
else 
    return false
}
console.log(palindrome2(chaine2))

