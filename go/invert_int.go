package main    

import "fmt"
func MakeNegative(x int) int {
    if x == 0 {
        return 0
    } else if x < 0{
        return x
    } else {
        return x - (2*x)
    }
}

func main() {
    fmt.Println(MakeNegative(5))
}
