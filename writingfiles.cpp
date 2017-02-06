#include <iostream>
#include <fstream>
using namespace std;

int main(){
//writing to a file
   ofstream write("C:\\Users\\Pentazoid\\Desktop\\Cplusplus\\OUR_FILE.txt");

   write<<"Windows is sucky I  hate working in it ,  I will get linux as soon as it supports itunes";
   write.close();



    return 0;

}
