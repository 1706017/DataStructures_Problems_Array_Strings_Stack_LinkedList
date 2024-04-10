import java.io.*;
import java.util.*;

class NonRepeatingElement
{
    public static void main(String[] args)
    {
        int[] arr ={1,2,34,56,2,34,78,78,1,89,98,89,98};

        for(int i=0;i<arr.length;i++) // Corrected declaration of 'i'
        {
            int x = arr[i];
            int count = 0;
            for(int j=0;j<arr.length;j++)
            {
                if(arr[j] == x)
                {
                    count++;
                }
            }
            if(count == 1)
            {
                System.out.println(arr[i]);
            }
        }
    }
}
