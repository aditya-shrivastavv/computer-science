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

    // Bubble Sort
    int iterations;
    for (iterations = 0; iterations < arr.length; iterations++) {
      boolean swapped = false;
      for (int i = 0; i < arr.length - iterations - 1; i++) {
        if (arr[i] > arr[i+1]) {
          swapped = true;
          int temp = arr[i];
          arr[i] = arr[i+1];
          arr[i+1] = temp;
        }
      }
      if (!swapped) {
        break;
      }
    }

    System.out.println(Arrays.toString(arr));
    System.out.println("times ran: "+iterations);

    input.close();
  }
}