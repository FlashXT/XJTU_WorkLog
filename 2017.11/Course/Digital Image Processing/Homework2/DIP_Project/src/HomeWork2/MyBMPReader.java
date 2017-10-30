package HomeWork2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;

public class MyBMPReader {
	public static void main(String [] args)throws IOException{
		 String src="images\\Lena.bmp";
		 FileInputStream fis=new FileInputStream(src);
		 DataInputStream in=new DataInputStream(fis);
		 //读取文件标识
		 byte [] fileflag=new byte[2];
		 in.read(fileflag);
		 System.out.println((char)fileflag[0]+" "+(char)fileflag[1]);
		 //读取文件大小
		 byte [] filesize=new byte[4];
		 in.read(filesize);
		 int num=Byte2Int(filesize);
		 System.out.println(num);
		 //跳过保留字
		 in.skip(4);
		 
		 //获取图像数据区的起始位置
		 byte [] offset=new byte[4];
		 in.read(offset);
		 int dataoffset=Byte2Int(offset);
		 System.out.println(dataoffset);
		 //获取图像信息块的大小
		 byte [] info=new byte[4];
		 in.read(info);
		 int bmpinfo=Byte2Int(info);
		 System.out.println(bmpinfo);
		 

	}
protected static int Byte2Int(byte [] b)
	    {
	  	    return((b[3]&0xff)<<24)|((b[2]&0xff)<<16)|((b[1]&0xff)<<8)|(b[0]&0xff);
	    }
}
