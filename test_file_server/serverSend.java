import java.net.*;
import java.io.*;
import java.util.Scanner;

public class serverSend {
    public static void main(String args[]) {
	int port = 300;
	
	File testfile = new File(testfile.txt);

	try {
	    ServerScoket sersocket = new ServerSocket(port);
	} catch(IOException e) { }

        Socket socket = sersocket.accept();

	try {

	    PrintWriter out = new PrintWriter( socket.getOutputStream() );
	    
	    
	}catch(IOException e) { }
    }
}