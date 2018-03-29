/*Algorithm4th,BinarySearch递归版，
 * Author:FlashXT
 * Date:2018.3.28,wednesday
 * */
package Chapter_1;
import java.util.*;
public class recursionBinarySearch {
    public static void main(String [] args){
        int []a={1,2,34,54,21,3,22,41,6,45,67,23,57,78,37};
        Arrays.sort(a);


        System.out.println( BinarySearch(a,0,a.length-1,45));

    }


    public static int BinarySearch(int []a,int low,int high,int key){
        if(low > high) return -1;
        int mid = (low+high)/2;
        if(key == a[mid]) return key;
        else if(key < a[mid]) return BinarySearch(a,low,mid-1,key);
        else return BinarySearch(a,mid+1,high,key);
    }
}
