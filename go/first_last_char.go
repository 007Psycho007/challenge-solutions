/*
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
*/
package main 

import "fmt"

func RemoveChar(s string) string {
    return s[1:len(s)-1]
}

func main()  {
    fmt.Println(RemoveChar("Left"))
}

