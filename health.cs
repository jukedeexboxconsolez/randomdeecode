using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Text;

// Making A Health System In C#

// health.cs (with bool logic)

namespace health {
    
    class bar {
        
        public static void Main(string[] args) {
            
            string healthbar = "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩";
            
            string dead = "☠️";
            
            bool health = true;
            
            if (health) {
                
                Console.WriteLine("100 Health " + healthbar);
                
                } else if (health == false) {
                    
                    Console.WriteLine("You Are Dead " + dead);
                    
                    
                    
                } else {
                    
                    Console.WriteLine("logic finished");
                    
                }
                
            
            
        }
        
    }
    
}