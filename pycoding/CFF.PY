public class exchange {
    public static String main(String inputString) {
        String returnvalue;;

        String hex = ASCIITOHEX(inputString);
        System.out.println("hex : " + hex);
        hex = jump(hex);
        System.out.println("jump hex : " + hex);
        String stringXor = calhex(hex);
        System.out.println("string xor : " + stringXor);
//        String xorValue = HEXTOASCII(stringXor);
        int xorValue = Integer.parseInt(stringXor, 16);
        System.out.println("result : " + inputString + (char)xorValue);
        return inputString + (char)xorValue;
//        if (num == 1) {
////            ASCIITOHEX(intro);
//            returnvalue = ASCIITOHEX(intro);
//            System.out.println(returnvalue);
//        }
//        else if (num == 2) {
////            HEXTOASCII(intro);
//            returnvalue = HEXTOASCII(intro);
//            System.out.println(returnvalue);
//        }
//        else {
//            System.out.println("숫자확인");
//        }
    }

    public static String koreanToHexByte(String korean) {
        try {
            byte[] euckrStrBuffer = korean.getBytes("euc-kr");
            System.out.println(byteArrayToHex(euckrStrBuffer));
            return byteArrayToHex(euckrStrBuffer);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return "";
        }
    }

    public static String byteArrayToHex(byte[] a) {
        StringBuilder sb = new StringBuilder();
        for(final byte b: a)
            sb.append(String.format("%02X", b&0xff));
        return sb.toString();
    }

    public static byte[] hexStringTooByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                    + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    public static String HEXTOASCII(String string) {

        if(string.length()%2!=0){
            System.err.println("Invlid hex string.");

        }

        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < string.length(); i = i + 2) {
            // Step-1 Split the hex string into two character group
            String s = string.substring(i, i + 2);
            // Step-2 Convert the each character group into integer using valueOf method
            int n = Integer.valueOf(s, 16);
            // Step-3 Cast the integer value to char
            builder.append((char)n);
        }

//        System.out.println("Hex = " + string);
//        System.out.println("ASCII = " + builder.toString());
        return String.valueOf(builder);
    }

    

    static char[] hexarray={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f','A', 'B', 'C', 'D', 'E', 'F'};
    static String[] hextobin={"0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100",
            "1101", "1110", "1111", "1010", "1011", "1100", "1101", "1110", "1111" };

    
    public static String calhex(String hex) {
        System.out.println("Enter the Hexadecimal numbers:");
        String str= hex;
        String stringArray[] = str.split(" ",0);
        System.out.println(stringArray.length);

        String binary1 = "00000000";
        String binary2 = "00000000";
        String xorValue = "00000000";
        for(int i = 0; i < stringArray.length; i++){
            binary2 = change(stringArray[i]);
            xorValue = xor(binary1,binary2);
            binary1 = xorValue;
        }

        System.out.println(xorValue);
        int i= Integer.parseInt(xorValue,2);
        String hexString = Integer.toHexString(i);
        return hexString;
    }

    
}