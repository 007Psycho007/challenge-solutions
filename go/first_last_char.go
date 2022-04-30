package main 

import "fmt"

func RemoveChar(s string) string {
    return s[1:len(s)-1]
}

func main()  {
    fmt.Println(trimLeftChar("Left"))
}

