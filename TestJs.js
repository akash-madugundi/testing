// badExample.js

function doEverything(a, b, c, d, e, f, g, h) { // Too Many Parameters
    console.log("Starting doEverything"); // Console Log Overuse
    let temp1 = 5; // Magic Number
    let temp2 = 5; // Duplicate Code
    let unusedVar = "I'm not used"; // Unused Variable

    for (let i = 0; i < 5; i++) { // Magic Number
        if (a > 0) {
            if (b > 0) {
                if (c > 0) {
                    if (d > 0) { // Deep Nesting
                        console.log("Deep inside if hell"); // Console Log Overuse
                    }
                }
            }
        }
    }

    const user = getData().process().filter().map().sort().reverse().join("-"); // Long Chained Calls

    try {
        riskyOperation();
    } catch (err) { // Empty Catch Block
    };

    let someNumber = 42; // Magic Number

    doSomethingAgain(a, b, c);
    doSomethingAgain(a, b, c); // Duplicate Code

    console.log("Done");;;;; // Unnecessary Semicolons
}

function doSomethingAgain(a, b, c) {
    console.log("This is another function that repeats code"); // Console Log Overuse
    let temp1 = 5; // Duplicate Code, Magic Number
    console.log(temp1);
}

function getData() {
    return {
        process: function () {
            return {
                filter: function () {
                    return {
                        map: function () {
                            return {
                                sort: function () {
                                    return {
                                        reverse: function () {
                                            return {
                                                join: function (s) {
                                                    return "result" + s + "joined";
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    };
}

function riskyOperation() {
    // No implementation
}

// callback hell
function doAsyncStuff(cb) {
    setTimeout(function () {
        console.log("Step 1 done");
        setTimeout(function () {
            console.log("Step 2 done");
            setTimeout(function () {
                console.log("Step 3 done");
                cb();
            }, 1000);
        }, 1000);
    }, 1000);
}

// inconsistent naming
let myVar = 10;
let my_variable = 20;
let MyVar = 30;
let myvar = 40;

/* This is the only comment in a massive file full of code */
/* Low Comment Density */

// Large File: Let's simulate it by adding lots of junk
for (let i = 0; i < 300; i++) {
    console.log("Spam " + i); // Console Log Overuse + Large File
}

doEverything(1, 2, 3, 4, 5, 6, 7, 8);
doAsyncStuff(() => {
    console.log("Async complete");
});
