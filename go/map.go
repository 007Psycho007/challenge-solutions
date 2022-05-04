/*
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
*/ 
package main

import "fmt"

func Maps(x []int) []int {
    var y []int
    for _,v := range x {
        y = append(y,v*2)
        fmt.Println(y)
    }
    return y
}

func main()  {
    x := []int{1,2,3}
    fmt.Println(Maps(x))
}

