import java.io.*;
import java.util.*;

class MajorityElement {
    public static void main(String[] args) {
        int[] array = {1, 23, 1, 34, 1, 56}; 
        int countCompare = array.length / 2; 
        for (int i = 0; i < array.length; i++) {
            int majorityElement = array[i];
            int count = 0;
            for (int j = 0; j < array.length; j++) {
                if (array[j] == majorityElement) { 
                    count++;
                }
            }
            if (count > countCompare) {
                System.out.println("Majority element is " + array[i]); 
            } else {
                continue;
            }
        }
    }
}
