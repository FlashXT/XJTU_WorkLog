package Test;

public class Test {
public static void main(String [] args){
	int i=1;
	System.out.println(intelInt(i));
	
	
}
	
	
	
	protected static int intelInt(int i)
	    {
	  	    return((i&0xff)<<24)+((i&0xff00)<<8)+((i&0xff0000)>>8)+((i>>24)&0xff);
	    }
}
