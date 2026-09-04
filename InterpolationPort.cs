using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Text;

namespace howtostringinterpolation {
    
    class stringz {
        
        public static void Main(string[] args) {
            
            
            /*
            
            How To Interpoliate Strings (putting all your strings into a print/Console.WriteLine Statement)
            
            */
            
            string dango = "🍡";
            
            string bento = "🍱";
            
            string hut = "🛖";
            
            // After You Get All Your Strings Do As Above
            
            Console.WriteLine($"{dango} {bento} {hut}");
            
            /* 
            
            What I Did Above Basically Is A $ And Then Parethesis That Acts as A Format Specifier Which Has A 
            a bracket as a way to put string names in it  (no , or commas are required after each one)
            make sure the string does exist in the current context otherwise it will give you a compiler error
            
            */
            
            
            
            
            
            
        }
        
    }
    
}