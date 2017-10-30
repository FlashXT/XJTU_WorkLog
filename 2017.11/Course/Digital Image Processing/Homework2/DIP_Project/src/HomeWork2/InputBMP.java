package HomeWork2;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.awt.Color;

public class InputBMP {
	 public static int[][] ReadBMPPic(String src) throws IOException
	    {
	        FileInputStream fis=new FileInputStream(src);
	        DataInputStream bis=new DataInputStream(fis);
	            
	        //丢掉文件头信息
	        bis.skip(18);
	        
	        //获取长度与宽度
	        byte[] b1=new byte[4];
	        bis.read(b1);
	        byte[] b2=new byte[4];
	        bis.read(b2);
	        
	        int Width=byte2Int(b1);
	        int Height=byte2Int(b2);
	        System.out.println("Hight:"+Height+" Width:"+Width);
	        int fileSize = intelInt(bis.readInt());
	        System.out.println(fileSize);
	        //因为bmp位图的读取顺序为横向扫描，所以应把数组定义为int[Height][Width]
	        int[][] data=new int[Height][Width];
	        int skipnum=0;
	        
	        //bmp图像区域的大小必须为4的倍数，而它以三个字节存一个像素，读的是偶应当跳过补上的0
	        if(Width*3%4!=0)
	        {
	            skipnum=4-Width*3%4;
	        }
	        System.out.println(skipnum);
	        
	        bis.skip(28);
	        
	        for(int i=0;i<data.length;i++)
	        {
	            for(int j=0;j<data[i].length;j++)
	            {
	                int red=bis.read();
	                int green=bis.read();
	                int blue=bis.read();
	            }
	            if(skipnum!=0)
	            {
	                bis.skip(skipnum);
	            }
	        }
	        
	        bis.close();
	        return data;
	    }
	    private static int byte2Int(byte[] b) throws IOException {
	        // TODO Auto-generated method stub
	        int num=(b[3]&0xff<<24)|(b[2]&0xff)<<16|(b[1]&0xff)<<8|(b[0]&0xff);
	        return num;
	    }
	    public static void main(String[] args) throws IOException {
	        // TODO Auto-generated method stub
//	    	String dir = System.getProperty("user.dir");
//	    	System.out.println(dir);
	        ReadBMPPic("images\\Lena.bmp");
//	    	 FileInputStream fis=new FileInputStream("images\\Lena.BMP");
//	    	 DataInputStream bis=new DataInputStream(fis);
//		   
//		     //获取长度与宽度
//		 	//Verify that the header starts with 'BM'
//			  	if(bis.read() != 'B')
//			  	  throw new IOException("Not a .BMP file!");  	  
//			  		  	
//			  	if(bis.read() != 'M')
//			  	  throw new IOException("Not a .BMP file!");  	  
//			  		  	
//			  	//Get the total file size
//			  	int fileSize = intelInt(bis.readInt());
//			  	
//			  	//Skip the 2 16-bit reserved words
//			  	bis.readUnsignedShort();
//			  	bis.readUnsignedShort();
//			  	
//			  	int bitmapOffset = intelInt(bis.readInt());
//			  	
//			  	int bitmapInfoSize = intelInt(bis.readInt());
//			  	
////			  	int width  = intelInt(bis.readInt());
////			  	int height = intelInt(bis.readInt());
//			  	
//			  	int width  = bis.readInt();
//			  	int height = bis.readInt();
//			  	
//		        System.out.println("Hight:"+height+" Width:"+width);
	    }

protected static int intelInt(int i)
	    {
	  	    return((i&0xff)<<24)+((i&0xff00)<<8)+((i&0xff0000)>>8)+((i>>24)&0xff);
	    }
}
