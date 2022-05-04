/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
*/

package main

import "fmt"
import "strings"
func AbbrevName(name string) string{
    split_name := strings.Split(strings.ToUpper(name)," ")
    
    return fmt.Sprintf("%s.%s",split_name[0][:1],split_name[1][:1])
}   

func main()  {
    fmt.Println(AbbrevName("hans zimmer"))
}
