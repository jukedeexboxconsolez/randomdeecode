#include <iostream>
using namespace std;

int main() 
{
    
    int xario = 16;
    
    int *pointerx = &xario;
    
    int **pointer = &pointerx;
    
    int ***pointerz = &pointer;
    
    int ****killedpointer = &pointerz;
    
    double wheel = 140.56;
    
    double *weight = &wheel;
    
    double **weight2 = &weight;
    
    double ***twist = &weight2;
    
    double ****twist2 = &twist;
    
    char joystick = 'j';
    
    char *joylock = &joystick;
    char **joykick = &joylock;
    
    char ***point = &joykick;
    
    
}