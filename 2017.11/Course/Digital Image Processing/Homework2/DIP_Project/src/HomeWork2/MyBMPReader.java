package HomeWork2;

import java.io.DataInputStream;
import java.io.FileInputStream;

public class MyBmpReader{
	
	public MyBmpReader(){	}
	
	public void BmpRerader(String src) throws Exception{
		 FileInputStream fis=new FileInputStream(src);
		 DataInputStream in=new DataInputStream(fis);
		 //read the flag of bmp image
		 byte [] fileflag=new byte[2];
		 in.read(fileflag);
		 System.out.println((char)fileflag[0]+" "+(char)fileflag[1]);
		 
		 //read the whole file size
		 byte [] filesize=new byte[4];
		 in.read(filesize);
		 int num=Byte2Int(filesize);
		 System.out.println(num);
		 
		 //skip the reserved word
		 in.skip(4);
		 
		 //read the data field offset
		 byte [] offset=new byte[4];
		 in.read(offset);
		 int dataoffset=Byte2Int(offset);
		 System.out.println("dataoffset="+dataoffset);
		 
		 //skip the info field of image
		 in.skip(4);
		 
		 //read the height and width of the bmp image
		 byte [] height=new byte[4];
		 in.read(height);	 
		 int Height=Byte2Int(height);
		 System.out.println("Height:"+Height);
		 
		 byte [] wide=new byte[4];
		 in.read(wide);
		 int Width=Byte2Int(wide);
		 System.out.println("Width:"+Width);
		 
		 //skip the plane
		 in.skip(2);
		 
		 // read the  bitmap pixels
		 byte [] pixel=new byte[2];
		 in.read(pixel);
		 int pixels=BytetoInt(pixel);
		 System.out.println("pixels:"+pixels);
		 
		 //read the compressionType of bmp
		 byte [] compressionType=new byte[4];
		 in.read(compressionType);	 
		 int CT=Byte2Int(compressionType);
		 System.out.println("CompressionType:"+CT);
		 
		 //read the imageSize of bmp
		 byte [] imageSize=new byte[4];
		 in.read(imageSize);	 
		 int iS=Byte2Int(imageSize);
		 System.out.println("imageSize:"+iS);
		 
		 //skip the number of pixel in per meter
		 in.skip(8);
		 
		 //read the colorUsed of bmp
		 byte [] cu=new byte[4];
		 in.read(cu);	 
		 int colorUsed=Byte2Int(cu);
		 System.out.println("colorUsed:"+colorUsed);
		 
		 //read the importantColor of bmp
		 byte [] ic=new byte[4];
		 in.read(ic);	 
		 int importantColor=Byte2Int(ic);
		 System.out.println("importantColor:"+importantColor);
		 
		//read the palette of the bmp
		 int colorTable[][] = new int[colorUsed][4];
		 byte [] temp=new byte[4];
		 for(int i = 0; i < colorUsed; i++){
			 in.read(temp);
			 for(int j = 0; j< 4; j++)
				 colorTable[i][j] =temp[j]&0xff;
		 }
//		 System.out.println("B\tG\tR\tR");
//		 for(int i = 0; i < colorUsed; i++){
//			 for(int j = 0; j < 4; j++)
//			
//				 System.out.print(colorTable[i][j]+"\t");
//			 System.out.println();
//		 }
		 
		 //read the graph data of bmp
		 
		 int bmpdata[][]=new int[Height*Width][3];
		 byte [] b =new byte[1];
		 for(int k=Height*Width-1;k>=0;k--)
		 {		
			 in.read(b);
			 bmpdata[k][0]=colorTable[b[0]&0xff][0];
			 bmpdata[k][1]=colorTable[b[0]&0xff][1];
			 bmpdata[k][2]=colorTable[b[0]&0xff][3];
		 }
		
//		 System.out.println("R\tG\tB");
//		 for(int i = 0; i < Height*Width; i++){
//				 System.out.println(bmpdata[i][2]+"\t"+bmpdata[i][1]+"\t"+bmpdata[i][0]);
//		 }
//		 
//		 System.out.println(colorTable[114][0]);
//		 System.out.println(colorTable[114][1]);
//		 System.out.println(colorTable[114][2]);
	}	 
	protected static int Byte2Int(byte [] b)
	    {
	  	    return((b[3]&0xff)<<24)|((b[2]&0xff)<<16)|((b[1]&0xff)<<8)|(b[0]&0xff);
	    }	
		
	protected static int BytetoInt(byte [] b)
		{
		    return((b[1]&0xff)<<8)|(b[0]&0xff);
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
