//the problem is we have data inside a data table we should reverse it
//as a return we need to get the array reversed 
// we will start by creating a temporary variable that we will use each time to change 
// we need to loop the half of the table and reverse its component with the oposite one 
//the loop will start from the first component in the table and will stop in the half of it 
//we will show the data table reversed 








var Array=["a","b","c","d","e"] ;
function reverseArray(Array){
    var temp="";
    for(i=0;(i<Array.length/2);i++){
        temp=Array[Array.length-i-1];
        Array[Array.length-i-1]=Array[i];
        Array[i]=temp;}
}
reverseArray(Array);
console.log(Array);

