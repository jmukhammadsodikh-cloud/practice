/* E-TASK (NodeJS)====================

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni
teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh" */

// Masalaning yechimi
function getReverse(name) {
    let b = ""
    for (x of name) {
        b = x + b
    }
    return b
}
console.log(getReverse("Samigjonov"))




/* D-TASK (NodeJS)
 Shunday function tuzingki unga integerlardan iborat array pass bolsin va
 function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
 MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini 

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

console.log(getHighestIndex([14, 923, 4, 6, 78, 23, 32]))*/

/* C-TASK (NodeJS)============

Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har
ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true; 

function checkContent(name1, name2) {
    return name1.split('').sort().join('') === name2.split('').sort().join('');
}

console.log(checkContent("farrux", "firdavs"))
*/




/* B-TASK (Nodejs)==============

 // Masalaning sharti
Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.


// Masalaning yechimi
function countDigits(welcome) {
    count = 0
    for (b of welcome) {
        if (b > 0 && b < 9)
            count += 1
    }
    return count
}

console.log(countDigits("welcome123mybeautiful12guests"))
*/




/* A - TASK (NodeJS) =========

// Masalaning sharti
Shunday 2 parametrli function tuzing,
hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.


// Masalani yechimi loop for bilan qlamiz

function countLetter(letter, word) {
    let count = 0
    for (let x of word) {
        if (x === letter)
            count += 1
    }


    return count
}
console.log(countLetter("a", "assalomu aleykum aka"))
*/