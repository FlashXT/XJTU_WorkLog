package Test;

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

//�����������������������£������
public class TestEncode {

    public static void main(String[] args) throws Exception{ 
        DataOutputStream dos = null; //�����������������
        File f = new File("C:\\Users\\Flash_XT\\Desktop" + File.separator + "colorTable.txt");//ָ���ļ��ı���·��
        OutputStreamWriter oStreamWriter = new OutputStreamWriter(new FileOutputStream(f), "utf-8");
        dos = new DataOutputStream(new FileOutputStream(f));//ʵ�����������������   
        String names[] = {"����","����","Χ��"};//��Ʒ����
        float prices[] = {98.3f,30.3f,50.5f};    //��Ʒ�۸� 
        int nums[] = {3,2,1};    //��Ʒ���� 
        for(int i = 0;i<names.length;i++){   
            //ѭ��д��   
//            dos.writeChar(names[i]);    //д���ַ���
//            dos.writeChar('\t');    //����ָ���
//            dos.writeFloat(prices[i]);  //д��С�� 
//            dos.writeChar('\t'); //����ָ���  
//            dos.writeInt(nums[i]); //д������ 
//            dos.writeChar('\n');    //����
                   
            oStreamWriter.write(names[i]);
            oStreamWriter.write('\t');
            oStreamWriter.write(prices[i]+"     ");  //д��С�� 
            oStreamWriter.write('\t'); //����ָ���
            oStreamWriter.write(nums[i]); //д������  
            oStreamWriter.write('\n');  //����
            }  
            oStreamWriter.close();  //�ر������
            dos.close();
    }
    
}