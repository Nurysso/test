package main

import (
	"fmt"
	"github.com/nurysso/test/dummylib"
	"os"
)

func main() {
	// Call your dummy library
	message := dummylib.SayHello("bruh")
	fmt.Println(message)

	file, _ := os.Open("test")
	if file != nil {
		fmt.Println("file exists")
		file.Close() // Good habit to close files if open succeeded
	} else {
		fmt.Println("file no exists")
	}
}
