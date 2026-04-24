/* D-TASK (NodeJS)
 Shunday function tuzingki unga integerlardan iborat array pass bolsin va
 function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
 MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini */

// Masalaning yechimi
function getHighestIndex(number) {
    let max = number[0]
    let maxIndex = 0
    for (let i = 0; i < number.length; i++) {

        if (number[i] > max) {
            max = number[i]
            maxIndex = i
        }
    }
    return maxIndex
}

console.log(getHighestIndex([14, 923, 4, 6, 78, 23, 32]))


























/*
C-TASK (NodeJS)

Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har
ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true; */

/*
function checkFruits(a, b) {
    if (a.length !== b.length) {
        return false;
    }
    let sortedA = a.split('').sort().join('');
    let sortedB = b.split('').sort().join('');
    return sortedA === sortedB
}
console.log(checkFruits("apricot", "mandarine"))

*/


/*
B-TASK (Nodejs)

 // Masalaning sharti
Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi. 
*/
/*
// Masalaning yechimi
function countDigits(string) {
    let count = 0;
    for (let i = 0; i < string.length; i++) {
        if (string[i] >= '0' && string[i] <= '9')
            count++
    }
    return count
}
const result1 = countDigits("I was born in 2005")
console.log("result1:", result1)
*/


/*
A - TASK ========= (NodeJS)

// Masalaning sharti
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/
/*
// Masalani yechimi loop for bilan qlamiz

function countLetter(letter, word) {
    let count = 0;
    for (let index = 0; index < word.length; index++)
        if (word[index] === letter) {
            count++
        }
    return count;
}
const result = countLetter("a", "assalomu aleykum");
console.log("result:", result);
*/