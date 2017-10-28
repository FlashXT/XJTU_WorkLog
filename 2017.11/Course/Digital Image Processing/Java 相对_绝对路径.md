# <center/>Java 相对/绝对路径 #
文件路径分为绝对路径和相对路径，具体来说Java中的有4种路径：

1. URI形式的绝对资源路径：例如：file:/E:/EclipseWorkSpace/JavaTest/bin/images/me.jpg。URL是URI的特例，URL的前缀必须是Java认识的。URL可以打开资源而URI不行。URL和URI可以通过各自的toURI()和toURL()方法进行转换。

2. 本地系统的绝对路径：例如：E:\EclipseWorkSpace\JavaTest\resources\武汉大学.kml。Java.io包中的类需要使用这种形式的参数。但是它们一般也提供了URI类型的参数，而URI类型的参数接收的是URI样式的String。因此，通过URI转换还是可以把URI样式的绝对路径用在java.io包中的类。

3. 相对于classpath的相对路径：例如：相对于路径file:/E:/EclipseWorkSpace/JavaTest/bin/的路径。其中，bin是项目的classpath。所有的Java源文件编译后的class文件都会复制到这个目录中。

4. 相对于当前用户目录的相对路径：就是相对于System.getProperty("user.dir")返回的路径。一般对项目而言，这是项目的根目录。一般不使用相对于用户目录的相对路径。

一般的JavaSE程序中，我们一般将资源文件放到src文件夹下。下面来看实例一些访问文件路径的实例：

    import java.io.File;  
    import java.io.IOException;  
    import java.util.Properties;  
    public class PathDemo {  
          
        public static void main(String[] args) throws IOException {  
            //第一种方式，我的工程目录是JavaTest  
            System.out.println("第一种方式");  
            String path = System.getProperty("user.dir");// 获得项目根目录的绝对路径  
            System.out.println(path);  
            Properties properties = System.getProperties();  
            System.out.println(properties.getProperty("user.dir"));  
            //第二种方式，这里我的文件目录是这样的：JavaTest（工程目录）\resources\武汉大学.kml  
            System.out.println("第二种方式");  
            File file = new File("resources/武汉大学.kml");  
            if (file.exists()) {  
                System.out.println(file.getAbsolutePath());//获取绝对路径  
                System.out.println(file.getCanonicalPath());//获取标准路径  
            }  
            //第三种方式，这里我的文件目录是这样的：JavaTest（工程目录）\src\images\me.jpg  
            System.out.println("第三种方式");  
            System.out.println(PathDemo.class.getResource("/"));//得到当前类文件的URL目录  
            System.out.println(PathDemo.class.getResource(""));//得到当前类的classpath目录  
            System.out.println(PathDemo.class.getResource("./"));  
                    //这里访问文件的时候目录前面要加/  
            System.out.println(PathDemo.class.getResource("/images/me.jpg"));  
            //第四种方式，这里我的文件目录是这样的：JavaTest（工程目录）\src\images\me.jpg     
            System.out.println("第四种方式");  
            System.out.println(PathDemo.class.getClassLoader().getResource(""));  
                    //这里访问文件的时候目录前面不能加/  
            System.out.println(PathDemo.class.getClassLoader().getResource("images/me.jpg"));  
        }  
    }  
输出：    

		第一种方式  
		E:\EclipseWorkSpace\JavaTest  
		E:\EclipseWorkSpace\JavaTest  
		第二种方式  
		E:\EclipseWorkSpace\JavaTest\resources\武汉大学.kml  
		E:\EclipseWorkSpace\JavaTest\resources\武汉大学.kml  
		第三种方式  
		file:/E:/EclipseWorkSpace/JavaTest/bin/  
		file:/E:/EclipseWorkSpace/JavaTest/bin/cn/tzy/path/  
		file:/E:/EclipseWorkSpace/JavaTest/bin/cn/tzy/path/  
		file:/E:/EclipseWorkSpace/JavaTest/bin/images/me.jpg  
		第四种方式  
		file:/E:/EclipseWorkSpace/JavaTest/bin/  
		file:/E:/EclipseWorkSpace/JavaTest/bin/images/me.jpg  

那如果文件不位于src文件夹中，我们可以这样访问：

		    public class FilePathDemo {  
		        public static void main(String[] args) throws IOException {  
		            //文件直接在工程目录下，这里的工程目录为JavaTest  
		            File txtFile = new File("readme.txt");  
		            if (!txtFile.exists()) {  
		                txtFile.createNewFile();  
		            }  
		            System.out.println(txtFile.getAbsolutePath());  
		            //文件在工程文件的子目录中，这里的子目录前面不能加/  
		            File imgFile = new File("resources/me.jpg");  
		            if (!imgFile.exists()) {  
		                imgFile.createNewFile();  
		            }  
		            System.out.println(imgFile.getAbsolutePath());  
		        }  
		    } 
 运行结果如下：

		    E:\EclipseWorkSpace\JavaTest\readme.txt  
			E:\EclipseWorkSpace\JavaTest\resources\me.jpg  