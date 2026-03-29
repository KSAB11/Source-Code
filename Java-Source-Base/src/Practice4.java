
import java.util.Arrays;

public class Practice4 {

    // Insertion sort

    public static void insertionSort() {
        int[] arr = {5, 7, 1, 0, -2, 3}; // Array
        int n = arr.length; // Array length

        System.out.print("Unsorted order: " + Arrays.toString(arr)); // Display original order

        for (int i = 1; i < n; i++) {
            int temp = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > temp) { // > ascending order / < descending order
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = temp;
        }
        System.out.print("\nSorted order: " + Arrays.toString(arr)); // Display sorted order
    }

    public static void main(String[] args) {
            Practice4.insertionSort();
        }
    }

