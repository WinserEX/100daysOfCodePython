
let leap = x => {
    if (x % 4 === 0) {
        if (x % 100 === 0 && x % 400 === 0) {
            console.log("Leap year 1");
        } else if(x % 100 === 0) {
            console.log("Not leap year 1")
        } else {
            console.log("leap year 2")
        }
    } else {
        console.log("Not a leap year 2")
    }
}