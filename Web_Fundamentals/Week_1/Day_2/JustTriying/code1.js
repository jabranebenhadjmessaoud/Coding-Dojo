var number=5 ;
var str="Hello ";
function stringRepeat(str,number)
    {
        var newstr="";
        for(var i=0;i<number;i++)
        {
            newstr+=str;
        }
        return(newstr);
    }
var word=stringRepeat(str,number);
console.log(word);