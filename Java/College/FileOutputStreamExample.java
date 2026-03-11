import java.io.FileOutputStream;  
public class FileOutputStreamExample {  
    public static void main(String args[]){    
           try{    
             FileOutputStream fout=new FileOutputStream("S:\\Roshani\\Amity\\Java Programming\\Java Programs\\PQR.txt");    
             fout.write(65);    
             fout.close();    
             System.out.println("success...");   
             FileOutputStream fout1=new FileOutputStream("S:\\Roshani\\Amity\\Java Programming\\Java Programs\\test.txt");    
             String s="Welcome to java programming.";    
             byte b[]=s.getBytes();//converting string into byte array    
             fout1.write(b);    
             fout1.close();    
             System.out.println("success..."); 
            }catch(Exception e){System.out.println(e);}    
             
      }    
}  
