/*
A-TASK ========= (NodeJS)
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/
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

