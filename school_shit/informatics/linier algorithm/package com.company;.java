package com.company;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;
 
public class Main {
    public static void main(String[] args) {
        int size = 0;
        boolean exit = true;
        Scanner in = new Scanner(System.in);
        while (exit){
            String command = in.nextLine();
            Stack<Integer> stack = new Stack();
 
            switch (command){
                case "push":
                    Integer n = in.nextInt();
                    stack.push(n);
                    System.out.println("ok");
                    size++;
                    break;
                case "pop":
                    System.out.println(stack.pop());
                    size--;
                    break;
                    case "back":
                    System.out.println(stack.peek());
                    break;
                case "size":
                    System.out.println(size);
                    break;
                case "clear":
                    stack.removeAllElements();
                    System.out.println("ok");
                    break;
                case "exit":
                    System.out.println("bye");
                    exit = false;
                    break;
            }
        }
    }
}