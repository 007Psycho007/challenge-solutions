/* You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested. */


package main 

import "fmt"

func OtherAngle(a int, b int) int {
    return 180 - a - b
}

func main()  {
    fmt.Println(OtherAngle(30,90))
}
