package sort;

import java.util.Arrays;
import java.util.Scanner;

public class insertionSort {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int[] arr = new int[8];

        System.out.println("enter 8 elements in the array");
        for (int i = 0; i < arr.length; i++) {
            System.out.print("enter "+(i+1)+" element: ");
            int element = input.nextInt();
            arr[i] = element;
        }

        // Insertion Sort
        for (int i = 1; i < arr.length; i++) {
            int insertElement = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > insertElement) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = insertElement;
        }
        System.out.println(Arrays.toString(arr));

        input.close();
    }
}