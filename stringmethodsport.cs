using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Text;

namespace clazz {
    
    class example {
        
        public static void Main(string[] args) {
            
            string phone = "365/654/7824";
            
            string replaced = phone.Replace("/", "-");
            
            Console.WriteLine(replaced);
            
            string text = "yellow";
            
            Console.WriteLine(text.Length);
            
            string alpha = "abcdefghijklmopqrstuvwxyz";
            
            string half = alpha.Substring(14, 6);
            
            Console.WriteLine(half);
            
            string math = "123456789";
            
            string chop = math.Remove(5);
            
            Console.WriteLine(chop);
            
        }
        
    }
    
}