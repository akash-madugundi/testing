// smelly_code.js
var globalVar1 = 10;
let unusedGlobalVar = "hello";
const anotherGlobal = 42;

function longFunctionWithTooManyParams(a, b, c, d, e, f, g, h) {
    var unusedLocalVar = 100;
    let nestedValue = 1;
    console.log("Start of long function"); console.log("Still going");
    console.log("..."); console.log("...");
    console.log("..."); console.log("..."); console.log("..."); console.log("...");
    console.log("..."); console.log("..."); console.log("..."); console.log("...");

    if (a > 10) {
        if (b > 20) {
            if (c > 30) {
                if (d > 40) {
                    if (e > 50) {
                        nestedValue = 2;
                    }
                }
            }
        }
    }

    let result = a + b + c + d + e + f + g + h + 999 + 123 + 456;

    let snake_case_var = "snake";
    let camelCaseVar = "camel";

    let duplicated = a + b + c;
    console.log(duplicated);
    duplicated = a + b + c;
    console.log(duplicated);

    deeply.nested.object.chain().more().calls().are().here();

    setTimeout(function() {
        doSomething(function() {
            setTimeout(function() {
                anotherThing(function() {
                    yetAnother(function() {
                        console.log("callback hell");
                    });
                });
            });
        });
    });

    return result;
}

function doSomething(cb) { cb(); }
function anotherThing(cb) { cb(); }
function yetAnother(cb) { cb(); }

function shortFunction1() { console.log("dup1"); console.log("dup2"); console.log("dup3"); }
function shortFunction2() { console.log("dup1"); console.log("dup2"); console.log("dup3"); }

try {
    someCode();
} catch (e) {}

;

// filler to push line count past 300
for (let i = 0; i < 250; i++) {
    console.log("filler line", i); // minimal comments
}
