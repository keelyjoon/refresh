// leetcode question 443. String Compression
// time complexity On
// space complexity O1
class Solution {
    public int compress(char[] chars) {
       // keep track of the index
        int index = 0;
        // pointer to walk through string
        int i = 0;
        while (i < chars.length)
        {
            // second pointer 
            // walking forward while its equal to the character at the i postion
            int j = i;
            while (j < chars.length && chars[j] == chars[i])
            {
                // increment j
                j++;
            }
            // record the character that we just saw
            chars[index++] = chars[i];
            // if we saw the character more than once, we need to compress it 
            if (j - i > 1)
            {
                // convert into string
                String count = j - i + "";
                // make sure you are compressing it correctly
                for (char c: count.toCharArray())
                {
                    chars[index++] = c;
                }
            }
            // update i to point to j
            i = j;
        }
        return index;
    }
}