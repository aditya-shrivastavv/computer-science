package sort;

import java.util.Arrays;
import java.util.Scanner;

public class bubbleSort {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int[] arr = new int[8];

    System.out.println("Enter 8 elements in the array");

    for (int i = 0; i < arr.length; i++) {
      System.out.print("Enter "+(i+1)+" element of array: ");
      int element = input.nextInt();
      arr[i] = element;
    }

    // sort begins here
    for (int j = 0; j < arr.length; j++) {
      for (int i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i+1]) {
          int temp = arr[i];
          arr[i] = arr[i+1];
          arr[i+1] = temp;
        }
      }
    }
    printArray(arr);

    input.close();
  }

  // make a method to print the array
  public static void printArray(int[] arr) {
    System.out.print(Arrays.toString(arr));
  }
}