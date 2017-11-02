package HomeWork2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class BMP {
	
	//define the bitmap file header
	//define the header of bitmap
	 byte []bmpheader= new byte[2];
	 
    //define the whole file size
	 byte [] filesize=new byte[4];
	 
	//define the reserved word
	 byte [] reservedWord = new byte[4];	
	 
	//define the data field offset
	 byte [] bitmapOffset = new byte[4];
	 
	//define the bitmap information header
	//define the info field of bitmap
	 byte [] bitmapInfoSize = new byte[4];
	 
	//define the height and width of the bitmap	 
	 
	 byte [] width=new byte[4];
	 byte [] height=new byte[4];
	 
	//define the 16-bit bitPlane size
	 byte [] bitPlane =new byte[2];
	 
	//define the bitCount of the bitmap
	 byte [] bitCount = new byte[2];
	 
	//define the compressionType of bitmap
	 byte [] compressionType = new byte[4];
	
	//define the imageSize of bitmap
	 byte [] imageSize=new byte[4];
	 
	//define the number of pixel in per meter
	 byte [] XpixelPerMeter=new byte[4];
	 byte [] YpixelPerMeter=new byte[4];
	 
	//define the colorUsed of bitmap
	 byte [] colorUsed = new byte[4];

	//define the importantColor of bitmap
	 byte [] importantColor = new byte[4];
		 
	//define the color table of the bitmap
	 byte [] []colorTable;
	 
	//define the bitmap data field
	 byte bmpData[][];
	 
	 //Constructor
	 public BMP(){	}
	 
	 public BMP(String src) throws Exception{
		 
		 FileInputStream fis=new FileInputStream(src);
		 DataInputStream in=new DataInputStream(fis);
		//read the bitmap file header
			 //read the header of bitmap
			 	in.read(this.bmpheader);
		     //read the whole file size
			 	in.read(filesize);
			 //read the reserved word
			 	in.read(reservedWord);	
			 //read the data field offset
			 	in.read(bitmapOffset);
			 
	    //read the bitmap information header
			//read the info field of bitmap
			 	in.read(bitmapInfoSize); 
			//read the height and width of the bitmap	 
			 	in.read(width);
			 	in.read(height);
			//read the 16-bit bitPlane size
			 	in.read(bitPlane);
			//read the bitCount of the bitmap
			 	in.read(bitCount);
			//read the compressionType of bitmap
			 	in.read(compressionType);
			//read the imageSize of bitmap
			 	in.read(imageSize);
			 
			//read the number of pixel in per meter
			 	in.read(XpixelPerMeter);
			 	in.read(YpixelPerMeter);
			 
			//read the colorUsed of bitmap
			 	in.read(colorUsed);
			
			//read the importantColor of bitmap
			 	in.read(importantColor);
				 
		 //read the color table of the bitmap
			 	colorTable = new byte[(1 << Byte2Int(this.bitCount))&0xffff][4];
				byte [] temp=new byte[4];
				for(int i = 0; i < colorTable.length; i++)
					{
						 in.read(temp);
						 for(int j = 0; j< 4; j++){
							 colorTable[i][j] = temp[j];
						 }
							 
					}
			 
		 //read the bitmap data field
			 	 bmpData=new byte[Byte2Int(height)][Byte2Int(width)];
				 byte [] b =new byte[1];
				 for(int m=0;m<bmpData.length;m++){
					 
					 for(int n=0;n<bmpData[m].length;n++){
						 in.read(b);
						 bmpData[m][n]=b[0];	 
					 }
					 
				 }
	 }
	 
	 public byte [][] getbitMapData(){
		 
		 return this.bmpData;
	 }

	 public String toString(){
		 
		 System.out.println("The bitmap file header:");
		 System.out.println("\tbmpheader:\t\t"+(char)(this.bmpheader[0]&0xff)+" "+(char)(this.bmpheader[1]&0xff));
		 System.out.println("\tfilesize:\t\t"+Byte2Int(this.filesize));
		 System.out.println("\treservedWord:\t\t"+Byte2Int(this.reservedWord));
		 System.out.println("\tbitmapOffset:\t\t"+Byte2Int(this.bitmapOffset));
		 
		 System.out.println("The bitmap information header:");
		 System.out.println("\tbitmapInfoSize:\t\t"+Byte2Int(this.bitmapInfoSize));
		 System.out.println("\tWidth:\t\t\t"+Byte2Int(this.width));
		 System.out.println("\tHeight:\t\t\t"+Byte2Int(this.height));
		 System.out.println("\tbitPlane:\t\t"+Byte2Int(this.bitPlane));
		 System.out.println("\tbitCount:\t\t"+Byte2Int(this.bitCount));
		 System.out.println("\tcompressionType:\t"+Byte2Int(this.compressionType));
		 System.out.println("\timageSize:\t\t"+Byte2Int(this.imageSize));
		 System.out.println("\tXpixelPerMeter:\t\t"+Byte2Int(this.XpixelPerMeter));
		 System.out.println("\tYpixelPerMeter:\t\t"+Byte2Int(this.YpixelPerMeter));
		 System.out.println("\tcolorUsed:\t\t"+Byte2Int(this.colorUsed));
		 System.out.println("\timportantColor:\t\t"+Byte2Int(this.importantColor));
		 
//		 System.out.println("The color table of the bitmap:\n\tB\tG\tR\tR");
		 System.out.println("The color table of the bitmap:\n\t\t\tcolorTable.txt");
//		 for(int i = 0; i < colorTable.length; i++){
//			 for(int j = 0; j < 4; j++)
//				 System.out.print("\t"+(colorTable[i][j]&0xff));
//			 System.out.println();
//		 }
		 
		FileOutputStream fos = null,fos2 = null;
		
		try {
				fos = new FileOutputStream("colorTable.txt");				
				 DataOutputStream dos = new DataOutputStream(fos);
				dos.write("R\tB\tG\tR\n".getBytes("UTF-8"));
				for(int i = 0; i < colorTable.length; i++){
					
				
					 for(int j = colorTable[i].length-2; j>=0; j--)
						 dos.write((Integer.toString(colorTable[i][j]&0xff)+"\t").getBytes("UTF-8"));
					dos.write((Integer.toString(colorTable[i][colorTable[i].length-1]&0xff)+"\t").getBytes("UTF-8"));
					 dos.write("\n".getBytes("UTF-8"));
				}	
				dos.close();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			 
		 //from the bottom left to the upper height 	 
//		 System.out.println("The bitmap data field:\n\tR\tG\tB");
		 System.out.println("The bitmap data field:\n\t\t\tbtimap Data.txt");
		 try {
				fos2 = new FileOutputStream("bitmap Data.txt");
				DataOutputStream dos2 = new DataOutputStream(fos2);
//				dos2.write(0);dos2.write(0);dos2.write(0);dos2.write(0);dos2.write(0);dos2.write(0);
				for(int i = bmpData.length-1; i >=0 ; i--){
					 for(int j = 0; j <bmpData[i].length; j++)
						 dos2.write((Integer.toString(bmpData[i][j]&0xff)+"\t").getBytes("UTF-8"));
					 dos2.write("\n".getBytes("UTF-8"));
				}
				dos2.close();
		 	} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
//		 for(int i = 0; i < 1; i++){
//			 for(int j = 0; j < bmpData[i].length; j++){
//				 System.out.println("\t["+(colorTable[bmpData[i][j]&0xff][2]&0xff)+"\t" + 
//						 (colorTable[bmpData[i][j]&0xff][1]&0xff)+"\t"+(colorTable[bmpData[i][j]&0xff][0]&0xff)+"]");
//			 }
			 

//		 }
		 
		 return null;
		 
	 }
	 
	 
	 
	//converts a 16-bit or 32-bit number  stored in Big-Endian byte order into int
	protected static int Byte2Int(byte [] b)
	    {	if(b.length == 4)
	  	     	return((b[3]&0xff)<<24)|((b[2]&0xff)<<16)|((b[1]&0xff)<<8)|(b[0]&0xff);
	    	else
	    		return((b[1]&0xff)<<8)|(b[0]&0xff);
	    }
	
	//converts a int number into Big-Endian byte order
	protected static void Int2ByteArray(int i,byte[] b)
    {	
	   b[3] = (byte) ((i>>24)&0xff);
	   b[2] = (byte) ((i>>16)&0xff);
	   b[1] = (byte) ((i>>8)&0xff);
	   b[0] = (byte) (i&0xff);
    }
	
	//output the processed bmp
	public void outPut(String dest,int threshold) throws Exception{
		
		 FileOutputStream fos=new FileOutputStream(dest);
		 DataOutputStream dos = new DataOutputStream(fos);
		 int average=0;
		 byte [] temp=new byte[4];
		 
		 dos.write(this.bmpheader);
		 dos.write(this.filesize);
		 dos.write(this.reservedWord);
		 dos.write(this.bitmapOffset);
		 dos.write(this.bitmapInfoSize);
		 dos.write(this.width);
		 dos.write(this.height);
		 dos.write(this.bitPlane);
		 dos.write(this.bitCount);
		 dos.write(this.compressionType);
		 dos.write(this.imageSize);
		 dos.write(this.XpixelPerMeter);
		 dos.write(this.YpixelPerMeter);
		 dos.write(this.colorUsed);
		 dos.write(this.importantColor);
				 
		 for(int m=0;m<colorTable.length;m++){
			 
			   average = (colorTable[m][0]&0xff+colorTable[m][1]&0xff+colorTable[m][2]&0xff)/3;	 
			   if(average >= threshold){
				   temp[0]=(byte) 0xff; temp[1]=(byte)0xff; temp[2]=(byte)0xff; temp[3]=(byte)0xff;
				 }
			   else{ 
				   temp[0]=0; temp[1]=0; temp[2]=0; temp[3]=0;
				 }
			   dos.write(temp);
			 }
		 	
		 for(int i = 0; i < bmpData.length; i++)
			 {
				for(int j=0; j<bmpData[i].length;j++)
				{
					
					dos.write(bmpData[i][j]);
				}			 
			 }
		
	}
	
	
	public static void main(String[] args){
		String src="images\\Lena.bmp";
		 try {
			 	BMP bmp = new BMP(src);
			 	bmp.toString();
			 	bmp.outPut("lena2.bmp",30);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			    e.printStackTrace();
		}
		
		
	}
}
