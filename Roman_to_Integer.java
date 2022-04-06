import java.util.ArrayList;
import java.util.List;

/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
 There are six instances where subtraction is used:
    #I can be placed before V (5) and X (10) to make 4 and 9. 
    #X can be placed before L (50) and C (100) to make 40 and 90. 
    #C can be placed before D (500) and M (1000) to make 400 and 900.

 contraints
    #1 <= s.length <= 15
    # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    # it is guaranteed that s is a valid roman numeral in the range [1, 3999]
*/

class Soultion
{
    public static int romanToInt(String s) 
    {
        List<Character> charList = new ArrayList<>();
        for (char ch : s.toCharArray()) 
        {
  
            charList.add(ch);
        }
          
        return -1;
    }
    public static void main(String [] args)
    {
        System.out.println(romanToInt("VIII"));
    }
}
