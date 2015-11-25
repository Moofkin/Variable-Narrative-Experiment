//this processes the files monster1.txt, monster2.txt and monster3.txt

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){

	ifstream file("monster1.txt", ios::in); //opens the file for input

	if (!file) //checks to see if there was an error opening the file, if so, displays error message and terminates the program
	{
		cerr << "File could not be opened" << endl;
		exit(0);
	}

	vector<string> monster1Text;
	string line;

	while (getline(file, line))
    {
		monster1Text.push_back(line);
    }

	file.close();

	for (vector<string>::iterator it = monster1Text.begin() ; it != monster1Text.end(); ++it){
		cout << *it << endl;
	}

	return(0);
}