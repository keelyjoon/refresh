import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Given an integer array arr, and an integer target, return the number of 
// tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.


public class threeSum_With_Multiplicity 
{
    public static int threeSumMulti(int[] arr, int target) 
    {
        //List<ArrayList<String>> listOfLists = new ArrayList<ArrayList<String>>();
        List<Integer> list = new ArrayList<Integer>();
        int temp = 0;
        for (int i = 0; i < arr.length; i++)
        {
            if (temp != arr[i])
            {
                if (temp + arr[i] <= target)
                {
                    temp += arr[i];
                    list.add(arr[i]);    
                }
                else
                {
                    if (temp - arr[i-1] + arr[i] <= target)
                    {
                        temp = arr[i-1] + arr[i];
                        list.remove(arr[i-1]);
                        list.add(arr[i]);
                    }
                }
            }
        }
        System.out.println(list.toString());

        return 3;
    }
    public static void main (String [] args)
    {
        int[] intArray = new int[]{1,1,2,2,3,3,4,4,5,5};
        threeSumMulti(intArray, 8);
    }
}
