let num = 100

if (num >= 50) {
    console.log("Big Number")
}else if (num < 50, num > 25) {
    console.log("medium Number")
} else {
    console.log("small number")
}


switch (num) {
    case num>=50:
        console.log("Big Number")
        break
    case num<50,num>25:
        console.log("medium Number")
        break
    case num<25:
        console.log("Small Number")
        break
}