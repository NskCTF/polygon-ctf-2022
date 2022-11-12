package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strconv"
)

func work(conn net.Conn) {
	c := bufio.NewReader(conn)

	for {
		_, err := conn.Write([]byte("Enter 5-digit numeric PIN (example 00000): "))
		if err != nil {
			return
		}
		line, _, err := c.ReadLine()
		if err != nil {
			return
		}
		result, _ := strconv.Atoi(string(line))

		if result == 63825 {
			_, _ = conn.Write([]byte("Good! CTF{3asy_PPC_p1n_guessed}\n"))
			_ = conn.Close()
			return
		} else {
			_, err := conn.Write([]byte("Bad! INCORRECT PIN\n"))
			if err != nil {
				return
			}
		}
	}
}
func main() {
	bindAddr := "0.0.0.0"
	bindPort := 6666

	ln, err := net.Listen("tcp", bindAddr+":"+strconv.Itoa(bindPort))
	if err != nil {
		panic(err)
	}
	log.Printf("Server is ready on [ %s ]\n", bindAddr+":"+strconv.Itoa(bindPort))

	for {
		conn, err := ln.Accept()

		if err != nil {
			fmt.Println(err)
			break
		}

		go work(conn)
	}
}
