package HomeWork2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;

public class MyBmpReader extends Object{
	
	public MyBmpReader(){	}
	public void BmpRerader(String src) throws Exception{
		 FileInputStream fis=new FileInputStream(src);
		 DataInputStream in=new DataInputStream(fis);
		 //read the flag of bmp image
		 byte [] fileflag=new byte[2];
		 in.read(fileflag);
		 System.out.println(fileflag[0]+" "+fileflag[1]);
		 System.out.println((char)fileflag[0]+" "+(char)fileflag[1]);
		 //read the whole file size
		 byte [] filesize=new byte[4];
		 in.read(filesize);
		 for(byte i : filesize)
			 System.out.println(i);
//		 int num=Byte2Int(filesize);
//		 System.out.println(num);
		 //skip the reserved word
		 in.skip(4);
		 
		 //read the data field begin point
		 byte [] offset=new byte[4];
		 in.read(offset);
		 int dataoffset=Byte2Int(offset);
		 System.out.println("dataoffset="+dataoffset);
		 //��ȡͼ����Ϣ��Ĵ�С
		 in.skip(4);
		 byte [] height=new byte[4];
		 in.read(height);
		 for(byte i : height)
			 System.out.println(i);
			 
		 //int Heigth=Byte2Int(height);
		 System.out.println("Heigth:"+height[3]);
		 
		 byte [] wide=new byte[4];
		 in.read(wide);
		 int Width=Byte2Int(wide);
		 System.out.println("Width:"+Width);
	}	 
	protected static int Byte2Int(byte [] b)
		    {
		  	    return((b[3]&0xff)<<24)|((b[2]&0xff)<<16)|((b[1]&0xff)<<8)|(b[0]&0xff);
		    }	
		
	public static void main(String [] args){
		 String src="images\\Lena.bmp";
		 MyBmpReader bmp= new MyBmpReader();
		 try{
			 bmp.BmpRerader(src);
		 }
		 catch(Exception e){
			 System.out.println(e.getStackTrace());
		 }
		 

	}
}
