// testing if the two strings are the same 
// changing the format of both strings to uppercase 
// test if the two strings are the same with an if condition  

AA="Hello";
BB="hello";


function caseIsensitiveStringCompare(AA,BB){
    var UpAA=AA.toUpperCase() ;     //changing to uppercase
    var UpBB=BB.toUpperCase() ;     // changing to uppercase
    if (UpAA==UpBB)                 //testing if eqauls
        return true                 //returning true if equals
    else return false               //returning false if strings are not the same 
}

result=caseIsensitiveStringCompare(AA,BB) ;    
console.log(result) ;


///// second solution 

function caseIsensitiveStringCompare1(AA,BB){
    var i=0
    var result1=true
    while (i<AA.length){
        if  ( AA[i]!=BB[i] ){
            result1=false
            break
        }
    i++ ;    
    }
        
    return result1    

}
AA="Hello";
BB="hello";
var result=caseIsensitiveStringCompare1(AA,BB) ;    
console.log(result) ;