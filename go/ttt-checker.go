package main

import "fmt"
func IsSolved(board [3][3]int) int {
    // First we convert the array to a slice so we can add the rotated Arrays to it
    win_conditions := board[:]
    for i:=0;i<3;i++ {
        win_conditions = append(win_conditions, ArrayFrom2d(board,i))
    }
    win_conditions = append(win_conditions, [3]int{board[0][0],board[1][1],board[2][2]})
    win_conditions = append(win_conditions, [3]int{board[0][2],board[1][1],board[2][0]})
    // Now we can check the WIn Conditions 
    for _,arr := range(win_conditions) {
        if CheckArray(arr,2) {
            return 2
        }
        if CheckArray(arr,1) {
            return 1
        }
    }   

    // If noone has won we check if the game is over.
    for _,arr := range(board) {
        for _,v := range(arr) {
            if v == 0 {
                return -1
            }
        }
    }

    return 0

}

func ArrayFrom2d(matrix [3][3]int,index int) [3]int{
    new_array := [3]int{}
    for i,a := range(matrix) {
        new_array[i] = a[index]
    }
    return new_array
}

func CheckArray(arr [3]int, num int) bool {
    for _,v := range(arr) {
        if v != num {
            return false
        }
    }
    return true
} 

func main() {
    board := [3][3]int{
        {2, 1, 2},
        {2, 1, 1},
        {0, 2, 1},
    }
    fmt.Println(IsSolved(board))
}   
    // IsSolved(board)

