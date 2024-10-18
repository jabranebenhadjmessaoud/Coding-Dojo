
var fruits=["apple","kiwi","banana","strawbery"] ;
function findLongestWord (words) {
        var longest=words[0];
        for(var i=1;i<words.length;i++)
        {
            if (words[i].length>=longest.length)
                longest=words[i] ;
        }
        return longest ;
    }
var affiche=findLongestWord(fruits) ;
console.log(affiche);    
