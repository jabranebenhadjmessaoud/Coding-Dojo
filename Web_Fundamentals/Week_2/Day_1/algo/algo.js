// in this funcion we need to get each time a random answer
// we need to get a random number from 0.1 to 0.99 by invoking the random function
// we multiplay that number by the length of the array we will get a float number from 1.01 to 9.99
// we will use ceil or floor function on that number to get an integer 
// we will use that integer as an index to get an answer from the arrray given

var lifeAnswers=["aazd","2558","3846",]
function randomAnswer(lifeAnswers){
    var number=Math.random();
    number=number*lifeAnswers.length;
    var aa=Math.floor(number);
    return lifeAnswers[aa];
}