import java.io.*;
import java.util.Arrays;
import java.util.TreeSet;

public class gatherWords{


    public static boolean checkWord(String word) {

        if(word.indexOf("_") > 0) {
            return false;
        }

        return true;
    }

    public static boolean allUpper(String word) {
        char[] charArray = word.toCharArray();
        boolean allUpper = true;
        for(int i=0; i < charArray.length; i++){
            
            if(Character.isLowerCase(charArray[i]))
                allUpper = false;
        }
        return allUpper;
    }

        

    public static void main(String args[]) throws IOException {

        
        File newFile = new File("words.txt");
        if (newFile.createNewFile()) {
            System.out.println("File created: " + newFile.getName());
        }

        FileWriter myWriter = new FileWriter("words.txt");

        File path = new File(System.getProperty("user.dir"));

        String[] pn = path.list();

        TreeSet<String> pathnames = new TreeSet<>(Arrays.asList(pn));

        int itr = 0;

        for(String filePath : pathnames) {

            if(!filePath.contains(".csv"))
                continue;

            System.out.println(itr + "/26");

            TreeSet<String> words = new TreeSet<>();

            File f = new File(filePath);
            FileReader fr = new FileReader(f);
            BufferedReader br = new BufferedReader(fr);
            String line = "";
            String[] tempArr;
            boolean first = true;

            while((line = br.readLine()) != null) {
                if(first) {
                    first = false;
                    continue;
                }
                tempArr = line.split(",");

                if(checkWord(tempArr[0])) {

                    if(allUpper(tempArr[0])) {
                        words.add(tempArr[0].toLowerCase());
                    }
                    else {
                        words.add(tempArr[0]);
                    }
                
                }
            }
            br.close();

            for(String w: words) {
                myWriter.write(w + "\n");
            }

            itr++;

        }
        
        myWriter.close();

    }

}