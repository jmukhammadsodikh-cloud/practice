/*B-TASK (Nodejs)
Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi. */
// Masalani yechimi
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
