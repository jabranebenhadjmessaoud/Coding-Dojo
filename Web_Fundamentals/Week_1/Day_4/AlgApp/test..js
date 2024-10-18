//finding the index of a given item in an array 
//we will put -1 in a variable we called index before 
//we will search in the array 
// we loop in the array from the start to the end and check if the given item exist in it 
// while looping the array if we find the wanted item we put the index of that item in the variable index number and the loop will stop 
// as a return of the funcion we get the index  number.


//********************************************* */
item1=["a","b","c"];
searchitem1="c" ;
expected1=2;

function indexof(item,searchitem){
    var index=100;
        for(var i=0;i<item.length;i++)
        {
            if (item[i]=searchitem)
            {
                return i ;
            }
            else
            return-1;
        }
        return index ;

    }
var result1=indexof(item1,searchitem1) ;
console.log(result1,"shouldd be",expected1);
